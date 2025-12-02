"""
level_interface.py

Интерфейс уровней. Этот файл реализует основное меню, которое появляется
при запуске game.py. После выбора уровня создаётся объект Game(level_num)
и запускается игровая логика.

Уровни:
1 — еда и статичные препятствия (1 жизнь)
2 — еда, статичные препятствия и порталы (1 жизнь)
3 — еда и движущееся препятствие (3 жизни)
"""

import pygame

pygame.init()
SCREEN = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Snake — выбор уровня")
FONT = pygame.font.SysFont("arial", 28)
BIG = pygame.font.SysFont("arial", 38)


def draw_text(text, pos, color=(255, 255, 255)):
    SCREEN.blit(FONT.render(text, True, color), pos)


def draw_menu():
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BIG.render("ВЫБЕРИТЕ УРОВЕНЬ", True, (255, 255, 0)), (160, 100))

    draw_text("1 — Уровень 1: еда + статичные препятствия", (100, 200))
    draw_text("2 — Уровень 2: + порталы", (100, 260))
    draw_text("3 — Уровень 3: + движущееся препятствие (3 жизни)", (100, 320))

    draw_text("Esc — выйти", (100, 420))
    pygame.display.flip()


def main_menu():
    """Отображает меню и запускает выбранный уровень."""
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                    from game import (
                        Game,
                    )  # ← ленивый импорт (исправляет циклический импорт)
                if event.key == pygame.K_1:
                    game = Game(level_num=1)
                    game.run()
                if event.key == pygame.K_2:
                    game = Game(level_num=2)
                    game.run()
                if event.key == pygame.K_3:
                    game = Game(level_num=3)
                    game.run()


if __name__ == "__main__":
    main_menu()

