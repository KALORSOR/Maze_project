# implement raycasting to render 3D view of maze

import pygame
import math

class Renderer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def render(self, player, maze):
        for x in range(self.width):
            ray_angle = (player.angle - math.pi / 6) + (x / self.width) * math.pi / 3
            for depth in range(20):
                target_x = player.x + depth * math.cos(ray_angle)
                target_y = player.y + depth * math.sin(ray_angle)
                if maze.is_wall(int(target_x), int(target_y)):
                    color = (255 - depth * 10, 255 - depth * 10, 255 - depth * 10)
                    pygame.draw.rect(self.screen, color, (x, self.height // 2 - 200 // depth, 1, 400 // depth))
                    break

