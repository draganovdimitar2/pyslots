import pygame
from settings import SYMBOL_WIDTH, SYMBOL_HEIGHT
from typing import Tuple


class Symbol(pygame.sprite.Sprite):
    def __init__(self, path_to_file: str, pos: Tuple[int, int], idx: int, name: str) -> None:
        super().__init__()
        self.name: str = name  # store the name of the symbols
        self.raw_image: pygame.Surface = pygame.image.load(path_to_file).convert_alpha()
        self.image: pygame.Surface = pygame.transform.scale(self.raw_image, (SYMBOL_WIDTH, SYMBOL_HEIGHT))
        self.rect: pygame.Rect = self.image.get_rect(topleft=pos)
        self.x_val: int = self.rect.left
        self.idx: int = idx
        # for animations (fade in/out)
        self.size_x: int = SYMBOL_WIDTH
        self.size_y: int = SYMBOL_HEIGHT
        self.alpha: int = 255
        self.fade_in: bool = False
        self.fade_out: bool = False

    def reset_state(self) -> None:
         self.fade_in = False
         self.fade_out = False
         self.alpha = 255
         self.size_x = SYMBOL_WIDTH
         self.size_y = SYMBOL_HEIGHT
         # Re-scale the image and set alpha immediately
         self.image = pygame.transform.scale(self.raw_image, (self.size_x, self.size_y))
         self.image.set_alpha(self.alpha)

    def update(self) -> None:
        # slightly increases size of winning symbols
        if self.fade_in:
            if self.size_x < 250:
                self.size_x += 1
                self.size_y += 1
                self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))

        # fades out non-winning symbols
        elif not self.fade_in and self.fade_out:
            if self.alpha > 115:
                self.alpha -= 7
                self.image.set_alpha(self.alpha)

    def __repr__(self) -> str:
        return self.name
