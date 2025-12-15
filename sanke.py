from random import *
import time

class Snake:
    def __init__(self):
        '''Инциализируем: Начальная длина змейки,
         Начальный цвет (зеленый),
         Высота игрового поля, ширина поля,
         начальная позиция змеи (головы),
         список-тело змеи,
         система эволюции: счет, 10 цветов эволюции, текущий нулевой цвет,
         флаг для ускорения,
         время окончанич ускорения'''

        self.snake_body = 3
        self.hight_table = 20
        self.size_table = 20

        center_x = self.size_table // 2
        center_y = self.hight_table // 2
        self.position = [(center_x, center_y), (center_x - 1, center_y), (center_x - 2, center_y)]
        self.head = self.position[0]
        self.direction = (1, 0)

        self.evolution_stage = 0
        self.evolution_score = 0
        self.evolution_colors = self.get_evolution_color(10)
        self.snake_color = self.evolution_colors[0]

        self.flag_acceleration = False
        self.acceleration_end_time = time.time() + 10

        self.flag_cheat = False

    def state(self, obstacles = None):
        '''Проверка состояния змеи: жива ли змеи или нет.

        1) Врезалась ли она сама в себя
        2) Врезалась ли она в препятвие'''

        if self.head in self.position[1::] and self.snake_body!=2:
            return False

        if obstacles is not None:
            for obstacle in obstacles:
                if self.head == obstacle['position']:
                    if self.flag_cheat == True:
                        return True
                    else:
                        return False
        return True


    def simple_move(self):
        '''Обичное движение змеи.
        1) По х и по у создаем координатвы
        2) Телпортирует змею вне поля
        3) Добавлет "новую" голову
        4) убирает хвост - послдений элемент'''
        nx = self.head[0] + self.direction[0] # Обновление позиции головы по х
        ny = self.head[1] + self.direction[1] # Обновление позиции головы по у

        # телепортация через границы
        nx = nx % self.size_table
        ny = ny % (self.hight_table-1)

        self.position.insert(0, (nx, ny)) # Добавление "новой головы" в змею

        self.head = self.position[0] # Обновление головы, а точнее ее позиции

        if len(self.position) > self.snake_body:
            self.position.pop() # Удаление хвоста, если длина позиций больше self.snake_body



    def eat(self, food_type):
        '''Процесс, который будет обрабатывать то, что съела змея.
        Обновление счетчика очков для комбо-еды.'''
        if food_type == 'apple':
            self.snake_body += 1 # Красное яблоко - длина + 1
            end = self.position[-1]
            self.position.append(end)
        if food_type == 'pear':
            #змейка длины 0 конечно весело но я это исправлю наверное
            if (self.snake_body>1):    
                self.snake_body -= 1 # Зеленая груша - длина - 1
            if len(self.position) > self.snake_body:
                self.position.pop()
        if food_type == 'grape':
            self.flag_acceleration = True
            self.acceleration_end_time = max(time.time() + 10,self.acceleration_end_time)
            '''Активация ускорение для змеи'''

        return  food_type
        '''Возвращение эффекта для вижуала змеи.'''


    def moving(self, direction_type):
        '''Обработка изменения направления.
        Проверка разворота на 180.
        Обновление self.direction'''
        '''всё равно можно было повернуть на 180 и самоубиться
        теперь по идеи незя наверное...'''
        if len(self.position)!=1:
           if (direction_type[0]+self.head[0], direction_type[1]+self.head[1]) != self.position[1]: # Проверка разворота на 180°
                self.direction = direction_type # Обновление направления
        else:
            if (direction_type[0] * -1, direction_type[1] * -1) != self.direction: # Проверка разворота на 180°
                self.direction = direction_type # Обновление направления


    def update_boost(self):
        if self.flag_acceleration and time.time() > self.acceleration_end_time:
            self.flag_acceleration = False

    def get_evolution_color(self, count = 10):
        not_have = [
            (255, 0, 0),    # красный - яблоко
            (0, 255, 0),    # зеленый - груша
            (128, 0, 128),  # фиолетовый - виноград
            (100, 100, 100) # серый - препятствия
        ]

        evolution_colors = []
        for i in range(count):
            while True:
                color = (randint(50, 200), randint(50, 200), randint(50, 200))
                if color not in not_have:
                    evolution_colors.append(color)
                    break

        return evolution_colors

    def evolve(self):
        if self.evolution_stage < len(self.evolution_colors) - 1:
            self.evolution_stage += 1
            self.snake_color = self.evolution_colors[self.evolution_stage]




# Простой тест
#snake = Snake()
#print(snake.state())
#snake.simple_move()
#print(snake.head)
#True
#(11, 10)