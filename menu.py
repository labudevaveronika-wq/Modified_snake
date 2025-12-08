# game_over_screen.py
import pygame
import time


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()

        self.big_font = pygame.font.SysFont("arial", 60, bold=True)
        self.font = pygame.font.SysFont("arial", 32, bold=True)
        self.button_font = pygame.font.SysFont("arial", 28, bold=True)
        self.small_font = pygame.font.SysFont("arial", 24, bold=True)

        # Цвета
        self.frame_color = (0, 255, 100)
        self.panel_color = (20, 20, 20)
        self.text_yellow = (255, 230, 0)
        self.button_color = (0, 200, 255)

    def draw_button(self, x, y, text, color=None):
        if color is None:
            color = self.button_color

        rect = pygame.Rect(x, y, 120, 120)
        pygame.draw.rect(self.screen, color, rect, border_radius=20)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 4, border_radius=20)

        label = self.button_font.render(text, True, (0, 0, 0))
        lx = x + 60 - label.get_width() // 2
        ly = y + 60 - label.get_height() // 2
        self.screen.blit(label, (lx, ly))

        return rect

    def draw_small_button(self, x, y, text, width=180, height=60):
        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, self.button_color, rect, border_radius=15)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 3, border_radius=15)

        label = self.small_font.render(text, True, (0, 0, 0))
        lx = x + width // 2 - label.get_width() // 2
        ly = y + height // 2 - label.get_height() // 2
        self.screen.blit(label, (lx, ly))

        return rect

    # ЭКРАН ЗАВЕРШЕНИЯ ИГРЫ
    def show_game_over(self, score=0, player_name="Гость", snake_length=0, play_time=0.0):
        clock = pygame.time.Clock()
        panel = pygame.Rect(100, 80, self.width - 200, self.height - 160)

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
                    if b_menu.collidepoint(mx, my):
                        return "menu"
                    if b_exit.collidepoint(mx, my):
                        return "exit"

            self.screen.fill((0, 0, 0))

            # Панель
            pygame.draw.rect(self.screen, self.frame_color, panel, border_radius=25)
            pygame.draw.rect(self.screen, self.panel_color, panel.inflate(-20, -20), border_radius=25)

            # Заголовок
            title = self.big_font.render("GAME OVER", True, (255, 100, 100))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 100))

            # Статистика игры
            stats_y = 200
            stats = [
                f"Player: {player_name}",
                f"Score: {score}",
                f"Snake length: {snake_length}",
                f"Time: {play_time:.1f} sec"
            ]

            for stat in stats:
                text = self.font.render(stat, True, self.text_yellow)
                self.screen.blit(text, (self.width // 2 - text.get_width() // 2, stats_y))
                stats_y += 50

            # Кнопки
            bx = self.width // 2 - 250
            by = 450

            b_retry = self.draw_button(bx, by, "↻")
            b_rating = self.draw_button(bx + 140, by, "🏆", (255, 215, 0))  # золотой
            b_menu = self.draw_button(bx + 280, by, "≡", (100, 255, 100))  # зелёный
            b_exit = self.draw_button(bx + 420, by, "X", (255, 100, 100))  # красный

            # Подписи под кнопками
            labels = ["Play again", "Rating", "Menu", "Exit"]
            label_x = bx - 10
            for i, label in enumerate(labels):
                lbl = self.small_font.render(label, True, (200, 200, 200))
                self.screen.blit(lbl, (label_x + i * 140, by + 140))

            pygame.display.flip()
            clock.tick(60)

    # ЭКРАН ВВОДА ИМЕНИ
    def show_name_input(self):
        clock = pygame.time.Clock()
        input_text = ""
        active = True

        panel = pygame.Rect(100, 150, self.width - 200, 300)

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
                        if len(input_text) < 15 and event.unicode.isprintable():
                            input_text += event.unicode

            self.screen.fill((0, 0, 0))

            # # Панель
            # pygame.draw.rect(self.screen, (0, 150, 255), panel, border_radius=25)
            # pygame.draw.rect(self.screen, self.panel_color, panel.inflate(-20, -20), border_radius=25)

            # Заголовок
            title = self.big_font.render("ENTER YOUR NAME", True, (0, 200, 255))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 180))

            # Поле ввода
            input_rect = pygame.Rect(self.width // 2 - 200, 280, 400, 60)
            pygame.draw.rect(self.screen, (50, 50, 50), input_rect, border_radius=10)
            pygame.draw.rect(self.screen, (0, 200, 255), input_rect, 4, border_radius=10)

            # Текст в поле
            text_surface = self.font.render(input_text if input_text else "Type here...", True,
                                            (255, 255, 255) if input_text else (100, 100, 100))
            self.screen.blit(text_surface, (input_rect.x + 20, input_rect.y + 15))

            # Инструкция
            inst1 = self.small_font.render("Press ENTER to confirm", True, (150, 150, 150))
            inst2 = self.small_font.render("Press ESC to play as Guest", True, (150, 150, 150))
            self.screen.blit(inst1, (self.width // 2 - inst1.get_width() // 2, 380))
            self.screen.blit(inst2, (self.width // 2 - inst2.get_width() // 2, 420))

            pygame.display.flip()
            clock.tick(60)

        return input_text.strip() if input_text.strip() else "Гость"

    # ЭКРАН РЕЙТИНГА
    def show_rating(self, top_players, current_player):
        clock = pygame.time.Clock()
        panel = pygame.Rect(50, 50, self.width - 100, self.height - 100)

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

            # # Панель
            # pygame.draw.rect(self.screen, (255, 215, 0), panel, border_radius=25)
            # pygame.draw.rect(self.screen, self.panel_color, panel.inflate(-20, -20), border_radius=25)

            # Заголовок
            title = self.big_font.render("🏆 LEADERBOARD 🏆", True, (255, 215, 0))
            self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 70))

            # Заголовки таблицы
            headers = ["RANK", "PLAYER", "BEST SCORE", "TOTAL SCORE"]
            x_positions = [100, 250, 450, 600]

            y_pos = 160
            for header, x in zip(headers, x_positions):
                text = self.font.render(header, True, (0, 200, 255))
                self.screen.blit(text, (x, y_pos))

            y_pos = 220

            if top_players:
                for i, player in enumerate(top_players, 1):
                    username = player[0]
                    best_score = player[1]
                    total_score = player[2] if len(player) > 2 else 0

                    # Выделяем текущего игрока
                    if username == current_player:
                        color = (255, 100, 100)  # красный
                        prefix = "> "
                    else:
                        color = (255, 255, 255)  # белый
                        prefix = ""

                    # Ранг
                    rank_text = self.font.render(f"{prefix}{i}", True, color)
                    self.screen.blit(rank_text, (x_positions[0], y_pos))

                    # Имя
                    name_display = username[:12] + "..." if len(username) > 12 else username
                    name_text = self.font.render(f"{prefix}{name_display}", True, color)
                    self.screen.blit(name_text, (x_positions[1], y_pos))

                    # Лучший счёт
                    best_text = self.font.render(f"{prefix}{best_score}", True, color)
                    self.screen.blit(best_text, (x_positions[2], y_pos))

                    # Всего очков
                    total_text = self.font.render(f"{prefix}{total_score}", True, color)
                    self.screen.blit(total_text, (x_positions[3], y_pos))

                    y_pos += 50
            else:
                no_data = self.font.render("No players yet", True, (150, 150, 150))
                self.screen.blit(no_data, (self.width // 2 - no_data.get_width() // 2, 250))

            # Кнопка "Назад"
            back_button = self.draw_small_button(self.width // 2 - 90, self.height - 120, "BACK")

            # Инструкция
            inst = self.small_font.render("Press ESC or click BACK to return", True, (150, 150, 150))
            self.screen.blit(inst, (self.width // 2 - inst.get_width() // 2, self.height - 180))

            pygame.display.flip()
            clock.tick(60)
