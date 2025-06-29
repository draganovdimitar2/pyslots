from player import Player
import random, pygame
from settings import *
from typing import List, Tuple


class UI:
    """
     Handle only user interface-related elements (balance, bet, lines..)
    """
    def __init__(self, player: "Player") -> None:
        self.player: Player = player
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.font: pygame.font.Font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.bet_font: pygame.font.Font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.win_font: pygame.font.Font = pygame.font.Font(UI_FONT, WIN_FONT_SIZE)
        self.win_text_angle: int = random.randint(-4, 4)

        self.jackpot_timer: float = 0.0
        self.jackpot_duration: float = 5.0  # seconds to show jackpot message
        self.jackpot_amount: int = 0

    def display_info(self) -> None:
        player_data = self.player.get_data()

        balance_surf = self.font.render("Balance: $" + player_data['balance'], True, TEXT_COLOR, None)
        x, y = 20, UI_FONT_POS_Y
        balance_rect = balance_surf.get_rect(bottomleft=(x, y))

        lines_surf = self.font.render(f"Lines: {self.player.lines}", True, TEXT_COLOR, None)
        x = WIDTH // 2 - 40
        lines_rect = lines_surf.get_rect(bottomleft=(x, y))

        bet_sur = self.bet_font.render("Wager: $" + player_data['bet_size'], True, TEXT_COLOR, None)
        x = WIDTH - 20
        bet_rect = bet_sur.get_rect(bottomright=(x, y))

        # draw data
        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, lines_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        self.display_surface.blit(balance_surf, balance_rect)
        self.display_surface.blit(lines_surf, lines_rect)
        self.display_surface.blit(bet_sur, bet_rect)

        # print last win if applicable
        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surf = self.win_font.render("WIN! $" + last_payout, True, TEXT_COLOR, None)
            x1 = WIDTH // 2
            y1 = HEIGHT - 120
            win_surf = pygame.transform.rotate(win_surf, self.win_text_angle)  # to tilt the text
            win_rect = win_surf.get_rect(center=(x1, y1))
            self.display_surface.blit(win_surf, win_rect)

    def draw_win_lines(self, points: List[Tuple[int, int]]) -> None:
        line_color = (255, 255, 255)
        line_thickness = 3

        pygame.draw.lines(self.display_surface, line_color, False, points, line_thickness)


    def mystery_hit(self, mystery_amount: int) -> None:  #  sets the jackpot amount and resets the timer
        self.jackpot_amount = mystery_amount
        self.jackpot_timer = self.jackpot_duration

    def jackpot_font(self) -> None:
        if self.jackpot_timer > 0:
            font = pygame.font.SysFont(None, 150)

            r = random.randint(200, 255)
            g = random.randint(0, 220)
            b = random.randint(0, 0)
            # line 1: "JACKPOT!"
            text1 = font.render("JACKPOT!", True, (r, g, b))
            text1_rect = text1.get_rect(center=(self.display_surface.get_width() // 2, self.display_surface.get_height() // 3))

            # line 2: "Won xxx.xx coins!"
            text2 = font.render(f"Won {int(self.jackpot_amount)}$!", True, (r, g, b))
            text2_rect = text2.get_rect(center=(self.display_surface.get_width() // 2, text1_rect.bottom + 150))

            # blit both
            self.display_surface.blit(text1, text1_rect)
            self.display_surface.blit(text2, text2_rect)

            # Countdown timer
            self.jackpot_timer -= 1 / 60


    def update(self, target_surface: pygame.Surface) -> None:
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, HEIGHT - UI_HEIGHT, WIDTH, UI_HEIGHT))
        self.display_info()
        self.jackpot_font()

