####################################################
# An attempt to explore the capabilities of pyGame #
# for pyweek									   #
####################################################

import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Mattvader')



class ColorPicker:
    """Docs, docs, docs"""

    # set up the colors
    BLACK = (0,0,0)
    LIGHT_BLACK = (50,50,50)
    GREY = (200,200,200)
    WHITE = (255,255,255)

    def __init__(self):
        self.data = []

colorpicker = ColorPicker()

    
def player():
    PLAYER = pygame.Rect(300,100,50,50)
    pygame.draw.rect(windowSurface, colorpicker.BLACK, PLAYER)
    	
# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(colorpicker.WHITE)

    player()

    pygame.display.update()
    mainClock.tick(40)