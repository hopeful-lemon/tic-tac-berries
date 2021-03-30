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
