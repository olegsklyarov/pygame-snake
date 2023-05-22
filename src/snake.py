from collections import deque
from .element import Element
from .direction import Direction


class Snake:
    """
    Класс контролирует элементы тела и вектор (направление) движения змейки.
    """

    def __init__(self, head: Element):
        self.snake = deque()
        self.snake.appendleft(head)
        self.direction = Direction.RIGHT

    def is_contains(self, element: Element) -> bool:
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
        raise Exception("")

    def set_direction(self, new_direction) -> None:
        if len(self.snake) == 1 or new_direction.value % 2 != self.direction.value % 2:
            self.direction = new_direction

    def enqueue(self, new_head: Element):
        self.snake.appendleft(new_head)

    def dequeue(self):
        self.snake.pop()
