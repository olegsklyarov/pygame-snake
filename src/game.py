from .snake import Snake
from .infrastructure import Infrastructure
from .constants import *
from .utils import *


class Game:
    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        head = get_center_element()
        self.snake = Snake(head)
        self.apple = gen_apple(self.snake)

        self.tick_counter = 0
        self.score = 0
        self.snake_speed_delay = INITIAL_SPEED_DELAY
        self.is_running = True
        self.is_game_over = False

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
            head = self.snake.get_new_head()
            if is_good_head(head, self.snake):
                self.snake.enqueue(head)
                if head == self.apple:
                    self.score += 1
                    self.apple = gen_apple(self.snake)
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
