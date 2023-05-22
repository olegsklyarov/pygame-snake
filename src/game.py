import pygame
from .field import Field
from .snake import Snake, Direction
from .element import Element
from .constants import *


class Game:
  def __init__(self) -> None:
    pygame.init()
    self.font =  pygame.font.Font(None, SCALE)
    self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
    self.clock = pygame.time.Clock()

    self.field = Field(WIDTH, HEIGHT)
    self.snake = Snake(self.field)
    self.apple = self.gen_new_apple()

    self.tick_counter = 0
    self.score = 0
    self.snake_speed_delay = 30
    self.is_running = True
    self.is_game_over = False


  def gen_new_apple(self) -> Element:
    candidate = None
    while candidate is None:
      candidate = self.field.gen_random_element()
      if self.snake.contains(candidate):
        candidate = None
    return candidate



  def is_good_head(self, head: Element) -> bool:
    return self.field.contains(head) and not self.snake.contains(head)


  def process_events(self) -> None:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print('quit event')
        self.is_running = False

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
      self.snake.set_direction(Direction.DOWN)
    if key[pygame.K_RIGHT]:
      self.snake.set_direction(Direction.RIGHT)
    if key[pygame.K_DOWN]:
      self.snake.set_direction(Direction.UP)
    if key[pygame.K_LEFT]:
      self.snake.set_direction(Direction.LEFT)


  def render(self) -> None:
    self.screen.fill('black')
    for e in self.snake.snake:
      pygame.draw.rect(self.screen, pygame.Color(SNAKE_COLOR), (e.x * SCALE, e.y * SCALE, SNAKE_SIZE, SNAKE_SIZE), 0, RADIUS)

    pygame.draw.rect(self.screen, pygame.Color(APPLE_COLOR), (self.apple.x * SCALE, self.apple.y * SCALE, SNAKE_SIZE, SNAKE_SIZE), 0, RADIUS)
    self.screen.blit(self.font.render(f'Score: {self.score}', 1, pygame.Color(SCORE_COLOR)), (5, 5))

    if self.is_game_over:
      message = self.font.render('GAME OVER', 1, pygame.Color(GAME_OVER_COLOR))
      self.screen.blit(message, message.get_rect(center=self.field.get_center_tuple(SCALE)))

    pygame.display.update()
    self.clock.tick(FPS)


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
          self.apple = self.gen_new_apple()
        else:
          self.snake.dequeue()
      else:
        self.is_game_over = True


  def loop(self):
    while self.is_running:
      self.process_events()
      self.update_state()
      self.render()
    pygame.quit()
