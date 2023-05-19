import pygame
from .field import Field
from .snake import Snake, Direction
from .element import Element

SCALE = 40
RADIUS = 5
SNAKE_SIZE = 38
SNAKE_COLOR = 'yellow'
APPLE_COLOR = 'red'
ROWS = 10
COLS = 20


def gen_new_apple(field: Field, snake: Snake) -> Element:
  apple = None
  while apple is None:
    candidate = field.gen_random_element()
    if not snake.contains(candidate):
      apple = candidate
  return apple
  


def main():
  field = Field(ROWS, COLS)
  snake = Snake(field)

  pygame.init()
  screen = pygame.display.set_mode([ROWS * SCALE, COLS * SCALE])
  clock = pygame.time.Clock()
  counter = 0
  snake_speed_limit = 40
  score = 0
  apple = gen_new_apple(field, snake)
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print('quit event')
        running = False

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
      snake.set_direction(Direction.DOWN)
    if key[pygame.K_RIGHT]:
      snake.set_direction(Direction.RIGHT)
    if key[pygame.K_DOWN]:
      snake.set_direction(Direction.UP)
    if key[pygame.K_LEFT]:
      snake.set_direction(Direction.LEFT)

    screen.fill('black')

    for e in snake.snake:
      pygame.draw.rect(screen, pygame.Color(SNAKE_COLOR), (e.x * SCALE, e.y * SCALE, SNAKE_SIZE, SNAKE_SIZE), 0, RADIUS)

    pygame.draw.rect(screen, pygame.Color(APPLE_COLOR), (apple.x * SCALE, apple.y * SCALE, SNAKE_SIZE, SNAKE_SIZE), 0, RADIUS)
    
    pygame.display.flip()
    clock.tick(60)
    counter += 1
    if not counter % snake_speed_limit:
      new_head = snake.get_new_head()
      if snake.contains(new_head):
        print('Snake colliding, game over')
        running = False
      if not field.contains(new_head):
        print('Wall colliging, game over')
        running = False
      snake.enqueue(new_head)
      if new_head == apple:
        score += 1
        print('Score: {}'.format(score))
        apple = gen_new_apple(field, snake)
      else:
        snake.dequeue()

  pygame.quit()
