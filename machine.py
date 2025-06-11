import pygame
from settings import *
from reel import Reel
from player import Player
from ui import UI
from random import randint
from typing import Dict, Optional, List, Tuple, Set, Sequence


class Machine:
    def __init__(self) -> None:
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.machine_balance: int = 10000
        self.reel_index: int = 0
        self.won_lines_count: int = 0
        self.reel_list: Dict[int, Reel] = {}  # map reel index to Reel instance
        self.can_toggle: bool = True
        self.spinning: bool = False
        self.win_animation_ongoing: bool = False
        self.can_animate: bool = False
        self.win_data: Optional[Sequence[Set[Tuple[int, int]]]] = None
        # win_data is in this format ->  {(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}

        # Results
        self.spin_result: Dict[int, Optional[List[str]]] = {i: None for i in range(5)}
        # spin_result is in this format ->  {0: ['star', 'clover', 'star'], 1: ['clover', 'diamond', 'clover'], 2: ['star', 'star', 'star'], 3: ['diamond', 'clover', 'star'], 4: ['star', 'star', 'diamond']}

        self.spawn_reels()
        self.currPlayer: Player = Player()
        self.ui: UI = UI(self.currPlayer)

        # sound_effects
        self.spin_sound: pygame.mixer.Sound = pygame.mixer.Sound('audio/spinning.mp3')
        self.spin_sound.set_volume(0.15)
        self.win_sound: pygame.mixer.Sound = pygame.mixer.Sound('audio/winning.mp3')
        self.win_sound.set_volume(0.5)

    def cooldowns(self) -> None:
        # only lets player to spin if all reels are not spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True
        if not self.can_toggle and all(not self.reel_list[reel].reel_is_spinning for reel in
                                       self.reel_list):  # making sure all 5 reels are not spinning
            self.can_toggle = True
            self.spin_result = self.get_result()
            if self.check_wins():
                self.win_data = self.check_wins()
                # play the win audio
                self.win_sound.play()
                self.pay_player()
                self.win_animation_ongoing = True
                self.ui.win_text_angle = randint(-4, 4)

    def input(self, events: Sequence[pygame.event.Event]) -> None:
        if self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.toggle_spinning()
                self.currPlayer.place_bet()
                self.machine_balance += self.currPlayer.bet_size
                self.currPlayer.last_payout = None

            for event in events:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        if self.currPlayer.lines > 1:
                            self.currPlayer.lines -= 1
                    elif event.key == pygame.K_UP:
                        if self.currPlayer.lines < len(PAYLINES):
                            self.currPlayer.lines += 1
                    elif event.key == pygame.K_RIGHT:
                        if self.currPlayer.bet_size < 20:
                            self.currPlayer.bet_size += 1
                    elif event.key == pygame.K_LEFT:
                        if self.currPlayer.bet_size > 0:
                            self.currPlayer.bet_size -= 1

    def draw_symbols_on_each_reel(self) -> None:
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()

    def draw_reels(self, delta_time: float) -> None:
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self) -> None:
        x_topleft, y_topleft = 0, 0
        if not self.reel_list:
            x_topleft, y_topleft = 0, -SYMBOL_HEIGHT
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + SYMBOL_WIDTH, y_topleft

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))  # need to create reel class
            self.reel_index += 1

    def toggle_spinning(self) -> None:
        if self.can_toggle:
            self.spinning = not self.spinning
            self.can_toggle = False
            self.won_lines_count = 0

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * DELAY_FOR_EACH_REEL)
                # play spin audio
                self.spin_sound.play()
                self.win_animation_ongoing = False

    def get_result(self) -> Dict[int, List[str]]:
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result

    def flip_reels_horizontally(self) -> List[List[str]]:
        # extract columns in sorted key order to ensure consistent ordering
        horizontal_values = [v for v in self.spin_result.values()]

        rows, cols = len(horizontal_values), len(horizontal_values[0])

        hvals2 = [
            # outer loop: iterate over each column index in the original grid
            # inner loop: for each column, collect values from bottom to top across rows (x)
            [horizontal_values[x][y] for x in reversed(range(rows))]  # reverse row order to simulate rotation
            for y in range(cols)  # # each new row corresponds to a column in the original grid
        ]

        # reverse each row to complete the horizontal flip
        return [row[::-1] for row in hvals2]

    def check_wins(self) -> Sequence[List[Sequence[Tuple[int, int]]]] | None:
        winning_lines = []  # this will store complete paylines that win
        horizontal = self.flip_reels_horizontally()

        for line_idx in range(self.currPlayer.lines):
            line = PAYLINES[line_idx]
            symbol = None
            is_winning = True
            for (row, col) in line:
                if symbol is None:
                    symbol = horizontal[row][col]
                if horizontal[row][col] != symbol:
                    is_winning = False
                    break

            if is_winning:
                winning_lines.append(line)  # add the complete winning payline

        if winning_lines:
            self.won_lines_count = len(winning_lines)
            print(winning_lines)
            print(self.won_lines_count)
            self.can_animate = True
            return winning_lines
        return None

    def pay_player(self) -> None:
        spin_payout = self.currPlayer.bet_size * (3 * self.won_lines_count)
        self.currPlayer.balance += spin_payout
        self.machine_balance -= spin_payout
        self.currPlayer.last_payout = spin_payout
        self.currPlayer.total_won += spin_payout

    def win_animation(self) -> None:
        if self.win_animation_ongoing and self.win_data:
            # then apply effects to winning symbols in complete paylines
            for payline in self.win_data:
                for (row, col) in payline:
                    reel = self.reel_list[col]
                    symbols = reel.symbol_list.sprites()[::-1]  # reverse to match top-down
                    symbol = symbols[row + 1]  # visible rows start from index 1
                    symbol.fade_in = True

                    # set non-winning symbols to fade out
                    for other_reel in self.reel_list.values():
                        for other_symbol in other_reel.symbol_list:
                            if not hasattr(other_symbol, 'fade_in') or not other_symbol.fade_in:
                                other_symbol.fade_out = True

    def win_lines(self) -> None:
        if not self.win_animation_ongoing or not self.win_data:
            return

        # for each complete winning payline
        for payline in self.win_data:
            points = []
            for (row, col) in payline:
                # get the corresponding reel and symbol sprite
                reel = self.reel_list[col]
                symbols_sprite = reel.symbol_list.sprites()
                symbols_reversed = symbols_sprite[::-1]  # reverse to match top-down visual layout

                # symbols visible rows start from index 1
                symbol = symbols_reversed[row + 1]

                # get the center of the symbol rect to connect the line smoothly
                center_pos = symbol.rect.center
                # when symbols fade they got to the right direction slightly so add 10px on the x value
                new_pos = (center_pos[0] + 10, center_pos[1])
                points.append(new_pos)

            if len(points) > 1:
                self.ui.draw_win_lines(points)

    def update(self, delta_time: float, events: Sequence[pygame.event.Event]) -> None:
        self.cooldowns()
        self.input(events)  # constantly check for user input
        self.draw_reels(delta_time)
        self.draw_symbols_on_each_reel()
        self.ui.update()
        self.win_animation()
        self.win_lines()
