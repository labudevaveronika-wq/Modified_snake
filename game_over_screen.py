# game_over_screen.py
import pygame
import time

pygame.init()


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = 800, 800

        self.big_font = pygame.font.SysFont("arial", 60, bold=True)
        self.font = pygame.font.SysFont("arial", 32, bold=True)
        self.button_font = pygame.font.SysFont("arial", 28, bold=True)
        self.button_font = pygame.font.SysFont("arial", 28, bold=True)
        self.small_font = pygame.font.SysFont("arial", 24, bold=True)

        # Цвета в стиле Geometry Dash
        self.frame_color = (0, 255, 100)
        self.panel_color = (20, 20, 20)
        self.text_yellow = (255, 230, 0)

        self.button_color = (0, 200, 255)

    def draw_button(self, x, y, text, color=None):
        if color is None:
            color = self.button_color
        rect = pygame.Rect(x, y, 120, 120)
        pygame.draw.rect(self.screen, (0, 200, 255), rect, border_radius=20)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 4, border_radius=20)

        label = self.button_font.render(text, True, (0, 0, 0))
        lx = x + 60 - label.get_width() // 2
        ly = y + 60 - label.get_height() // 2
        self.screen.blit(label, (lx, ly))

        return rect

    def draw_small_button(self, x, y, text, width=180, height=60):
        """Отрисовка маленькой прямоугольной кнопки"""

        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, self.button_color, rect, border_radius=15)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 3, border_radius=15)

        label = self.small_font.render(text, True, (0, 0, 0))
        lx = x + width // 2 - label.get_width() // 2
        ly = y + height // 2 - label.get_height() // 2
        self.screen.blit(label, (lx, ly))

        return rect




    def show_name_input(self):
        """Показать экран ввода имени игрока"""
        clock = pygame.time.Clock()
        input_text = ""
        active = True

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        return "Гость"
                    else:
                        if len(input_text) < 20 and event.unicode.isprintable():
                            input_text += event.unicode

            self.screen.fill((0, 0, 0))

            # Заголовок
            title = self.big_font.render(" ВВЕДИТЕ ВАШЕ ИМЯ ", True, (0, 255, 127) )
            title_1 = self.big_font.render(" (не более 6ти симвлов) ", True, (0, 255, 127))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 120))
            self.screen.blit(title_1, (self.width // 2 - title_1.get_width() // 2, 180))

            # Поле ввода
            input_rect = pygame.Rect(self.width // 2 - 200, 280, 400, 60)
            pygame.draw.rect(self.screen, (0, 0, 0), input_rect)
            pygame.draw.rect(self.screen, (0, 200, 255), input_rect, 4)

            # Текст в поле
            text_surface = self.font.render(input_text if input_text else "Печайтате здесь...", True, (0, 0, 0) if input_text else (100, 100, 100))
            self.screen.blit(text_surface, (input_rect.x + 20, input_rect.y + 15))


            pygame.display.flip()
            clock.tick(60)

        return input_text.strip() if input_text.strip() else "Гость"















    def show_game_over(self, score=0, player_name="Гость", snake_length=0, play_time=0.0):
        """Показать экран завершения игры с кнопками"""
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()

                    if b_retry.collidepoint(mx, my):
                        return "retry"
                    if b_rating.collidepoint(mx, my):
                        return "rating"
                    if b_exit.collidepoint(mx, my):
                        return "exit"

            self.screen.fill((0, 0, 0))

            # Заголовок
            title = self.big_font.render("...RIP...", True, (100, 100, 100))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 80))

            # Статистика игры
            stats_y = 180
            stats = [
                f"Игрок: {player_name}",
                f"Счет: {score}",
                f"Длина змеи: {snake_length}",
                f"Время: {play_time:.1f} sec"
            ]

            for stat in stats:
                text = self.font.render(stat, True, self.text_yellow)
                self.screen.blit(text, (self.width // 2 - text.get_width() // 2, stats_y))
                stats_y += 50

            # Кнопки - ПО ЦЕНТРУ БЕЗ ПОДПИСЕЙ
            b_retry = self.draw_button(200, 450, "AGAIN", (255, 215, 100))
            b_rating = self.draw_button(340, 450, "TOP", (255, 215, 100))
            b_exit = self.draw_button(480, 450, "EXIT", (255, 100, 100))

            pygame.display.flip()
            clock.tick(60)


    def show_rating(self, top_players, current_player):
        """Показать таблицу рейтинга"""
        clock = pygame.time.Clock()
        rating_font = pygame.font.SysFont("arial", 24, bold=True)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "back"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if back_button.collidepoint(mx, my):
                        return "back"

            self.screen.fill((0, 0, 0))

            # Заголовок
            title = self.big_font.render("РЕЙТИНГ", True, (255, 215, 0))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 70))

            # Заголовки таблицы
            headers = ["МЕСТО", "ИГРОК", "РЕКОРД", "ВСЕГО ОЧКОВ", "ВРЕМЯ"]
            x_positions = [50, 200, 350, 500, 690]

            y_pos = 160
            for header, x in zip(headers, x_positions):
                text = rating_font.render(header, True, (0, 200, 255))
                self.screen.blit(text, (x, y_pos))

            y_pos = 220

            if top_players:
                for i, player in enumerate(top_players, 1):
                    username = player[0]
                    best_score = player[1]
                    total_score = player[2]
                    total_time = player[3]

                    # Выделяем текущего игрока
                    if username == current_player:
                        color = (255, 100, 100)  # красный
                        prefix = "> "
                    else:
                        color = (255, 255, 255)  # белый
                        prefix = ""

                    # Ранг
                    rank_text = rating_font.render(f"{prefix}{i}", True, color)
                    self.screen.blit(rank_text, (x_positions[0], y_pos))

                    # Имя
                    name_display = username[:12] + "..." if len(username) > 12 else username
                    name_text = rating_font.render(f"{prefix}{name_display}", True, color)
                    self.screen.blit(name_text, (x_positions[1], y_pos))

                    # Лучший счёт
                    best_text = rating_font.render(f"{prefix}{best_score}", True, color)
                    self.screen.blit(best_text, (x_positions[2], y_pos))

                    # Всего очков
                    total_text = rating_font.render(f"{prefix}{total_score}", True, color)
                    self.screen.blit(total_text, (x_positions[3], y_pos))

                    time_text = rating_font.render(f"{prefix}{total_time}с", True, color)
                    self.screen.blit(time_text, (x_positions[4], y_pos))

                    y_pos += 50
            else:
                no_data = rating_font.render("Игроков еще нет..", True, (150, 150, 150))
                self.screen.blit(no_data, (self.width // 2 - no_data.get_width() // 2, 250))

            # Кнопка "Назад"
            back_button = self.draw_small_button(self.width // 2 - 90, 720, "BACK")

            pygame.display.flip()
            clock.tick(60)

    def show(self, score=0, attempts=1, play_time=0.0):
        """Старой версии для совместимости (использует новую версию)"""
        return self.show_game_over(
            score=score,
            player_name="Гость",
            snake_length=attempts,
            play_time=play_time
        )





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
# # game_over_screen.py
# import pygame
# import time
#
# pygame.init()


# class GameOverScreen:
#     def __init__(self, screen):
#         self.screen = screen
#         self.width, self.height = screen.get_size()
#
#         self.big_font = pygame.font.SysFont("arial", 60, bold=True)
#         self.font = pygame.font.SysFont("arial", 32, bold=True)
#
#         self.button_font = pygame.font.SysFont("arial", 28, bold=True)
#
#         # Цвета в стиле Geometry Dash
#         self.frame_color = (0, 255, 100)
#         self.panel_color = (20, 20, 20)
#         self.text_yellow = (255, 230, 0)
#
#     def draw_button(self, x, y, text):
#         rect = pygame.Rect(x, y, 120, 120)
#         pygame.draw.rect(self.screen, (0, 200, 255), rect, border_radius=20)
#         pygame.draw.rect(self.screen, (255, 255, 255), rect, 4, border_radius=20)
#
#         label = self.button_font.render(text, True, (0, 0, 0))
#         lx = x + 60 - label.get_width() // 2
#         ly = y + 60 - label.get_height() // 2
#         self.screen.blit(label, (lx, ly))
#
#         return rect
#
#     def show(self, score=0, attempts=1, play_time=0.0):
#         clock = pygame.time.Clock()
#
#         panel = pygame.Rect(100, 100, self.width - 200, self.height - 200)
#
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     return "exit"
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     mx, my = pygame.mouse.get_pos()
#
#                     if b_retry.collidepoint(mx, my):
#                         return "retry"
#                     if b_menu.collidepoint(mx, my):
#                         return "menu"
#                     if b_exit.collidepoint(mx, my):
#                         return "exit"
#
#             self.screen.fill((0, 0, 0))
#
#             # Внешняя рамка в стиле GD
#             pygame.draw.rect(self.screen, self.frame_color, panel, border_radius=25)
#             pygame.draw.rect(
#                 self.screen, self.panel_color, panel.inflate(-20, -20), border_radius=25
#             )
#
#             # Текст "LEVEL FAILED!"
#             title = self.big_font.render("LEVEL FAILED!", True, (255, 255, 255))
#             self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 130))
#
#             # Информация
#             t2 = self.font.render(f"Score: {score}", True, self.text_yellow)
#             t3 = self.font.render(f"Time: {play_time:.2f}", True, self.text_yellow)
#
#             self.screen.blit(t2, (self.width // 2 - t2.get_width() // 2, 300))
#             self.screen.blit(t3, (self.width // 2 - t3.get_width() // 2, 350))
#
#             # Три кнопки (как в GD)
#             bx = self.width // 2 - 200
#             by = 430
#
#             b_retry = self.draw_button(bx, by, "↻")
#             b_menu = self.draw_button(bx + 140, by, "≡")
#             b_exit = self.draw_button(bx + 280, by, "X")
#
#             pygame.display.flip()
#             clock.tick(60)
#
