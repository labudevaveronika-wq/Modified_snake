from random import *

class Food:
    def __init__(self, count=0, obstacles=None):
        self.fruits = []

        if obstacles:  # если obstacles не пусто и не None
            self.obstacles = obstacles
        else:  # если obstacles пустое или None
            self.obstacles = []

        for i in range(count):
            fruit = self.create_fruit()
            while fruit is None:
                fruit = self.create_fruit()

            self.fruits.append(fruit)

    def create_fruit(self,obstacles=None):
        '''Поменяю немного историю создания фруктов.
        именно тут они будут создаваться, а в spawn именно появляться на поле.
        фрукт мог заспавниться в стене или в другом фрукте'''

        while True:
            x = randint(0, 17)
            y = randint(0, 17)

            position_occupied = False
            for obstacle in self.obstacles:
                if obstacle['position'] == (x, y):  # Сравниваем с нашими (x, y)
                    position_occupied = True
                    break

            if not position_occupied:
                for fruit in self.fruits:
                    if fruit['position'] == (x, y):
                        position_occupied = True
                        break

            if not position_occupied:
                fruit_counts = {'apple': 0, 'pear': 0, 'grape': 0}
                for fruit in self.fruits:
                    fruit_counts[fruit['type']] += 1

                min_count = min(fruit_counts.values())
                available_types = []

                for fruit_type, count in fruit_counts.items():
                    if count == min_count:
                        available_types.append(fruit_type)

                fruit_type = choice(available_types)

                if fruit_type == 'apple':
                    color = "red"
                elif fruit_type == 'pear':
                    color = "green"
                else:
                    color = "purple"


                return {
                    'position': (x, y),
                    'type': fruit_type,
                    'color': color
                }

    def spawn(self, fruits_index=None, obstacles=None): # появление рандомном месте
        '''Опишем создание и генерацаю трех фруктов на поле'''
        if obstacles is not None:
            self.obstacles = obstacles

        if fruits_index is not None:
            # Заменяем конкретный фрукт
            self.fruits[fruits_index] = self.create_fruit()
        else:
            # Добавляем новый фрукт
            self.fruits.append(self.create_fruit())

    def get_all_fruits(self): # Возвращает все фрукты
        return self.fruits

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