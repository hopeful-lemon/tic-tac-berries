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
btn_dim = (64, 64)

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

ui_panel = pygame.image.load("assets/img/ui_panel.png")

ui_value = pygame.image.load("assets/img/ui_value.png")

ui_btn_menu = pygame.image.load("assets/img/ui_btn_menu.png")
ui_btn_music = pygame.image.load("assets/img/ui_btn_music.png")
ui_btn_menu = pygame.transform.scale(ui_btn_menu, btn_dim)
ui_btn_music = pygame.transform.scale(ui_btn_music, btn_dim)

# Game
game = Game()

while 1:
    cells = get_cells(grid_pos, cell_dim, grid_dim)
    bottom_bar_rects = get_bottom_bar_rects(size, ui_panel, ui_value, ui_btn_music, ui_btn_menu)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for l in range(3):
                for c in range(3):
                    if cells[l][c].collidepoint(event.pos):
                        game.play(l, c)
            if bottom_bar_rects[1].collidepoint(event.pos):
                print("MENU (Not implemented yet)")
                #menu
            elif bottom_bar_rects[2].collidepoint(event.pos):
                print("MUSIC (Not implemented yet)")
                #music
       

    
    screen.fill(background_color)
    
    draw_board(screen, game, grid_pos, cell_dim, grid_color, x_img, o_img)
    draw_bottom_bar(screen, size, game.get_turn(), [x_img, o_img], ui_panel, ui_value, ui_btn_music, ui_btn_menu)

    pygame.display.flip()
