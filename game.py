from food import Food
from obstacle import Obstacle
from sanke import Snake
import time
import pygame
from snake_database import SnakeDatabase
from menu import GameOverScreen


class Game:
    def __init__(self, level = 1):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700)) # Создали окно 600x600 пикселей
        pygame.display.set_caption('Snake') # название окна

        # Шрифты для отображения счета, уровня и жизней
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 48)  # Для большего текста

        self.level = level

        # создадим объекты: сама
        # змея, еда
        self.snake = Snake()
        self.obstacles = Obstacle()
        self.food = Food()
        #сделал так чтобы еда спавнилась ПОСЛЕ стен объяснения в файле с едой

        self.score = 0 # счет игрока, начало с нуля

        self.life = True # змея жива или нет True - жива, False - нет

        self.score = 0  # текущий счёт
        self.start_time = 0  # время начала игры
        self.player_name = "Гость"  # имя игрока
        self.is_game_over = False  # флаг завершения игры
        self.play_time = 0  # время игры в секундах

        self.db = SnakeDatabase()

        self.game_over_screen = GameOverScreen(self.screen)

    def run(self):
        '''Таким образом в run только вызов методов'''
        clock = pygame.time.Clock()

        if self.player_name == "Гость":
            name = self.game_over_screen.show_name_input()
            if name:
                self.player_name = name
                if self.player_name != "Гость":
                    self.db.add_player(self.player_name)
            else:
                return

        self.start_time = time.time()

        while self.life == True: # проверка на жизнь змеи
            self.events() # вызываем меропреятие (действие) из метода обработки нажатия клавиш или события
            self.snake.simple_move()  # змея двигается
            self.update()
            self.draw() # рисуем новый кадр

            if not self.snake.state():
                self.handle_game_over()
                return

            if self.snake.flag_acceleration:
                clock.tick(10)
            else:
                clock.tick(5)

#    def prtals_movement_in_space(self):

    def show_name_input_screen(self):
        """Экран ввода имени игрока"""
        self.screen.fill((0, 0, 0))  # чёрный фон

        # Заголовок
        title = self.big_font.render("ВВЕДИТЕ ВАШЕ ИМЯ", True, (255, 255, 255))
        self.screen.blit(title, (200, 100))

        # Инструкция
        instruction = self.font.render("Напишите имя и нажмите Enter", True, (200, 200, 200))
        self.screen.blit(instruction, (200, 200))

        # Поле для ввода
        input_box = pygame.Rect(200, 300, 300, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), input_box, 2)

        # Текст в поле
        input_text = ""

        pygame.display.flip()

        # Обработка ввода
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter
                        waiting = False
                    elif event.key == pygame.K_BACKSPACE:  # Backspace
                        input_text = input_text[:-1]
                    else:
                        # Добавляем символ
                        if len(input_text) < 15:
                            input_text += event.unicode

            # Обновляем отображение текста
            self.screen.fill((0, 0, 0))
            self.screen.blit(title, (200, 100))
            self.screen.blit(instruction, (200, 200))
            pygame.draw.rect(self.screen, (255, 255, 255), input_box, 2)

            # Текст в поле ввода
            text_surface = self.font.render(input_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (210, 310))

            pygame.display.flip()

        # Сохраняем имя
        if input_text.strip():
            self.player_name = input_text.strip()
            # Добавляем игрока в базу
            self.db.add_player(self.player_name)
        else:
            self.player_name = "Гость"


    def handle_game_over(self):
        self.game_over = True
#        self.game_over_reason = reason
        self.total_play_time = int(time.time() - self.start_time)

        if self.player_name != "Гость":
            self.save_game_result()

        self.life = False
        self.show_game_over_screen()
        self.show_game_over_menu()

    def show_game_over_screen(self):
        self.screen.fill(pygame.Color('black'))

    def save_game_result(self):
        try:
            success = self.db.save_game_result(
                username=self.player_name,
                score=self.score,
                play_time=self.total_play_time
            )
            return success
        except Exception as e:
            return False

    def show_game_over_screen(self):
        self.screen.fill(pygame.Color('black'))

        title = self.big_font.render("ИГРА ОКОНЧЕНА", True, (255,0,0))
        self.screen.blit(title, (250,100))

        current_status = [
            f"Текущая игра:",
            f"Игрок: {self.player_name}",
            f"Счёт: {self.score}",  # или self.skore/ckore
            f"Длина змеи: {self.snake.snake_body}",
            f"Время: {self.total_play_time} сек"
        ]

        player_status = self.get_player_status_from_db()

        y_pos = 170
        for line in current_status:
            text = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text, (250, y_pos))
            y_pos += 40

        # 2. Отобразить player_status если есть
        if player_status:
            y_pos += 20
            db_stats = [
                f"Общая статистика:",
                f"Лучший результат: {player_status.get('best_score', 0)}",
                f"Всего очков: {player_status.get('total_score', 0)}",
                f"Игр сыграно: {player_status.get('games_played', 0)}",
                f"Общее время: {player_status.get('total_time', 0)} сек"
            ]

            for line in db_stats:
                text = self.font.render(line, True, (100, 200, 255))
                self.screen.blit(text, (250, y_pos))
                y_pos += 40

        # 3. Обновить экран
        pygame.display.flip()

        # 4. Пауза
        pygame.time.wait(3000)



    def get_player_status_from_db(self):
        if self.player_name == "Гость":
            return None

        try:
            return self.db.get_player_status(self.player_name)
        except Exception as e:
            return None



    def events(self): # проверять все от клавиш до эффектов
        '''Проверять все события pygame
        Если событие "закрытие окна" - останавливать игру
        Если нажата клавиша - определять какая именно
        Если нажаты стрелки - менять направление змейки'''
        for event in pygame.event.get(): # проыерить событие: что именно случилось, кнопка или закрытие окна
            if event.type == pygame.QUIT: # если нажат крестик для закрытия окна
                self.life = False
            # добавляю управление змеей с помощью кнопок - стрелок
            # проверка на нажатие стрелок
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:  # вниз
                    self.snake.moving((0, +1))
                if event.key == pygame.K_UP:  # вверх
                    self.snake.moving((0, -1))
                if event.key == pygame.K_LEFT:  # влево
                    self.snake.moving((-1, 0))
                if event.key == pygame.K_RIGHT:  # вправо
                    self.snake.moving((1, 0))


            # надо добавить проверку на то, что змея съедает фрукт

    def update(self):
        '''Двигать змейку вперед
        Проверять столкновение змейки с едой
        Проверять столкновение змейки с собой или границами
        Проверять столкновение с препятсвием.
        Если змейка съела еду - увеличивать счет и создавать новую еду'''
        self.snake.update_boost()
        # проверка на столкновение с любым фруктом
        fruits = self.food.get_all_fruits()
        for i, fruit in enumerate(fruits):
            if self.snake.head == fruit['position']:
                food_type = fruit['type']
                self.snake.eat(food_type)
                self.food.spawn(i) # замена того фрукта, который съели и добавили новый
                if food_type == 'apple':
                    self.score += 10
                elif food_type == 'pear':
                    self.score += 5
                elif food_type == 'grape':
                    self.score += 15

                self.snake.evolution_score += 1
                if self.snake.evolution_score >= 10:  # каждые 10 очков
                    self.snake.evolve()
                    self.snake.evolution_score = 0  # сбрасываем счетчик
                break


        for obstacle in self.obstacles.get_all_obstacles():
            head_rect = pygame.Rect(self.snake.head[0] * 40, self.snake.head[1] * 40, 40, 40)
            obstacle_rect = pygame.Rect(obstacle['position'][0] * 40, obstacle['position'][1] * 40, obstacle['width'], obstacle['height'])


            if head_rect.colliderect(obstacle_rect):
                self.life = False
                break

        if not self.snake.state():
            self.life = False


    def draw(self):
        '''Залить экран черным цветом
        Нарисовать змейку (по координатам из snake.position)
        Нарисовать еду (по координатам из food.position)
        Отобразить счет игрока на экране'''

        self.screen.fill(pygame.Color('black')) # залили экран черным

        # отрисовка препятствий
        for obstacle in self.obstacles.get_all_obstacles():
            obstacle_rect = pygame.Rect(obstacle['position'][0] * 40, obstacle['position'][1] * 40, obstacle['width'], obstacle['height'])
            pygame.draw.rect(self.screen, obstacle['color'], obstacle_rect)


        for position in self.snake.position:
            square = pygame.Rect(position[0] * 40, position[1] * 40, 40, 40)
            '''position[0] * 40 - координата X (позиция змейки × 40 пикселей) 
            position[1] * 40 - координата Y (позиция змейки × 40 пикселей)
            40, 40 - ширина и высота прямоугольника (40×40 пикселей)'''

            pygame.draw.rect(self.screen, pygame.Color('green'), square)
            '''self.screen - на каком окне рисовать
            self.snake.snake_color - каким цветом (зеленый)
            rect - какой прямоугольник рисовать'''

        for fruit in self.food.get_all_fruits():
            food_rect = pygame.Rect(fruit['position'][0] * 40, fruit['position'][1] * 40, 40, 40) # то же самое для еды
            if fruit['color'] == "red":
                color = (255, 0, 0)
            elif fruit['color'] == "green":
                color = (0, 255, 0)
            else:
                color = (128, 0, 128)

            pygame.draw.rect(self.screen, color, food_rect)

        for position in self.snake.position:
            if self.snake.flag_acceleration:
                color = (0, 255, 0)  # ярко-зеленый при ускорении
            else:
                color = (0, 200, 0)  # обычный зеленый

            square = pygame.Rect(position[0] * 40, position[1] * 40, 40, 40)
            pygame.draw.rect(self.screen, color, square)

        for position in self.snake.position:
            # Используем цвет эволюции
            if self.snake.flag_acceleration:
                color = (min(255, self.snake.snake_color[0] + 50),
                         min(255, self.snake.snake_color[1] + 50),
                         min(255, self.snake.snake_color[2] + 50))  # ярче при ускорении
            else:
                color = self.snake.snake_color  # обычный цвет эволюции

            square = pygame.Rect(position[0] * 40, position[1] * 40, 40, 40)
            pygame.draw.rect(self.screen, color, square)




        pygame.display.flip() # тут обновляем экарн



# Проверка что все создалось
#game = Game()
#print("Окно создано!")
#print("Змейка создана:", game.snake)
#print("Еда создана:", game.food)
#print("Счет:", game.ckore)

# тест отрисовки
#game = Game()
#game.run()
# поначалу вот такой вывод для этого теста:
# pygame 2.6.1 (SDL 2.28.4, Python 3.13.7)
# Hello from the pygame community. https://www.pygame.org/contribute.html
# так просихдит потому что окно появляется и исчезает, так как программа сразу завершается
# это по идее можно исправить с помощью изменения метода run
# Получилось, появляется черное окно и висит до закрытия
# новый тест
game = Game()
#print("Змейка:", game.snake.position)
#print("Еда:", game.food.position)
game.run()

# обнаружена проблема (неточность): фрукты должны исчезать моментально как только змея на них наедет, но у меня так не происходит. Пытаемся исправить. змея двигается юлагодаря методу Run, а взимодействие с едой осуществляется в spawn, надо поменять порядок их осществления
# Проблема решена: в run изменили порядок методов


