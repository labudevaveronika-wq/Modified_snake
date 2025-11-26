from random import *
from sanke import Snake

class Obstacle:
    def __init__(self, count = 7, snake_positions=None):
        self.obstacles = []
        for i in range(count):
            self.obstacles.append(self.create_obstacle(snake_positions))

    def create_obstacle(self, snake_positions=None):

        x = randint(0, 14)
        y = randint(0, 14)

        if snake_positions:
            while (x, y) in snake_positions:
                y = randint(0, 14)
                x = randint(0, 14)

        width = 40
        hight = 40

        return {
            'position': (x, y),
            'width': width,
            'height': hight,
            'color': (100, 100, 100),
        }

    def get_all_obstacles(self):
        return self.obstacles
