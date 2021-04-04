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

            