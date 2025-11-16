import pygame
from food import Food
from sanke import Snake

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600)) # Создали окно 600x600 пикселей
        pygame.display.set_caption('Snake') # название

        # создадим объекты: сама змея,

