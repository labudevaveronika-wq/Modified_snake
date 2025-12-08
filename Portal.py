import pygame
from obstacle import Obstacle
from food import Food
from sanke import Snake
from random import *

class Portal:
    def __init__(self, obstacles_positions, food_positions, snake_positions):
        occupied_places = self.get_occupied_position(obstacles_positions, food_positions, snake_positions)
        free_positions = self.get_free_position(occupied=occupied_places)

        portal_pos1 = choice(free_positions)
        free_positions.remove(portal_pos1)

        portal_pos2 = choice(free_positions)
        free_positions.remove(portal_pos2)

        self.portals = [
            {
                'position': portal_pos1,
                'color': (255, 255, 0),  # Ярко-желтый
                'width': 40,
                'height': 40,
                'type': 'in'  # Для идентификации
            },
            {
                'position': portal_pos2,
                'color': (255, 200, 0),  # Оранжево-желтый
                'width': 40,
                'height': 40,
                'type': 'out'
            }
        ]

    def get_occupied_position(self, obstacles, foods, snake_positions):
        occupied = []
        # 1. Позиции препятствий
        for obstacle in obstacles:
            occupied.append(obstacle['position'])
        # 2. Позиции еды
        for food in foods:
            occupied.append(food['position'])
        # 3. Позиции змейки
        occupied.extend(snake_positions)
        return occupied

    def get_free_position(self, occupied):
        free_positions = []
        for x in range(15):
            for y in range(15):
                pos = (x , y)
                if pos not in occupied:
                    free_positions.append(pos)
        return free_positions

    def get_portals_for_index(self, index):
        return self.portals[index]






