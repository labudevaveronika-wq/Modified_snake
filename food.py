import time
from random import *

class Food:
    def __init__(self, count = 3):
        self.fruits = []

        for i in range(count):
            self.fruits.append(self.create_fruit())



        self.position = None
        self.type = None
        self.color = None


    def create_fruit(self):
        '''Поменяю немного историю создания фруктов.
        именно тут они будут создаваться, а в spawn именно появляться на поле.
        '''
        x = randint(0, 14)
        y = randint(0, 14)
        fruit_type = choice(["apple", "pear", "grape"])  # сначала выбираем тип

        # потом устанавливаем цвет по типу
        if fruit_type == "apple":
            color = "red"
        elif fruit_type == "pear":
            color = "green"
        else:
            color = "purple"

        self.position = (x, y)

        return { #возвращаем
            'position': (x, y),  # координаты
            'type': fruit_type,  # тип фрукта
            'color': color  # цвет
        }


    def spawn(self, fruits_index=None): # появление рандомном месте
        '''Опишем создание и генерацаю трех фруктов на поле'''
        if fruits_index is not None:
            self.fruits[fruits_index] = self.create_fruit()
        else:
            self.fruits.append(self.create_fruit())



    def get_all_fruits(self): # Возвращает все фрукты
        return self.fruits

    def get_type(self): # получить тип еды для обработки эффект на змею
        return self.type

    def remove_fruits(self): # тут будет происходить удаление фрукта по его позиции и возвращение его типа
        pass

## Тест
#food = Food()
#print("Позиция еды:", food.get_position())
#print("Тип еды:", food.get_type())
#print("Цвет еды:", food.color)
# spawn()
#food.spawn()
#print("Новая позиция:", food.get_position())
#print("Новый тип:", food.get_type())
#print("Новый цвет:", food.color)

# Игра проверяет столкновение
#if snake.head == food.get_position():  # змейка на еде?
#    food_type = food.get_type()         # что съела?
#    snake.eat(food_type)               # применить эффект
#    food.spawn()                       # создать новую еду

# я захотела генерить несколько фруктов, например 3
# возникла проблема, что они все одинаковые появляются, и я решила проблему в лоб
#
#
#
#