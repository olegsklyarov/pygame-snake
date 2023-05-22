from random import randrange
from .element import Element
from .snake import Snake
from .constants import *


def gen_random_element() -> Element:
    """
    Генерирует случайный элмент на игровом поле.
    Используется для позиционирования яблок.
    """
    return Element(randrange(0, WIDTH), randrange(0, HEIGHT))


def get_center_element() -> Element:
    """
    Вычисляет центр игрового поля.

    Используется для начальной позиции змейки.
    """
    return Element(WIDTH // 2, HEIGHT // 2)


def is_field_containts(element: Element) -> bool:
    """
    Проверяет, что элемент находится внутри поля.
    Используется чтобы зафиксировать столкновение змейки с границей экрана.
    """
    return 0 <= element.x < WIDTH and 0 <= element.y < HEIGHT


def is_good_head(head: Element, snake: Snake) -> bool:
    """
    Проверяет, что очередной ход "хороший", то если нет столкновения
    змейки с границей поля или с самой собой.
    """
    return is_field_containts(head) and not snake.is_contains(head)


def gen_apple(snake: Snake) -> Element:
    """
    Вычисляет элемент поля, где будет показано новое яблоко.
    Гарантирует, что яблоко появится вне тела змейки.
    """
    candidate = None
    while candidate is None:
        candidate = gen_random_element()
        if snake.is_contains(candidate):
            candidate = None
    return candidate
