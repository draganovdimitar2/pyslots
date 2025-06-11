from player import Player
import random, pygame
from settings import *
from typing import List, Tuple


class UI:
    def __init__(self, player: "Player"):
        self.player: Player = player
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.font, self.bet_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE), pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.win_font = pygame.font.Font(UI_FONT, WIN_FONT_SIZE)
        self.win_text_angle = random.randint(-4, 4)

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

        # Draw data
        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, lines_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        self.display_surface.blit(balance_surf, balance_rect)
        self.display_surface.blit(lines_surf, lines_rect)
        self.display_surface.blit(bet_sur, bet_rect)

        # Print last win if applicable
        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surf = self.win_font.render("WIN! $" + last_payout, True, TEXT_COLOR, None)
            x1 = WIDTH // 2
            y1 = HEIGHT - 120
            win_surf = pygame.transform.rotate(win_surf, self.win_text_angle)  # to tilt the text
            win_rect = win_surf.get_rect(center=(x1, y1))
            self.display_surface.blit(win_surf, win_rect)

    def draw_win_lines(self, points: List[Tuple[int, int]]) -> None:
        line_color = (255, 0, 0)
        line_thickness = 3

        pygame.draw.lines(self.display_surface, line_color, False, points, line_thickness)
        # Add circles at connection points for better visibility
        for point in points:
            pygame.draw.circle(self.display_surface, line_color, point, 4)

    def update(self) -> None:
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, HEIGHT - UI_HEIGHT, WIDTH, UI_HEIGHT))
        self.display_info()
