from collections import deque
from enum import Enum

from .field import Field
from .element import Element

class Direction(Enum):
  UP = 1
  RIGHT = 2
  DOWN = 3
  LEFT = 4


class Snake:
  def __init__(self, field: Field):
    self.field = field
    self.snake = deque()
    self.snake.appendleft(field.get_center_element())
    self.direction = Direction.RIGHT

  def contains(self, element: Element) -> bool:
    try:
      self.snake.index(element)
      return True
    except ValueError:
      return False

  def get_new_head(self) -> Element:
    head = self.snake[0]
    if self.direction == Direction.UP:
      return Element(head.x, head.y + 1)
    if self.direction == Direction.RIGHT:
      return Element(head.x + 1, head.y)
    if self.direction == Direction.DOWN:
      return Element(head.x, head.y - 1)
    if self.direction == Direction.LEFT:
      return Element(head.x - 1, head.y)

  def set_direction(self, new_direction) -> None:
    if len(self.snake) == 1 or new_direction.value % 2 != self.direction.value % 2:
      self.direction = new_direction

  def enqueue(self, new_head: Element):
    self.snake.appendleft(new_head)

  def dequeue(self):
    self.snake.pop()
