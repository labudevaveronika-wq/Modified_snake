from random import *

class Food:
    def __init__(self, ):
        self.position = None
        self.type = None
        self.color = None
        self.spawn()

    def spawn(self): # появление рандомном месте
        x = randint(0, 14)
        y = randint(0, 14)
        self.type = choice(["apple", "pear", "grape"])  # сначала выбираем тип
        self.position = (x, y)

        # потом устанавливаем цвет по типу
        if self.type == "apple":
            self.color = "red"
        elif self.type == "pear":
            self.color = "green"
        else:
            self.color = "purple"

    def get_position(self): # получить позицию еды
        return self.position

    def get_type(self): # получить тип еды для обработки эффект на змею
        return self.type

# Тест
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