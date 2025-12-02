# moving_obstacle.py
from random import randint
import time


class MovingObstacle:
    """
    Движущееся препятствие.
    Появляется на одной из граней карты и движется внутрь поля.
    Движется 1 клетку каждые 10 секунд.
    Когда достигает противоположной границы — исчезает.
    """

    def __init__(self, width=15, height=15):
        self.width = width
        self.height = height

        self.position = None
        self.direction = None
        self.last_move_time = time.time()

        self.generate()

    # ------------------------------------------------------
    # Генерация препятствия
    # ------------------------------------------------------
    def generate(self):
        """Создаёт препятствие на одном из краёв карты."""

        side = randint(1, 4)

        if side == 1:  # сверху (y = 0)
            self.position = (randint(0, self.width - 1), 0)
            self.direction = (0, +1)  # вниз

        elif side == 2:  # снизу (y = height-1)
            self.position = (randint(0, self.width - 1), self.height - 1)
            self.direction = (0, -1)  # вверх

        elif side == 3:  # слева (x = 0)
            self.position = (0, randint(0, self.height - 1))
            self.direction = (+1, 0)  # вправо

        elif side == 4:  # справа (x = width-1)
            self.position = (self.width - 1, randint(0, self.height - 1))
            self.direction = (-1, 0)  # влево

        self.last_move_time = time.time()

    # ------------------------------------------------------
    # Логика движения
    # ------------------------------------------------------
    def update(self):
        """Каждые 10 секунд двигает препятствие на 1 клетку."""

        if time.time() - self.last_move_time < 10:
            return  # ещё не пора двигаться

        self.last_move_time = time.time()

        x, y = self.position
        dx, dy = self.direction

        new_x = x + dx
        new_y = y + dy

        # Если выходит за границу — препятствие исчезает и пересоздаётся.
        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            self.generate()
            return

        self.position = (new_x, new_y)

    # ------------------------------------------------------
    def get_position(self):
        return self.position
