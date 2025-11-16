import pygame
from food import Food
from sanke import Snake

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600)) # Создали окно 600x600 пикселей
        pygame.display.set_caption('Snake') # название окна

        # создадим объекты: сама змея, еда
        self.food = Food()
        self.snake = Snake()

        self.ckore = 0 # счет игрока, начало с нуля

        self.life = True # змея жива или нет True - жива, False - нет

    def run(self):

    def events(self): # проверять все от клавиш до эффектов
        '''Проверять все события pygame
        Если событие "закрытие окна" - останавливать игру
        Если нажата клавиша - определять какая именно
        Если нажаты стрелки - менять направление змейки'''

    def update(self):
        '''Двигать змейку вперед
        Проверять столкновение змейки с едой
        Проверять столкновение змейки с собой или границами
        Если змейка съела еду - увеличивать счет и создавать новую еду'''

    def draw(self):
        '''Залить экран черным цветом
        Нарисовать змейку (по координатам из snake.position)
        Нарисовать еду (по координатам из food.position)
        Отобразить счет игрока на экране'''


# Проверка что все создалось
#game = Game()
#print("Окно создано!")
#print("Змейка создана:", game.snake)
#print("Еда создана:", game.food)
#print("Счет:", game.ckore)