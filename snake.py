import pygame


def main():
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print('quit event')
        running = False
    screen.fill('purple')
    pygame.display.flip()
    clock.tick(60)
  pygame.quit()


if __name__ == '__main__':
  main()
