import pygame
import random
from settings import WIDTH, HEIGHT
from typing import List, Sequence

class Coin(pygame.sprite.Sprite):
    def __init__(self, images: pygame.Surface) -> None:
        super().__init__()
        self.images: pygame.Surface = images
        self.image_index: int = 0
        self.image: pygame.Surface = self.images[self.image_index]
        self.rect: pygame.Rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.timer: float = 0
        self.animation_speed: float = 0.1
        self.velocity: List[float] = [random.uniform(-1, 1), random.uniform(-2, -1)]

    def update(self, dt: float) -> None:
        self.timer += dt
        if self.timer >= self.animation_speed:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.timer = 0

        # Move the coin
        self.rect.x += self.velocity[0] * 60 * dt
        self.rect.y += self.velocity[1] * 60 * dt

        # Respawn if off screen
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.center = (random.randint(0, WIDTH), HEIGHT)
            self.velocity = [random.uniform(-1, 1), random.uniform(-2, -1)]


class CoinAnimation:
    def __init__(self, coin_image_paths: List[str]) -> None:
        self.coin_images: List[pygame.Surface] = [pygame.transform.scale(pygame.image.load(path).convert_alpha(), (80, 80)) for path in coin_image_paths]
        self.coins: pygame.sprite.Group = pygame.sprite.Group()
        self.active: bool = False
        self.duration: int = 5 # seconds
        self.timer: int = 0

    def trigger(self) -> None:
        self.active = True
        self.timer = self.duration
        self.coins.empty()
        for _ in range(30):  # spawn 30 animated coins
            self.coins.add(Coin(self.coin_images))

    def update(self, dt: float) -> None:
        if self.active:
            self.timer -= dt
            if self.timer <= 0:
                self.active = False
                self.coins.empty()
            else:
                self.coins.update(dt)

    def draw(self, surface: pygame.Surface) -> None:
        if self.active:
            self.coins.draw(surface)
