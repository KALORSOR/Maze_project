# main game loop

import pygame
from maze import Maze
from player import Player
from renderer import Renderer

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize maze, player, and renderer
maze = Maze()
player = Player(1.5, 1.5, 0)
#renderer = Renderer(screen, WIDTH, HEIGHT)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(1, maze)
    if keys[pygame.K_DOWN]:
        player.move(-1, maze)
    if keys[pygame.K_LEFT]:
        player.rotate(-1)
    if keys[pygame.K_RIGHT]:
        player.rotate(1)

    screen.fill((0, 0, 0))
    #renderer.render()
    pygame.display.flip()

pygame.quit()

