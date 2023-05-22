from random import randrange
from .snake import Snake
from .element import Element
from .infrastructure import Infrastructure
from .constants import *


class Game:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        head = self.get_center_element()
        self.snake = Snake(head)
        self.apple = self.gen_apple()

        self.tick_counter = 0
        self.score = 0
        self.snake_speed_delay = INITIAL_SPEED_DELAY
        self.is_running = True
        self.is_game_over = False

    def gen_random_element(self) -> Element:
        return Element(
            randrange(0, WIDTH),
            randrange(0, HEIGHT),
        )

    def get_center_element(self) -> Element:
        return Element(
            WIDTH // 2,
            HEIGHT // 2,
        )

    def is_field_containts(self, element: Element) -> bool:
        return 0 <= element.x < WIDTH and 0 <= element.y < HEIGHT

    def gen_apple(self) -> Element:
        candidate = None
        while candidate is None:
            candidate = self.gen_random_element()
            if self.snake.contains(candidate):
                candidate = None
        return candidate

    def is_good_head(self, head: Element) -> bool:
        return self.is_field_containts(head) and not self.snake.contains(head)

    def process_events(self) -> None:
        if self.infrastructure.is_quit_event():
            self.is_running = False
        new_direction = self.infrastructure.get_pressed_key()
        if new_direction is not None:
            self.snake.set_direction(new_direction)

    def render(self) -> None:
        self.infrastructure.fill_screen()
        for e in self.snake.snake:
            self.infrastructure.draw_element(e.x, e.y, SNAKE_COLOR)

        self.infrastructure.draw_element(self.apple.x, self.apple.y, APPLE_COLOR)
        self.infrastructure.draw_score(self.score)

        if self.is_game_over:
            self.infrastructure.draw_game_over()

        self.infrastructure.update_and_tick()

    def update_state(self) -> None:
        if self.is_game_over:
            return

        self.tick_counter += 1
        if not self.tick_counter % self.snake_speed_delay:
            new_head = self.snake.get_new_head()
            if self.is_good_head(new_head):
                self.snake.enqueue(new_head)
                if new_head == self.apple:
                    self.score += 1
                    self.apple = self.gen_apple()
                else:
                    self.snake.dequeue()
            else:
                self.is_game_over = True

    def loop(self):
        while self.is_running:
            self.process_events()
            self.update_state()
            self.render()
        self.infrastructure.quit()
