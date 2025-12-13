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




def main_menu(screen=None):
    """Отображает меню и запускает выбранный уровень."""
    if screen is None:
        screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Snake — выбор уровня")


    while True:
        screen.fill((0, 0, 0))
        screen.blit(BIG.render("ВЫБЕРИТЕ УРОВЕНЬ", True, (255, 255, 0)), (160, 100))

        draw_text("1 — Уровень 1: еда + статичные препятствия", (100, 200))
        draw_text("2 — Уровень 2: + порталы", (100, 260))
        draw_text("3 — Уровень 3: + движущееся препятствие (3 жизни)", (100, 320))
        draw_text("Нажмите 1, 2 или 3 для выбора", (100, 400))
        draw_text("Esc — отмена", (100, 440))

        pygame.display.flip()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_2:
                    return 2
                if event.key == pygame.K_3:
                     return 3
def show_level_selection(screen):
    """Показать экран выбора уровня и вернуть выбранный уровень"""
    return main_menu(screen)


# if __name__ == "__main__":
#     main_menu()

