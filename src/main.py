import pygame
import sys

from draw_helpers import * 
from game_logic import *

# Useful variables
size = (550, 550)
width, height = size

background_color = (0x8e, 0xca, 0xe6)
grid_color = (0xff, 0xff, 0xff)

grid_dim = (3, 3)
cell_dim = (100, 100)
xo_dim = (50, 50)

grid_width, grid_height = (grid_dim[0] * cell_dim[0], grid_dim[1] * cell_dim[1])
grid_pos = (width/2 - grid_width/2 , height/2 - grid_height/2)

# Window initialization
pygame.init()
screen = pygame.display.set_mode(size)

# Ressources loading
x_img = pygame.image.load("assets/img/x.png")
o_img = pygame.image.load("assets/img/o.png")
x_img = pygame.transform.scale(x_img, xo_dim)
o_img = pygame.transform.scale(o_img, xo_dim)


# Game
game = Game()
game.play(0, 0)
game.play(1, 1)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    screen.fill(background_color)
    
    # draw_grid(screen, grid_pos, cell_dim, grid_dim, grid_color)
    draw_board(screen, game, grid_pos, cell_dim, grid_color, x_img, o_img)
    pygame.display.flip()
