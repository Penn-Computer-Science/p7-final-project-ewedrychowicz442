import pygame

pygame.init()

maze = [
    [1, 0, 0, 0, 0, 0, ],
    []
]

#variables
TILE_SIZE = 32
GAME_WIDTH = 512
GAME_HEIGHT = 512
ROWS = len(maze)
COLS = len(maze[0])

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Maze")

'''
1 = path_tile
2 = wall
'''

def create_maze():
    for row in range(ROWS):
        for column in range(COLS):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            if maze[row][column] == 1:
                pygame.draw.rect(screen, ("blue"), (x, y, TILE_SIZE, TILE_SIZE))
                