from random import *

class Obstacle:
    def __init__(self, count = 5):
        self.obstacles = []
        for i in range(count):
            self.obstacles.append(self.create_obstacke())

        def create_obstacke(self):
            x = randint(0, 14)
            y = randint(0, 14)
            width = 10
            hight = 20

            return {
                'position': (x, y),
                'width': width,
                'height': hight,
                'color': randint(100, 100, 100),
            }

        def get_all_obstacles(self):
            return self.obstacles
