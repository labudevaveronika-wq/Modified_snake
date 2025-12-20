from food import Food
from obstacle import Obstacle
from sanke import Snake
import time
import pygame
from portals import Portals
from moving_obstacle import MovingObstacle
from game_over_screen import GameOverScreen
from snake_database import SnakeDatabase
from level_interface import main_menu

# Инициализирует все игровые объекты
# Управляет игровым циклом
# Координирует взаимодействие между всеми компонентами
# Обрабатывает ввод пользователя
# Отображает всё на экране
class Game:
    def __init__(self, level_num=1, play_name="Гость"):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 840))
        pygame.display.set_caption("Snake")

        self.panel_font = pygame.font.SysFont(None, 28)

        self.panel_color = (30, 30, 30)  # Темно-серый цвет
        self.panel_text_color = (220, 220, 220)  # Светло-серый текст

        self.grid_size = 20  # 20x20 клеток
        self.cell_size = 40
        self.panel_height = 80

        self.offset_x = 0
        self.offset_y = 0

        self.player_name = play_name

        self.level = level_num

        self.snake = Snake()

        self.obstacles = Obstacle(15, self.snake.position)
        self.food = Food(10, self.obstacles.obstacles)

        self.key_history = []
        self.flag_cheat = False

        if self.level == 3:
            self.lives = 3
            self.moving_obstacle = MovingObstacle()

            fruit_positions = [f["position"] for f in self.food.get_all_fruits()]
            obstacle_positions = [o["position"] for o in self.obstacles.get_all_obstacles()]
            forbidden = fruit_positions + obstacle_positions
            self.moving_obstacle.generate(fruit_positions)
            self.moving_obstacle.generate(forbidden)
        else:
            self.lives = 1


        if self.level == 2:
            self.portals = Portals(
            width=self.grid_size,  # 20
            height=self.grid_size,  # 20
            obstacles=self.obstacles.get_all_obstacles(),
            fruits=self.food.get_all_fruits(),
            snake_body=self.snake.position
            )

        self.score = 0  # счётзмейка

        self.life = True  # жива ли
        # self.score = 0  # текущий счёт
        self.start_time = 0  # время начала игры
        # self.player_name = "Гость"  # имя игрока
        self.is_game_over = False  # флаг завершения игры
        self.play_time = 0  # время игры в секундах

        self.db = SnakeDatabase()

        self.game_over_screen = GameOverScreen(self.screen)

#        self.panel_font = pygame.font.SysFont(None, 28)

    def run(self):
        '''Таким образом в run только вызов методов'''
        clock = pygame.time.Clock()
        self.start_time = time.time()


        if self.player_name == "Гость":
            name = self.game_over_screen.show_name_input()
            if name:
                self.player_name = name
                if self.player_name=="veronika dasha andre":
                    self.flag_cheat=True
                    self.snake.flag_cheat=True
                    self.snake.flag_acceleration = True
                    self.snake.acceleration_end_time = time.time() + 1000000000
                if self.player_name != "Гость":
                    self.db.add_player(self.player_name)
            else:
                pygame.quit()
                return

        selected_level = self.choose_level()
        if selected_level:
            # Обновляем уровень и пересоздаем игровые объекты
            self.level = selected_level
            self.reinitialize_with_level(selected_level)
        else:
            return


        while self.life:
            self.events()
            self.snake.simple_move()
            self.update()
            self.draw()

            if self.snake.flag_acceleration:
                clock.tick(10)
            else:
                clock.tick(5)


        self.play_time = int(time.time() - self.start_time)

        if self.player_name != "Гость":
            success = self.db.save_game_result(self.player_name, self.score, self.play_time)

        while True:
            action = self.game_over_screen.show_game_over(
                score=self.score,
                player_name=self.player_name,
                snake_length=len(self.snake.position),
                play_time=self.play_time
            )

            if action == "retry":
                return Game(self.level, self.player_name).run()
            if action == "rating":
                top_players = self.db.get_top_players(10)

                rating_action = self.game_over_screen.show_rating(top_players, self.player_name)

                if rating_action == "back":
                    continue
                else:
                    action = rating_action
                    if action == "exit":
                        pygame.quit()
                        exit()
                    elif action == "menu":
#                        from level_interface import main_menu
                        return main_menu()
                    continue

            if action == "exit":
                pygame.quit()
                exit()
            return None

    def show_main_menu(self):
        """Показать главное меню"""
        from level_interface import main_menu
        return main_menu()

    def choose_level(self):
        """Показать экран выбора уровня"""
        from level_interface import show_level_selection

        # Нужно создать функцию show_level_selection в level_interface.py
        return show_level_selection(self.screen)

    def reinitialize_with_level(self, level_num):
        """Переинициализировать игру с новым уровнем"""
        # Обновляем уровень
        self.level = level_num

        # Обновляем жизни
        if self.level == 3:
            self.lives = 3
        else:
            self.lives = 1

        # Обновляем порталы
        if self.level == 2:
            self.portals = Portals()
        else:
            self.portals = None

        # Обновляем движущееся препятствие
        if self.level == 3:
            from moving_obstacle import MovingObstacle
            self.moving_obstacle = MovingObstacle()
            fruit_positions = [f["position"] for f in self.food.get_all_fruits()]
            obstacle_positions = [o["position"] for o in self.obstacles.get_all_obstacles()]
            forbidden = fruit_positions + obstacle_positions
            self.moving_obstacle.generate(forbidden)
        else:
            self.moving_obstacle = None



    def events(self):  # проверять все от клавиш до эффектов
        """Проверять все события pygame
        Если событие "закрытие окна" - останавливать игру
        Если нажата клавиша - определять какая именно
        Если нажаты стрелки - менять направление змейки"""
        for (event) in (pygame.event.get()):  # проыерить событие: что именно случилось, кнопка или закрытие окна
            if event.type == pygame.QUIT:  # если нажат крестик для закрытия окна
                self.life = False
            # добавляю управление змеей с помощью кнопок - стрелок
            # проверка на нажатие стрелок
            if event.type == pygame.KEYDOWN:
                # print(f"Нажата клавиша: {event.key}")
                if event.key == pygame.K_DOWN:  # вниз
                    self.snake.moving((0, +1))
                elif event.key == pygame.K_UP:  # вверх
                    self.snake.moving((0, -1))
                elif event.key == pygame.K_LEFT:  # влево
                    self.snake.moving((-1, 0))
                elif event.key == pygame.K_RIGHT:  # вправо
                    self.snake.moving((1, 0))


                elif event.key == pygame.K_q:
                    # print("Q нажата! Очищаю базу...")
                    self.db.clear_db()
                self.handle_cheats(event.key)
            # надо добавить проверку на то, что змея съедает фрукт
    def handle_cheats(self, key):
        self.key_history.append(key)
        if len(self.key_history) > 5:
            self.key_history.pop(0)
        if self.key_history == [100, 114, 101, 97, 109]:
            self.flag_cheat = True
            self.snake.flag_cheat = True

            self.key_history = []

    def update(self):
        '''Двигать змейку вперед
        Проверять столкновение змейки с едой
        Проверять столкновение змейки с собой или границами
        Если змейка съела еду - увеличивать счет и создавать новую еду'''
        self.snake.update_boost()
        # проверка на столкновение с любым фруктом
        fruits = self.food.get_all_fruits()
        for i, fruit in enumerate(fruits):
            if self.snake.head == fruit["position"]:
                food_type = fruit["type"]
                self.snake.eat(food_type)
                self.food.spawn(i) # замена того фрукта, который съели и добавили новый
                if food_type == 'apple':
                    self.score += 10
                elif food_type == 'pear':
                    self.score += 5
                elif food_type == 'grape':
                    self.score += 15
                self.food.spawn(
                    i, self.obstacles.obstacles
                )  # замена того фрукта, который съели и добавили новый


                self.snake.evolution_score += 1
                if self.snake.evolution_score >= 10:  # каждые 10 очков
                    self.snake.evolve()
                    self.snake.evolution_score = 0  # сбрасываем счетчик
                break


        if not self.snake.state(self.obstacles.get_all_obstacles()):
            self.life = False

        # Проверка телепортации (для уровня 2)
        if self.level == 2 and self.portals is not None:
            teleport_to = self.portals.check_teleport(self.snake.head)
            if teleport_to:
                self.snake.head = teleport_to
                self.snake.position[0] = teleport_to

    def draw_panel(self):
        panel_rect = pygame.Rect(0, 0, 800, 80)
        pygame.draw.rect(self.screen, self.panel_color, panel_rect)

        current_time = int(time.time() - self.start_time)

        hours = current_time // 3600
        minutes = (current_time % 3600) // 60
        seconds = current_time % 60
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        name_text = self.panel_font.render(f"Игрок: {self.player_name}", True, self.panel_text_color)
        score_text = self.panel_font.render(f"Счет: {self.score}", True, self.panel_text_color)
        time_text = self.panel_font.render(f"Время: {time_str}", True, self.panel_text_color)

        self.screen.blit(name_text, (20, 45 - name_text.get_height() // 2))

        # Центр - счет
        self.screen.blit(score_text, (
            self.screen.get_width() // 2 - score_text.get_width() // 2,
            45 - score_text.get_height() // 2
        ))

        # Правая часть - время
        self.screen.blit(time_text, (
            self.screen.get_width() - time_text.get_width() - 20,
            45 - time_text.get_height() // 2
        ))
    def draw(self):
        '''Залить экран черным цветом
        Нарисовать змейку (по координатам из snake.position)
        Нарисовать еду (по координатам из food.position)
        Отобразить счет игрока на экране'''

        self.screen.fill(pygame.Color('black')) # залили экран черным
        background_image = pygame.image.load("background.png").convert_alpha() #задний фон
        background_image = pygame.transform.scale(background_image, (self.cell_size*20, self.cell_size*25))
        self.screen.blit(background_image, (0, 0))
        filter_surface = pygame.Surface(background_image.get_size())
        filter_surface.fill((0, 0, 0))  # Синий цвет
        filter_surface.set_alpha(200)  # Прозрачность (0-255)
        self.screen.blit(filter_surface, (0, 0))  # Затем накладываем фильтр




        self.draw_panel()

        # отрисовка препятствий
        for obstacle in self.obstacles.get_all_obstacles():
            image = pygame.image.load("obstacle.png").convert_alpha()
            new_image = pygame.transform.scale(image, (self.cell_size, self.cell_size))
            new_image.set_colorkey((0, 0, 0))
            self.screen.blit(
                new_image, (obstacle["position"][0] * self.cell_size + self.offset_x,
             obstacle["position"][1] * self.cell_size + self.offset_y + 80)
        )

        for fruit in self.food.get_all_fruits():
            if fruit["color"] == "red":
                image = pygame.image.load("apple.png").convert_alpha()
            elif fruit["color"] == "green":
                image = pygame.image.load("pear.png").convert_alpha()
            else:
                image = pygame.image.load("grape.png").convert_alpha()
            new_image = pygame.transform.scale(image, (self.cell_size, self.cell_size))
            new_image.set_colorkey((0, 0, 0))
            self.screen.blit(
            new_image,
            (fruit["position"][0] * self.cell_size + self.offset_x,
             fruit["position"][1] * self.cell_size + self.offset_y+80)
        )

        if self.level == 3 and self.moving_obstacle is not None:
            ox, oy = self.moving_obstacle.get_position()
            image_moving=pygame.image.load("moving_obstacle.png").convert_alpha()
            image_moving = pygame.transform.scale(image_moving, (self.cell_size, self.cell_size))
            #image_moving.set_colorkey((255,255,255))
            rect = pygame.Rect(
            ox * self.cell_size + self.offset_x,
            oy * self.cell_size + self.offset_y + 80,
            self.cell_size,
            self.cell_size
            )
            self.screen.blit(image_moving, rect)


        snake_image = pygame.image.load("snake.png").convert_alpha()
        snake_image = pygame.transform.scale(snake_image, (self.cell_size, self.cell_size))
        snake_image_head = pygame.image.load("snake_head.png").convert_alpha()
        snake_image_head = pygame.transform.scale(snake_image_head, (self.cell_size, self.cell_size))
        portal_image = pygame.image.load("portal.png").convert_alpha()
        portal_image =pygame.transform.scale(portal_image,(self.cell_size,self.cell_size))

        for position in self.snake.position:
            # Выбираем цвет в зависимости от состояния
            if self.snake.flag_acceleration:
                # Ярче при ускорении
                color = (
                    min(255, self.snake.snake_color[0] + 50),
                    min(255, self.snake.snake_color[1] + 50),
                    min(255, self.snake.snake_color[2] + 50)
                )
            else:
                # Обычный цвет эволюции
                color = self.snake.snake_color

            # Рисуем клетку змейки
            square = pygame.Rect(
                position[0] * self.cell_size + self.offset_x,
                position[1] * self.cell_size + self.offset_y + 80,
                self.cell_size,
                self.cell_size
            )

            if position==self.snake.head:
                snake_image_head.set_colorkey((0, 0, 0))
                if self.snake.direction==(1,0):
                    snake_image_head=pygame.transform.rotate(snake_image_head,270)
                if self.snake.direction==(-1,0):
                    snake_image_head=pygame.transform.rotate(snake_image_head,90)
                if self.snake.direction==(0,1):
                    snake_image_head=pygame.transform.rotate(snake_image_head,180)
                self.screen.blit(snake_image_head, square)
            else: # задний фон
                self.screen.blit(snake_image, square)
                snake_filter_surface = pygame.Surface(background_image.get_size())
                snake_filter_surface.fill(color)  # цвет змеи
                snake_filter_surface.set_alpha(100)  # Прозрачность (0-255)
                self.screen.blit(snake_filter_surface, square,(40,40,40,40)) # отрисовка фильтра

            if self.level == 2 and self.portals is not None:
                pa, pb = self.portals.get_portals()
                square_pa=pygame.Rect(
                    pa[0] * self.cell_size + self.offset_x,
                    pa[1] * self.cell_size + self.offset_y + 80,
                    self.cell_size,
                    self.cell_size
                )
                self.screen.blit(portal_image, square_pa)
                square_pb = pygame.Rect(
                    pb[0] * self.cell_size + self.offset_x,
                    pb[1] * self.cell_size + self.offset_y + 80,
                    self.cell_size,
                    self.cell_size
                )
                self.screen.blit(portal_image, square_pb)


            pygame.display.flip()  # тут обновляем экарн



# Проверка что все создалось
# game = Game()
# print("Окно создано!")
# print("Змейка создана:", game.snake)
# print("Еда создана:", game.food)
# print("Счет:", game.score)

# тест отрисовки
game = Game()
game.run()
# поначалу вот такой вывод для этого теста:
# pygame 2.6.1 (SDL 2.28.4, Python 3.13.7)
# Hello from the pygame community. https://www.pygame.org/contribute.html
# так просихдит потому что окно появляется и исчезает, так как программа сразу завершается
# это по идее можно исправить с помощью изменения метода run
# Получилось, появляется черное окно и висит до закрытия
# новый тест
# print("Змейка:", game.snake.position)
# print("Еда:", game.food.position)


# if __name__ == "__main__":
#     main_menu()

# обнаружена проблема (неточность): фрукты должны исчезать моментально как только змея на них наедет, но у меня так не происходит. Пытаемся исправить. змея двигается юлагодаря методу Run, а взимодействие с едой осуществляется в spawn, надо поменять порядок их осществления
# Проблема решена: в run изменили порядок методов