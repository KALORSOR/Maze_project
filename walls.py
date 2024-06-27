import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Map and player setup
MAP = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
TILE_SIZE = 64
MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = TILE_SIZE * 5

player = {
    "x": TILE_SIZE + TILE_SIZE // 2,
    "y": TILE_SIZE + TILE_SIZE // 2,
    "angle": 0
}

def raycasting(screen, player, MAP):
    start_angle = player["angle"] - HALF_FOV
    for ray in range(NUM_RAYS):
        for depth in range(MAX_DEPTH):
            target_x = player["x"] + math.cos(start_angle) * depth
            target_y = player["y"] + math.sin(start_angle) * depth
            
            col = int(target_x / TILE_SIZE)
            row = int(target_y / TILE_SIZE)
            
            if MAP[row][col] == 1:
                color = (255 / (1 + depth * depth * 0.0001),) * 3
                pygame.draw.line(screen, color, (player["x"], player["y"]), (target_x, target_y))
                break
            
        start_angle += FOV / NUM_RAYS

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    raycasting(screen, player, MAP)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
