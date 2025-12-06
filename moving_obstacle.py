# moving_obstacle.py
from random import randint
import time


class MovingObstacle:
    """
    Движущееся препятствие:
    - появляется на одном из краёв поля
    - ждёт 2 секунды
    - движется 5 секунд до противоположного края
    - исчезает и создаётся заново
    - не появляется во фруктах
    """

    def __init__(self, width=15, height=15):
        self.width = width
        self.height = height

        self.position = None
        self.start_position = None
        self.direction = None

        self.phase = "wait"  # wait → move
        self.spawn_time = time.time()
        self.move_start = None

        self.wait_time = 2  # стоим 2 секунды
        self.total_travel_time = 5  # едем 5 секунд

        self.generate([])  # создаём впервые

    # ---------------------------------------------------------
    def generate(self, forbidden_positions):
        """Создаёт препятствие на краю, не заспавнившись во фрукте."""
        while True:
            side = randint(1, 4)

            if side == 1:  # сверху
                pos = (randint(0, self.width - 1), 0)
                direction = (0, +1)

            elif side == 2:  # снизу
                pos = (randint(0, self.width - 1), self.height - 1)
                direction = (0, -1)

            elif side == 3:  # слева
                pos = (0, randint(0, self.height - 1))
                direction = (+1, 0)

            else:  # справа
                pos = (self.width - 1, randint(0, self.height - 1))
                direction = (-1, 0)

            if pos not in forbidden_positions:
                break

        self.position = pos
        self.start_position = pos
        self.direction = direction

        self.phase = "wait"
        self.spawn_time = time.time()
        self.move_start = None

    # ---------------------------------------------------------
    def update(self, forbidden_positions):
        """Управляет фазами движения препятствия."""
        now = time.time()

        # ---- Фаза ожидания ----
        if self.phase == "wait":
            if now - self.spawn_time >= self.wait_time:
                self.phase = "move"
                self.move_start = now
            return

        # ---- Фаза движения ----
        if self.phase == "move":
            elapsed = now - self.move_start

            if elapsed >= self.total_travel_time:
                # закончил движение → пересоздаём
                self.generate(forbidden_positions)
                return

            # вычисляем дистанцию от старта
            px, py = self.start_position
            dx, dy = self.direction

            if dx != 0:
                distance = self.width - 1
            else:
                distance = self.height - 1

            # доля пути (0..1)
            t = elapsed / self.total_travel_time
            t = max(0, min(1, t))

            shift = int(distance * t)

            self.position = (px + dx * shift, py + dy * shift)

    # ---------------------------------------------------------
    def get_position(self):
        """Возвращает целочисленную координату."""
        if self.position is None:
            return None
        return (int(self.position[0]), int(self.position[1]))
