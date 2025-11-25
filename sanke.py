import time
from random import randint

import pygame


class Snake:
    def __init__(self):
        self.snake_body = 3
        self.snake_color = (0, 200, 0)
        self.hight_table = 15
        self.size_table = 15

        center_x = self.size_table // 2
        center_y = self.hight_table // 2
        self.position = [(center_x, center_y), (center_x - 1, center_y), (center_x - 2, center_y)]
        self.head = self.position[0]
        self.direction = (1, 0)
        self.flag_acceleration = False
        self.acceleration_end_time = time.time() + 10

    def state(self, ):
        '''Здесь будет статус сотояния тела в поле.
        Проверка на столкновение: жива или нет.
        Проверка выхода за границы.'''

        if self.head in self.position[1::]:
            return False # змея мертва (врезалась в себя)'

        if (self.head[0] < 0 or self.head[0] >= self.size_table) or (self.head[1] < 0 or self.head[1] >= self.size_table):
            return False # змея мертва (вне поля)

        return True # Все хорошо змея жива, пока что...'



    def simple_move(self):
        '''Простое движение змеи, процесс, который длится до столкновения.
        Перемещать змейку на одну клетку в текущем направлении.
        Брать позицию головы и добавлять направление движения.
        Обновлять переменную self.head.'''
        nx = self.head[0] + self.direction[0] # Обновление позиции головы по х
        ny = self.head[1] + self.direction[1] # Обновление позиции головы по у

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
            self.snake_body -= 1 # Зеленая груша - длина - 1
            if len(self.position) > self.snake_body:
                self.position.pop()
        if food_type == 'grape':
            self.flag_acceleration = True
            self.acceleration_end_time = time.time() + 10
            '''Активация ускорение для змеи'''

        return  food_type
        '''Возвращение эффекта для вижуала змеи.'''


    def moving(self, direction_type):
        '''Обработка изменения направления.
        Проверка разворота на 180.
        Обновление self.direction'''

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

        evolution_color = []
        for i in range(count):
            while True:
                color = (randint(50, 200), randint(50, 200), randint(50, 200))
                if color not in not_have:
                    evolution_color.append(color)
                    break

        return evolution_color



# Простой тест
#snake = Snake()
#print(snake.state())
#snake.simple_move()
#print(snake.head)
#True
#(11, 10)