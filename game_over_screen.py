# game_over_screen.py
import pygame
import time

pygame.init()


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()

        self.big_font = pygame.font.SysFont("arial", 60, bold=True)
        self.font = pygame.font.SysFont("arial", 32, bold=True)

        self.button_font = pygame.font.SysFont("arial", 28, bold=True)

        # Цвета в стиле Geometry Dash
        self.frame_color = (0, 255, 100)
        self.panel_color = (20, 20, 20)
        self.text_yellow = (255, 230, 0)

    def draw_button(self, x, y, text):
        rect = pygame.Rect(x, y, 120, 120)
        pygame.draw.rect(self.screen, (0, 200, 255), rect, border_radius=20)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 4, border_radius=20)

        label = self.button_font.render(text, True, (0, 0, 0))
        lx = x + 60 - label.get_width() // 2
        ly = y + 60 - label.get_height() // 2
        self.screen.blit(label, (lx, ly))

        return rect

    def show(self, score=0, attempts=1, play_time=0.0):
        clock = pygame.time.Clock()

        panel = pygame.Rect(100, 100, self.width - 200, self.height - 200)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    if b_retry.collidepoint(mx, my):
                        return "retry"
                    if b_menu.collidepoint(mx, my):
                        return "menu"
                    if b_exit.collidepoint(mx, my):
                        return "exit"

            self.screen.fill((0, 0, 0))

            # Внешняя рамка в стиле GD
            pygame.draw.rect(self.screen, self.frame_color, panel, border_radius=25)
            pygame.draw.rect(
                self.screen, self.panel_color, panel.inflate(-20, -20), border_radius=25
            )

            # Текст "LEVEL FAILED!"
            title = self.big_font.render("LEVEL FAILED!", True, (255, 255, 255))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 130))

            # Информация
            t1 = self.font.render(f"Score: {score}", True, self.text_yellow)
            t2 = self.font.render(f"Time: {play_time:.2f}", True, self.text_yellow)

            self.screen.blit(t1, (self.width // 2 - t1.get_width() // 2, 300))
            self.screen.blit(t2, (self.width // 2 - t2.get_width() // 2, 350))

            # Три кнопки (как в GD)
            bx = self.width // 2 - 200
            by = 430

            b_retry = self.draw_button(bx, by, "↻")
            b_menu = self.draw_button(bx + 140, by, "≡")
            b_exit = self.draw_button(bx + 280, by, "X")

            pygame.display.flip()
            clock.tick(60)
# game_over_screen.py
import pygame
import time

pygame.init()


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()

        self.big_font = pygame.font.SysFont("arial", 60, bold=True)
        self.font = pygame.font.SysFont("arial", 32, bold=True)

        self.button_font = pygame.font.SysFont("arial", 28, bold=True)

        # Цвета в стиле Geometry Dash
        self.frame_color = (0, 255, 100)
        self.panel_color = (20, 20, 20)
        self.text_yellow = (255, 230, 0)

    def draw_button(self, x, y, text):
        rect = pygame.Rect(x, y, 120, 120)
        pygame.draw.rect(self.screen, (0, 200, 255), rect, border_radius=20)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 4, border_radius=20)

        label = self.button_font.render(text, True, (0, 0, 0))
        lx = x + 60 - label.get_width() // 2
        ly = y + 60 - label.get_height() // 2
        self.screen.blit(label, (lx, ly))

        return rect

    def show(self, score=0, attempts=1, play_time=0.0):
        clock = pygame.time.Clock()

        panel = pygame.Rect(100, 100, self.width - 200, self.height - 200)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    if b_retry.collidepoint(mx, my):
                        return "retry"
                    if b_menu.collidepoint(mx, my):
                        return "menu"
                    if b_exit.collidepoint(mx, my):
                        return "exit"

            self.screen.fill((0, 0, 0))

            # Внешняя рамка в стиле GD
            pygame.draw.rect(self.screen, self.frame_color, panel, border_radius=25)
            pygame.draw.rect(
                self.screen, self.panel_color, panel.inflate(-20, -20), border_radius=25
            )

            # Текст "LEVEL FAILED!"
            title = self.big_font.render("LEVEL FAILED!", True, (255, 255, 255))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 130))

            # Информация
            t2 = self.font.render(f"Score: {score}", True, self.text_yellow)
            t3 = self.font.render(f"Time: {play_time:.2f}", True, self.text_yellow)

            self.screen.blit(t2, (self.width // 2 - t2.get_width() // 2, 300))
            self.screen.blit(t3, (self.width // 2 - t3.get_width() // 2, 350))

            # Три кнопки (как в GD)
            bx = self.width // 2 - 200
            by = 430

            b_retry = self.draw_button(bx, by, "↻")
            b_menu = self.draw_button(bx + 140, by, "≡")
            b_exit = self.draw_button(bx + 280, by, "X")

            pygame.display.flip()
            clock.tick(60)

