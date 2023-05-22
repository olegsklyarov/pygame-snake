from random import randrange
from .element import Element
from .snake import Snake
from .constants import *


def gen_random_element() -> Element:
    return Element(
        randrange(0, WIDTH),
        randrange(0, HEIGHT),
    )


def get_center_element() -> Element:
    return Element(
        WIDTH // 2,
        HEIGHT // 2,
    )


def is_field_containts(element: Element) -> bool:
    return 0 <= element.x < WIDTH and 0 <= element.y < HEIGHT


def is_good_head(head: Element, snake: Snake) -> bool:
    return is_field_containts(head) and not snake.contains(head)


def gen_apple(snake: Snake) -> Element:
    candidate = None
    while candidate is None:
        candidate = gen_random_element()
        if snake.contains(candidate):
            candidate = None
    return candidate
