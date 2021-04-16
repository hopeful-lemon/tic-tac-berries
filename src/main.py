import pygame
import sys

from draw_helpers import * 
from game_logic import *
from scene import *

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
play_btn = pygame.image.load("assets/img/ui_btn_play.png")
play_btn = pygame.transform.scale(play_btn, (90,90))
ui_panel = pygame.image.load("assets/img/ui_panel.png")

ui_value = pygame.image.load("assets/img/ui_value.png")

ui_btn_menu = pygame.image.load("assets/img/ui_btn_menu.png")
ui_btn_music = pygame.image.load("assets/img/ui_btn_music.png")
ui_btn_replay = pygame.image.load("assets/img/ui_btn_replay.png")

ui_btn_menu = pygame.transform.scale(ui_btn_menu, btn_dim)
ui_btn_music = pygame.transform.scale(ui_btn_music, btn_dim)
ui_btn_replay = pygame.transform.scale(ui_btn_replay, btn_dim)
menu_bg = pygame.image.load("assets/img/menu_bg.png")
sky = pygame.image.load("assets/img/bg.png")

pygame.font.init()
default_font = pygame.font.Font("assets/fonts/Fipps-Regular.otf", 25)

# Game
game = Game()

# Scenes
scn_mgr = Scene_manager()

def menu_scn_draw():
    screen.fill(background_color)
    screen.blit(menu_bg, pygame.Rect(0, 0, size[0], size[1]))

    
    screen.blit(play_btn, pygame.Rect(220,300,10,10))

play_btn_rect = pygame.Rect(220,300,178,180); 

def menu_scn_handle_event(event):
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        if play_btn_rect.collidepoint(event.pos):
            scn_mgr.switch(1)


def game_scn_draw():
    screen.fill(background_color)
    screen.blit(sky, pygame.Rect(0, 0, size[0], size[1]))

    draw_board(screen, game, grid_pos, cell_dim, grid_color, x_img, o_img)
    draw_bottom_bar(screen, size, game.get_turn(), [x_img, o_img], ui_panel, ui_value, ui_btn_music, ui_btn_menu)
    draw_top_bar(screen, size, game, default_font, [x_img, o_img], ui_panel, ui_value, ui_btn_replay)

def game_scn_handle_event(event):
    cells = get_cells(grid_pos, cell_dim, grid_dim)
    bottom_bar_rects = get_bottom_bar_rects(size, ui_panel, ui_value, ui_btn_music, ui_btn_menu)
    top_bar_rects = get_top_bar_rects(size,  [x_img, o_img], ui_panel, ui_value, ui_btn_replay)
    
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        for l in range(3):
            for c in range(3):
                if cells[l][c].collidepoint(event.pos):
                    game.play(l, c)
        if bottom_bar_rects[1].collidepoint(event.pos):
            scn_mgr.switch(0)
            
        elif bottom_bar_rects[2].collidepoint(event.pos):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        if top_bar_rects[2].collidepoint(event.pos):
            game.reset()

menu_scn = Scene(menu_scn_draw, menu_scn_handle_event)
game_scn = Scene(game_scn_draw, game_scn_handle_event)
scn_mgr.add_scene(menu_scn)
scn_mgr.add_scene(game_scn)

# Music
pygame.mixer.music.load("assets/music/music.wav")
pygame.mixer.music.play(loops = -1)

while 1:

    for event in pygame.event.get():
        scn_mgr.handle_event(event)

    scn_mgr.draw()
    pygame.display.flip()


