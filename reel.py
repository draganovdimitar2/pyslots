import pygame
from random import choice, choices
from settings import *
from symbols import Symbol


class Reel:
    def __init__(self, pos: tuple):  # pass the tuple for pos from machine class (x_topleft, y_topleft)
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = choices(weighted_symbols, k=5)  # both shuffle and limits the reels to 5
        self.reel_is_spinning = False
        self.delay_time = 0
        self.spin_time = 0

        for idx, item in enumerate(self.shuffled_keys):
            symbol_path = symbols[item]
            self.symbol_list.add(Symbol(symbol_path, pos, idx, item))  # <-- add name
            pos = (pos[0], pos[1] + SYMBOL_HEIGHT)

    def animate(self, delta_time):
        if self.reel_is_spinning:
            self.delay_time -= delta_time * 1000
            self.spin_time -= delta_time * 1000
            reel_is_stopping = False

            if self.spin_time < 0:
                reel_is_stopping = True

            if self.delay_time <= 0:  # starting the animations

                # Iterate through all 5 symbols in the reel; truncate; add new symbol on top of the stack
                for symbol in self.symbol_list:
                    symbol.rect.bottom += 20  # each tick move each symbol downwards

                    # when we hit the end of the screen remove the reel (if it is spinning)
                    if symbol.rect.top == GAME_HEIGHT + SYMBOL_HEIGHT:
                        if reel_is_stopping:
                            self.reel_is_spinning = False
                            # play stop audio
                        symbol_idx = symbol.idx  # save the current idx so later we can spawn on this place
                        symbol.kill()
                        # spawn random symbol in place of the above
                        new_name = choice(self.shuffled_keys)
                        symbol_path = symbols[new_name]
                        self.symbol_list.add(
                            Symbol(symbol_path, (symbol.x_val, -SYMBOL_HEIGHT), symbol_idx, new_name))


