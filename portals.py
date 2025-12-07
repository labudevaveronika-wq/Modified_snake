# portals.py
from random import randint


class Portals:
    """
    Класс для работы с двумя порталами.
    После каждого использования порталы пересоздаются в новых местах.
    """

    def __init__(self,obstacles=None, width=15, height=15):
        self.width = width
        self.height = height

        self.obstacles=obstacles
        # Две точки портала
        self.portal_a = None
        self.portal_b = None

        self.generate_portals()

    def generate_portals(self):
        """Генерирует две новые разные клетки порталов."""
        ax = randint(0, self.width - 1)
        ay = randint(0, self.height - 1)
        while (ax, ay) in self.obstacles:
            ax = randint(0, self.width - 1)
            ay = randint(0, self.height - 1)
        bx = randint(0, self.width - 1)
        by = randint(0, self.height - 1)

        # Порталы не должны совпадать
        while (bx == ax and by == ay) or (bx, by) in self.obstacles:
            bx = randint(0, self.width - 1)
            by = randint(0, self.height - 1)

        self.portal_a = (ax, ay)
        self.portal_b = (bx, by)

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
