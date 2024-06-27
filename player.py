# player movements

import math

class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.05
        self.rot_speed = 0.03

    def move(self, direction, maze):
        new_x = self.x + direction * self.speed * math.cos(self.angle)
        new_y = self.y + direction * self.speed * math.sin(self.angle)
        if not maze.is_wall(int(new_x), int(new_y)):
            self.x = new_x
            self.y = new_y

    def rotate(self, direction):
        self.angle += direction * self.rot_speed

