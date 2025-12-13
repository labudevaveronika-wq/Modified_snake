# portals.py
from random import randint


class Portals:
    """
    Класс для работы с двумя порталами.
    После каждого использования порталы пересоздаются в новых местах.
    """

    def __init__(self, width=20, height=20, obstacles=None, fruits=None, snake_body=None):
        self.width = width
        self.height = height

        # Две точки портала
        self.portal_a = None
        self.portal_b = None

        self.forbidden_positions = []
        if obstacles:
            self.forbidden_positions.extend(obstacle['position'] for obstacle in obstacles)
        if fruits:
            self.forbidden_positions.extend(fruit['position'] for fruit in fruits)
        if snake_body:
            self.forbidden_positions.extend(snake_body)

        self.generate_portals()

    def generate_portals(self):
        """Генерирует две новые разные клетки порталов."""
        while True:
            ax, ay = randint(0, self.width - 1), randint(0, self.height - 1)
            if (ax, ay) not in self.forbidden_positions:
                self.portal_a = (ax, ay)
                break
        while True:
            bx, by = randint(0, self.width - 1), randint(0, self.height - 1)
            self.portal_b = (bx, by)
            if self.portal_b != self.portal_a and self.portal_b not in self.forbidden_positions:
                break

    def check_teleport(self, snake_head):
        """
        Проверяет, наступила ли змейка на портал.
        Если да — возвращает координату выхода.
        Если нет — возвращает None.
        """
        if snake_head == self.portal_a:
            # пересоздаем порталы после использования
            exit_pos = self.portal_b
            self.generate_portals()
            return exit_pos

        if snake_head == self.portal_b:
            exit_pos = self.portal_a
            self.generate_portals()
            return exit_pos

        return None

    def get_portals(self):
        """Возвращает две точки порталов."""
        return self.portal_a, self.portal_b
