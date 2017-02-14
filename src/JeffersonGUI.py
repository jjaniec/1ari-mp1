import pygame, sys
from pygame.locals import *

pygame.init()

def displayCylinder(mySurface, cylinder, i):
    RED = (255,0,0)
    fontObj = pygame.font.Font('Roboto-Light.ttf', 16)
    for n in range(len(cylinder.get(i))):
        texteSurface = fontObj.render(cylinder.get(i)[n], True, RED)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (30 + 20 * i, 20 + 20 *n)
        mySurface.blit(texteSurface, texteRect)

def displayCylinders(mySurface, cylinder):
    for i in range(1, len(cylinder) + 1):
        displayCylinder(mySurface, cylinder, i)
        pygame.display.update()

def enterKey(mySurface,n):
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    k = 1
    key = []
    fontObj = pygame.font.Font('Roboto-Thin.ttf',14)
    displaykey(RED,fontObj, n, mySurface)
    inProgress = True
    while inProgress:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                X, Y = event.pos
                for i in range(1,n+1):
                    if X > 30+20*i and X < 50+20*i and Y > 560 and Y < 580 :
                        pygame.draw.rect(mySurface, BLACK, (30+20*i, 560, 20, 20))
                        texteSurface = fontObj.render(str(i), True,WHITE)
                        texteRect = texteSurface.get_rect()
                        texteRect.topleft = (30 + 20 * i, 560)
                        mySurface.blit(texteSurface, texteRect)

                        if i not in key :
                            key += [i]
                            texteSurface = fontObj.render(str(i), True, RED)
                            texteRect = texteSurface.get_rect()
                            texteRect.topleft = (30 + 20 * k, 580)
                            mySurface.blit(texteSurface, texteRect)
                            k += 1
                        if len(key) == n :
                            return key
                        pygame.display.update()

            if event.type == QUIT:
                inProgress = False

def displaykey(RED,fontObj,n,mySurface):
    for i in range(1,n+1):
        texteSurface = fontObj.render(str(i) ,True, RED)
        texteRect = texteSurface.get_rect()
        texteRect.topleft = (30+20*i, 560)
        mySurface.blit(texteSurface, texteRect)
    texteSurface = fontObj.render('ENTER KEY', True, RED)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (80 + 20 * i , 560)
    print("i : " + str(i))
    mySurface.blit(texteSurface, texteRect)
    pygame.display.update()

jeffersonGUI()
