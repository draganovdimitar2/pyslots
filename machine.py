import pygame
from settings import *
from reel import Reel
from player import Player
from ui import UI
from random import randint


class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.machine_balance = 10000
        self.reel_index = 0
        self.won_lines_count = 0
        self.reel_list = {}  # {reel_key: reel_class_obj}
        self.can_toggle = True  # to be able to spin the machine
        self.spinning = False
        self.win_animation_ongoing = False
        self.can_animate = False
        self.win_data = None
        # win_data is in this format ->  {(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}

        # Results
        self.spin_result = {0: None, 1: None, 2: None, 3: None, 4: None}
        # spin_result is in this format ->  {0: ['star', 'clover', 'star'], 1: ['clover', 'diamond', 'clover'], 2: ['star', 'star', 'star'], 3: ['diamond', 'clover', 'star'], 4: ['star', 'star', 'diamond']}

        self.spawn_reels()
        self.currPlayer = Player()
        self.ui = UI(self.currPlayer)

        # sound_effects
        self.spin_sound = pygame.mixer.Sound('audio/spinning.mp3')
        self.spin_sound.set_volume(0.15)
        self.win_sound = pygame.mixer.Sound('audio/winning.mp3')
        self.win_sound.set_volume(0.5)

    def cooldowns(self):
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
                # Play the win audio
                self.win_sound.play()
                self.pay_player()
                self.win_animation_ongoing = True
                self.ui.win_text_angle = randint(-4, 4)

    def input(self, events):
        if self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
            keys = pygame.key.get_pressed()

            # Space key triggers on press (can be held)
            if keys[pygame.K_SPACE]:
                self.toggle_spinning()
                self.currPlayer.place_bet()
                self.machine_balance += self.currPlayer.bet_size
                self.currPlayer.last_payout = None

            # Check for KEYUP events for arrows only
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

    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self):
        x_topleft, y_topleft = 0, 0
        if not self.reel_list:
            x_topleft, y_topleft = 0, -SYMBOL_HEIGHT
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + SYMBOL_WIDTH, y_topleft

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))  # Need to create reel class
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spinning = not self.spinning
            self.can_toggle = False
            self.won_lines_count = 0

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * DELAY_FOR_EACH_REEL)
                # play spin audio
                self.spin_sound.play()
                self.win_animation_ongoing = False

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result

    def flip_reels_horizontally(self):
        # Extract columns in sorted key order to ensure consistent ordering
        horizontal_values = [v for v in self.spin_result.values()]

        rows, cols = len(horizontal_values), len(horizontal_values[0])

        hvals2 = [
            # outer loop: iterate over each column index in the original grid
            # inner loop: for each column, collect values from bottom to top across rows (x)
            [horizontal_values[x][y] for x in reversed(range(rows))]  # reverse row order to simulate rotation
            for y in range(cols)  # # each new row corresponds to a column in the original grid
        ]

        # Reverse each row to complete the horizontal flip
        return [row[::-1] for row in hvals2]

    def check_wins(self):
        winning_lines = []  # This will store complete paylines that win
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
                winning_lines.append(line)  # Add the complete winning payline

        if winning_lines:
            self.won_lines_count = len(winning_lines)
            print(winning_lines)
            print(self.won_lines_count)
            self.can_animate = True
            return winning_lines
        return None


