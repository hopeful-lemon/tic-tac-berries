import pygame

# Draws a grid on a surface
#
# @param surface    Surface     The surface to draw on
# @param grid_pos   Tuple       Coordinates of the grid
# @param cell_dim   Tuple       Dimensions of one cell
# @param grid_dim   Tuple       Dimensions of the grid
# @param color      Tuple       Color of the grid

def draw_grid(surface, grid_pos, cell_dim, grid_dim, color):
    x, y = grid_pos
    w, h = cell_dim
    lines, columns = grid_dim

    for l in range(lines):
        for c in range(columns):
            r = pygame.Rect(x + c*w, y + l*h, w, h)
            pygame.draw.rect(surface, color, r, width = 3)

def get_cells(grid_pos, cell_dim, grid_dim):
    x, y = grid_pos
    w, h = cell_dim
    lines, columns = grid_dim

    cells = []
    for l in range(lines):
        line = []
        for c in range(columns):
            line.append(pygame.Rect(x + c*w, y + l*h, w, h))
        cells.append(line)
    return cells


def draw_board(surface, game, grid_pos, cell_dim, color, x_img, o_img):
    x, y = grid_pos
    w, h = cell_dim
    draw_grid(surface, grid_pos, cell_dim, (3,3), color)
    
    for l in range(3):
        for c in range(3):
            rxo = x_img.get_rect()
            ww = rxo.width
            hh = rxo.width
            r = pygame.Rect(x + c*w + w/2 - ww/2, y + l*h + h/2 - hh/2, ww, hh)
            if(game.grid[l][c] == 'x'):
                surface.blit(x_img, r)
            elif(game.grid[l][c] == 'o'):
                surface.blit(o_img, r)

def get_bottom_bar_rects(dim, ui_panel, ui_value, ui_btn_music, ui_btn_menu):
    panel_rect = ui_panel.get_rect()
    panel_rect.x = dim[0]/2 - panel_rect.w/2
    panel_rect.y = dim[1] - 100
    
    btn_menu_rect = ui_btn_menu.get_rect()
    btn_menu_rect.x = panel_rect.x + panel_rect.w - btn_menu_rect.w - 50
    btn_menu_rect.y = panel_rect.y + 20

    btn_music_rect = ui_btn_music.get_rect()
    btn_music_rect.x = panel_rect.x + panel_rect.w - 2*btn_music_rect.w - 55
    btn_music_rect.y = panel_rect.y + 20

    ui_value_rect = ui_value.get_rect()
    ui_value_rect.x = panel_rect.x + 40 
    ui_value_rect.y = panel_rect.y + 20

    turn_rect = ui_value_rect
    
    return [panel_rect, btn_menu_rect, btn_music_rect, ui_value_rect, turn_rect]


def draw_bottom_bar(surface, dim, turn, xo_images, ui_panel, ui_value, ui_btn_music, ui_btn_menu):
    
    panel_rect, btn_menu_rect, btn_music_rect, ui_value_rect, turn_rect = get_bottom_bar_rects(
        dim, ui_panel, ui_value, ui_btn_music, ui_btn_menu)

    surface.blit(ui_panel, panel_rect)
    surface.blit(ui_btn_menu, btn_menu_rect)
    surface.blit(ui_btn_music, btn_music_rect)
    surface.blit(ui_value, ui_value_rect)
    turn_rect.x += ui_value_rect.w/2 - 25
    surface.blit(xo_images[0 if turn=='x' else 1], turn_rect)





