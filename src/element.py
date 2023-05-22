class Element:
    """
    Элемент (точка) игрового поля

    Args:
        x, y - координаты элемента внутри игрового поля
        0 <= x < WIDTH
        0 <= y < HEIGHT
    """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, o) -> bool:
        """
        Проверка на совпадение двух элементов поля

        Используется для проверки, что змейка съела яблоко
        """
        return self.x == o.x and self.y == o.y
