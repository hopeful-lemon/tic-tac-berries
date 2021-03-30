import pygame
import sys

from draw_helpers import * 
from game_logic import *

size = (550, 550)
width, height = size

background_color = (0x8e, 0xca, 0xe6)
grid_color = (0xff, 0xff, 0xff)

grid_dim = (3, 3)
cell_dim = (100, 100)
grid_width, grid_height = (grid_dim[0] * cell_dim[0], grid_dim[1] * cell_dim[1])
grid_pos = (width/2 - grid_width/2 , height/2 - grid_height/2)


pygame.init()
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    screen.fill(background_color)
    
    draw_grid(screen, grid_pos, cell_dim, grid_dim, grid_color)

    pygame.display.flip()
