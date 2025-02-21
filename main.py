import pgzrun
import random

GRID_WIDTH = 3
GRID_HEIGHT = 3
GRID_SIZE = 128

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

board = [
'NNN',
'NFN',
'NNN'
]

def screen_coords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
def draw_background():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit('null3.png', screen_coords(x, y))

def draw_scenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = board[y][x]
            if square == 'F':
                screen.blit('fire3.png', screen_coords(x, y))
            elif square == 'W':
                screen.blit('water1.png', screen_coords(x, y))
            elif square == 'E':
                screen.blit('earth1.png', screen_coords(x, y))
            #elif square == 'A':
                #screen.blit('air.png', screen_coords(x, y))

                

def draw():
    draw_background()
    draw_scenery()


pgzrun.go()
