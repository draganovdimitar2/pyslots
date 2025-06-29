import pygame
from settings import FPS, WIDTH, HEIGHT, BACKGROUND
from sys import exit
from machine import Machine


class GameController:
    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine Demo')
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.bg_unscaled: pygame.Surface = pygame.image.load(BACKGROUND).convert()
        self.background: pygame.Surface = pygame.transform.scale(self.bg_unscaled, (WIDTH, HEIGHT))
        self.machine: Machine = Machine()
        self.delta_time: float = 0.0

        # Sound
        # main_sound = pygame.mixer.Sound('audio/main_song.mp3')
        # main_sound.play()

    def run(self) -> None:
        start_time = pygame.time.get_ticks()
        running = True
        while running:
            events = pygame.event.get()  # Get all events once

            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    exit()

            self.delta_time = (pygame.time.get_ticks() - start_time) / 1000
            start_time = pygame.time.get_ticks()

            self.screen.blit(self.background, (0, 0))  # draw background

            self.machine.update(self.delta_time, events)  # pass events here

            self.clock.tick(FPS)
            pygame.display.update()


if __name__ == '__main__':
    game = GameController()
    game.run()
