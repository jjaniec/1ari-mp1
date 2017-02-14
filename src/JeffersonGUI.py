import pygame, sys
from pygame.locals import *

pygame.init()

def displayCylinder(mySurface,cylinder,i):
    RED = (255,0,0)
    fontObj = pygame.font.Font('Roboto-Light.ttf',16)
    for n in range(len(cylinder.get(i))):
        #print(cylinder.get(i)[n])
        texteSurface = fontObj.render(cylinder.get(i)[n], True, RED)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (30+20*i, 20+20*n)
        mySurface.blit(texteSurface, texteRect)


jeffersonGUI()
