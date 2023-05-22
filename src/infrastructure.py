import pygame
from typing import Optional
from .direction import Direction
from .constants import *


class Infrastructure:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, SCALE)
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()

    def is_quit_event(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit event")
                return True
        return False

    def get_pressed_key(self) -> Optional[Direction]:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Direction.DOWN
        if key[pygame.K_RIGHT]:
            return Direction.RIGHT
        if key[pygame.K_DOWN]:
            return Direction.UP
        if key[pygame.K_LEFT]:
            return Direction.LEFT

        return None

    def fill_screen(self):
        self.screen.fill(SCREEN_COLOR)

    def draw_element(self, x, y, color):
        pygame.draw.rect(
            self.screen,
            pygame.Color(color),
            (x * SCALE, y * SCALE, ELEMENT_SIZE, ELEMENT_SIZE),
            0,
            RADIUS,
        )

    def draw_score(self, score: int) -> None:
        self.screen.blit(
            self.font.render(f"Score: {score}", True, pygame.Color(SCORE_COLOR)),
            (5, 5),
        )

    def draw_game_over(self) -> None:
        message = self.font.render("GAME OVER", True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get_rect(center=((WIDTH // 2 * SCALE), (HEIGHT // 2 * SCALE))),
        )

    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    def quit(self) -> None:
        pygame.quit()
