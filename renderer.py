# implement raycasting to render 3D view of maze

import pygame
import math

class Renderer:
    def __init__(self, screen, width, height, textures):
        self.screen = screen
        self.width = width
        self.height = height
        self.textures = textures

    def render(self, player, maze):
        for x in range(self.width):
            ray_angle = (player.angle - math.pi / 6) + (x / self.width) * math.pi / 3
            for depth in range(1, 20):
                target_x = player.x + depth * 0.1 * math.cos(ray_angle)
                target_y = player.y + depth * 0.1 * math.sin(ray_angle)
                if maze.is_wall(int(target_x), int(target_y)):
                    texture = self.textures['wall']
                    texture_x = int((target_x % 1) * texture.get_width())
                    column = texture.subsurface(texture_x, 0, 1, texture.get_height())
                    column = pygame.transform.scale(column, (1, self.height // depth))
                    self.screen.blit(column, (x, self.height // 2 - column.get_height() // 2))
                    break
