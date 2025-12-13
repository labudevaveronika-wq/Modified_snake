from random import *

class Obstacle:
    def __init__(self, count = 10, snake_positions=None):
        self.obstacles = []
        for i in range(count):
            self.obstacles.append(self.create_obstacle(snake_positions))

    def create_obstacle(self, snake_positions=None):

        x = randint(0, 17)
        y = randint(0, 17)

        if snake_positions:
            #препятствие могло заспавниться в препятствии
            while (x, y) in snake_positions or (x, y) in self.obstacles:
                y = randint(0, 17)
                x = randint(0, 17)
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
