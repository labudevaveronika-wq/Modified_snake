from random import *

class Obstacle:
    def __init__(self, count = 7):
        self.obstacles = []
        for i in range(count):
            self.obstacles.append(self.create_obstacle())

    def create_obstacle(self):
        x = randint(0, 14)
        y = randint(0, 14)
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
