from settings import *
from writer import Writer
import pygame
# global variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
board = makeList(BOARDHEIGHT, BOARDWIDTH) # imported from settings
pieces = []

p1Score = Writer(screen, color = CYAN, size = 20)
p1Score.setText('0')

p2Score = Writer(screen, color = ORANGE, size = 20)
p2Score.setText('0')

playerIndicator = Writer(screen, size = 20)
playerIndicator.setText('Player 1 Turn')

# set game caption
pygame.display.set_caption(TITLE)

def onMousePress(x, y):
    if playerIndicator.getText() == 'Player 1 Turn' or playerIndicator.getText() == 'Player 2 Turn':
        if x > BOARDWIDTH * BOXSIZE:
            for piece in pieces:
                if piece.rect.collidepoint((x, y)):
                    piece.selected = True
                else:
                    piece.selected = False
        else:
            selectedPiece = None
            for piece in pieces:
                if piece.selected == True:
                    selectedPiece = piece
                    piece.selected = False # turn off selection
            if selectedPiece != None:
                for row in range(BOARDHEIGHT):
                    for col in range(BOARDWIDTH):
                        spot = board[row][col]
                        if spot.rect.collidepoint((x, y)):
                            if spot.shape == None:  # make sure empty
                                spot.shape = selectedPiece.shape
                                spot.color = selectedPiece.color
                                #print(selectedPiece.shape, selectedPiece.color)
                                spot.image.blit(selectedPiece.image, (0, 0))
                checkForScore(selectedPiece.shape, selectedPiece.color)
                removePieces()
                if int(p1Score.getText()) >= 20:
                    playerIndicator.setText('Player 1 wins!')
                elif int(p2Score.getText()) >= 20:
                    playerIndicator.setText('Player 2 wins!')
                elif playerIndicator.getText() == 'Player 1 Turn':
                    playerIndicator.setText('Player 2 Turn')
                else:
                    playerIndicator.setText('Player 1 Turn')
            

def removePieces():
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            spot = board[row][col]
            if spot.remove == True:
                spot.image.fill(BGCOLOR) # erase piece
                spot.shape = None # reset shape and color
                spot.color = None
                spot.remove = False # done removing
                pygame.draw.circle(spot.image, SADDLEBROWN, (BOXSIZE // 2, BOXSIZE // 2), BOXSIZE // 3) # redraw circle pit
                updateScore(1) # increase score by 1
                
def checkForScore(shape, color):
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH):
            checkVertical(shape, x, y)
            checkVertical(color, x, y)
            checkHorizontal(color, x, y)
            checkHorizontal(shape, x, y)
            checkDiagonal(color, x, y)
            checkDiagonal(shape, x, y)

def updateScore(score):
    if playerIndicator.getText() == 'Player 1 Turn':
        p1Score.setText(str(int(p1Score.getText()) + score))
    else:
        p2Score.setText(str(int(p2Score.getText()) + score))
        
        
def checkHorizontal(value, x, y):
    row = y
    col = x
    while (col >= 0):
        spot = board[row][col]
        if (spot.shape == value or spot.color == value):
            col -= 1
        else:
            break
    if (x - col >= 3): # three in a row!
        col += 1
        while (col <= x):
            board[row][col].remove = True
            col += 1
        
def checkVertical(value, x, y):
    row = y
    col = x
    while (row >= 0):
        spot = board[row][col]
        if (spot.shape == value or spot.color == value):
            row -= 1
        else:
            break
    if (y - row >= 3): # three in a row!
        row += 1
        while (row <= y):
            board[row][col].remove = True
            row += 1
            
def checkDiagonal(value, x, y):
    # check up left
    row = y
    col = x
    while (row >= 0 and col >= 0):
        spot = board[row][col]
        if (spot.shape == value or spot.color == value):
            row -= 1
            col -= 1
        else:
            break
    if (y - row >= 3): # three in a row!
        row += 1
        col += 1
        while (row <= y):
            board[row][col].remove = True
            row += 1
            col += 1

    # check up right
    row = y
    col = x
    while (row >= 0 and col < BOARDWIDTH):
        spot = board[row][col]
        if (spot.shape == value or spot.color == value):
            row -= 1
            col += 1
        else:
            break
    if (y - row >= 3): # three in a row!
        row += 1
        col -= 1
        while (row <= y):
            board[row][col].remove = True
            row += 1
            col -= 1

def draw():
    screen.fill(BGCOLOR)
    drawSidePieces()
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            spot = board[row][col]
            screen.blit(spot.image, spot.rect)
    pygame.draw.line(screen, BLACK, (BOARDWIDTH * BOXSIZE - 2, 0), (BOARDWIDTH * BOXSIZE - 2, HEIGHT - BOXSIZE // 2))
    p1Score.writeText(BOXSIZE, HEIGHT - BOXSIZE // 3)
    p2Score.writeText(WIDTH - BOXSIZE, HEIGHT - BOXSIZE // 3)
    if playerIndicator.getText() == 'Player 1 Turn':
        playerIndicator.color = CYAN
    elif playerIndicator.getText() == 'Player 2 Turn':
        playerIndicator.color = ORANGE
    playerIndicator.writeText(WIDTH // 5 * 2, HEIGHT - BOXSIZE // 3)
    pygame.display.update()

def drawSidePieces():
    for piece in pieces:
        screen.blit(piece.image, piece.rect)
        if piece.selected == True:
            pygame.draw.rect(screen, YELLOW, piece.rect, width = 1)
        
def initBoard():
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            spot = pygame.sprite.Sprite()
            spot.image = pygame.Surface((BOXSIZE, BOXSIZE))
            spot.image.fill(BGCOLOR)
            spot.shape = None
            spot.color = None
            spot.remove = False # set to True if needs to be removed from board after scoring
            pygame.draw.circle(spot.image, SADDLEBROWN, (BOXSIZE // 2, BOXSIZE // 2), BOXSIZE // 3)
            spot.rect = pygame.Rect(col * BOXSIZE, row * BOXSIZE, BOXSIZE, BOXSIZE)
            board[row][col] = spot

def makePieces():
    x = BOARDWIDTH * BOXSIZE
    y = 0
    shapeSize = BOXSIZE // 2
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            piece = pygame.sprite.Sprite()
            piece.image = pygame.Surface((BOXSIZE, BOXSIZE), pygame.SRCALPHA, 32)
            piece.image.convert_alpha()
            #piece.image.fill(BGCOLOR)
            piece.rect = pygame.Rect(x, y, BOXSIZE, BOXSIZE)
            piece.selected = False
            piece.color = color
            piece.shape = shape
            if shape == SQUARE:
                rect = pygame.Rect(BOXSIZE // 2 - shapeSize // 3,
                                   BOXSIZE // 2 - shapeSize // 3,
                                   shapeSize * 2//3, shapeSize*2//3)
                pygame.draw.rect(piece.image, color, rect)
            elif shape == STAR:
                s = BOXSIZE // 4
                shift = BOXSIZE // 4
                starPoints = [[.825 * s + shift, .755 * s+ shift],
                              [s+ shift, .1 * s+ shift],
                              [1.175 * s+ shift, .755 * s+ shift],
                              [1.855 * s+ shift, .72 * s+ shift],
                              [1.285 * s+ shift, 1.095 * s+ shift],
                              [1.53 * s+ shift, 1.73 * s+ shift],
                              [s+ shift, 1.3 * s+ shift],
                              [.47 * s+ shift, 1.73 * s+ shift],
                              [.715 * s+ shift, 1.095 * s+ shift],
                              [.145 * s+ shift, .72 * s+ shift]]
                pygame.draw.polygon(piece.image, color, starPoints)
            elif shape == CIRCLE:
                pygame.draw.circle(piece.image, color, (BOXSIZE // 2, BOXSIZE // 2), shapeSize // 3, width = shapeSize // 8)
            pieces.append(piece)
            x += BOXSIZE
            if x >= WIDTH:
                x = BOARDWIDTH * BOXSIZE
                y += BOXSIZE
def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                onMousePress(event.pos[0], event.pos[1])
        clock.tick(FPS)


pygame.init()
initBoard()
makePieces()                                     
mainloop()