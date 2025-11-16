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

        self.screen.fill(pygame.Color('black')) # залили экран черным

        for position in self.snake.position:
            square = pygame.Rect(position[0] * 40, position[1] * 40, 40, 40)
            '''position[0] * 40 - координата X (позиция змейки × 40 пикселей) 
            position[1] * 40 - координата Y (позиция змейки × 40 пикселей)
            40, 40 - ширина и высота прямоугольника (40×40 пикселей)'''

            pygame.draw.rect(self.screen, pygame.Color('red'), square)
            '''self.screen - на каком окне рисовать
            self.snake.snake_color - каким цветом (зеленый)
            rect - какой прямоугольник рисовать'''

        food_rect = pygame.Rect(self.food.position[0] * 40, self.food.position[1], 40, 40) # то же самое для еды
        if self.food.color == "red":
            color = (255, 0, 0)
        elif self.food.color == "green":
            color = (0, 255, 0)
        else:
            color = (128, 0, 128)

        pygame.draw.rect(self.screen, color, food_rect) # тут сама отрисовка: где нариосвать, каким цветом, что рисовать

        pygame.display.flip() # тут обновляем экарн



# Проверка что все создалось
#game = Game()
#print("Окно создано!")
#print("Змейка создана:", game.snake)
#print("Еда создана:", game.food)
#print("Счет:", game.ckore)