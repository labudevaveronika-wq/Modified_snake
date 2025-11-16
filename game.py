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


# Проверка что все создалось
#game = Game()
#print("Окно создано!")
#print("Змейка создана:", game.snake)
#print("Еда создана:", game.food)
#print("Счет:", game.ckore)