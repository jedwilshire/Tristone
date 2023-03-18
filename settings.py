import pygame
BOXSIZE = 80

BOARDWIDTH = 5
BOARDHEIGHT = 5
SIDEBOARDWIDTH = BOXSIZE * 2
BOTTOMBOARDHEIGHT = BOXSIZE // 2

WIDTH = BOXSIZE * BOARDWIDTH + SIDEBOARDWIDTH
HEIGHT = BOXSIZE * BOARDHEIGHT + BOTTOMBOARDHEIGHT
TITLE = 'Tristone'
FPS = 60

## COLORS
#            R    G    B
BLACK       = (  0,  0,  0)
BLUE        = (  0,  0,255)
BROWN       = (165, 42, 42)
CYAN        = (  0,255,255)
DARKGREEN   = (  0,100,  0)
GOLD        = (255,215,  0)
GRAY        = (100,100,100)
GREEN       = (  0,128,  0)
INDIGO      = ( 75,  0,130)
MAGENTA     = (255,  0,255)
NAVY        = (  0,  0,128)
LIME        = (  0,255,  0)
ORANGE      = (255,128,  0)
PURPLE      = (255,  0,255)
RED         = (255,  0,  0)
SADDLEBROWN = (139, 69, 19)
SIENNA      = (160, 82, 45)
SILVER      = (192,192,192)
VIOLET      = (238,130,238)
WHEAT       = (245,222,179)
WHITE       = (255,255,255)
YELLOW      = (255,255,  0)

BGCOLOR = SIENNA

# Shape constants
STAR = 'star'
CIRCLE = 'circle'
SQUARE = 'square'

ALLSHAPES = [STAR, CIRCLE, SQUARE]
ALLCOLORS = [NAVY, DARKGREEN, PURPLE]

def makeList(row, col):
    board = []
    for i in range(row):
        board.append([])
        for k in range(col):
            board[i].append(None)
    return board
