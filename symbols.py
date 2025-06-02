import pygame
from settings import SYMBOL_WIDTH, SYMBOL_HEIGHT


class Symbol(pygame.sprite.Sprite):
    def __init__(self, pathToFile, pos, idx, name):
        super().__init__()
        self.name = name  # store the name of the symbols
        self.raw_image = pygame.image.load(pathToFile).convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (SYMBOL_WIDTH, SYMBOL_HEIGHT))
        self.rect = self.image.get_rect(topleft=pos)
        self.x_val = self.rect.left
        self.idx = idx
        # For animations (fade in/out)
        self.size_x = SYMBOL_WIDTH
        self.size_y = SYMBOL_HEIGHT
        self.alpha = 255
        self.fade_in = False
        self.fade_out = False

    def update(self):
        # Slightly increases size of winning symbols
        if self.fade_in:
            if self.size_x < 250:
                self.size_x += 1
                self.size_y += 1
                self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))

        # Fades out non-winning symbols
        elif not self.fade_in and self.fade_out:
            if self.alpha > 115:
                self.alpha -= 7
                self.image.set_alpha(self.alpha)

    def __repr__(self):
        return self.name
