import pygame, sys
from pygame.locals import *

pygame.init()

FILEPATH    = "../Cylinder.txt"

def jeffersonGUI():
    cylinder = loadCylinder(FILEPATH)
    mySurface = pygame.display.set_mode((180 + 20 * (len(cylinder)), 650))

    pygame.display.set_caption("Jefferson's cylinders")
    displayCylinders(mySurface, cylinder)

    key = enterKey(mySurface, len(cylinder))
    newcylinder = NewCylinders(cylinder, key)
    displayNewCylinders(mySurface, newcylinder)

    if (rotateCylinders(mySurface, newcylinder) == 0):
        quit()
    for event in pygame.event.get():
         if event.type == QUIT:
            quit()

def ft_getnewlinesnb(str_):
    count = 0

    for i in range(0, len(str_)):
        if (str_[i] == '\n'):
            count += 1
    return (count)

def loadCylinder(file):
    content = open(file, "r").read()
    lines_dict = {}
    i = 0
    buf = ""

    for i in range(0, ft_getnewlinesnb(content)):
        for j in range(0, 26):
            buf += content[(i * 27) + j]
        lines_dict[i + 1] = buf
        buf = ""
    return (lines_dict)

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
    fontObj = pygame.font.Font('Roboto-Thin.ttf', 14)
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

def NewCylinders(cylinder,key):
    newCylinder = {}
    for i in range(1,len(cylinder)+1):
        newCylinder[i] = cylinder.get(key[i-1])
    return newCylinder

def displayNewCylinders(mySurface,newCylinder):
    BLACK = (0,0,0)
    pygame.draw.rect(mySurface, BLACK, (0 , 0, 600, 700))
    pygame.display.update()
    displayCylinders(mySurface,newCylinder)

def rotateCylinder(cylinder,i,up):
    rotate = cylinder.get(i)
    if up == True:
        rotate += rotate[0]
        rotate = rotate[1:27]
    else:
        rotate = rotate[25] + rotate
        rotate = rotate[:26]
    cylinder[i] = rotate
    return cylinder

def ft_print_env(mySurface, cylinder, coordsstrs):
    fontObj = pygame.font.Font('Comfortaa-Light.ttf', 14)
    textstrs = ["↑", "↓", "CLEAR", "CIPHER", "FINISH"]
    #print arrows, finish, cypher, clear
    pygame.draw.line(mySurface, (255, 0, 0), (50, 139), ((40 + 20 * (len(cylinder)), 139)))
    pygame.draw.line(mySurface, (255, 0, 0), (50, 159), ((40 + 20 * (len(cylinder)), 159)))
    pygame.draw.line(mySurface, (255, 0, 0), (50, 259), ((40 + 20 * (len(cylinder)), 259)))
    pygame.draw.line(mySurface, (255, 0, 0), (50, 279), ((40 + 20 * (len(cylinder)), 279)))
    #print separating lines
    for j in range(0, len(textstrs)):
        texteSurface = fontObj.render(textstrs[j], True, (255, 0, 0))
        texteRect = texteSurface.get_rect()
        if (j <= 1):
            for i in range(0, len(cylinder)):
                texteRect.topleft = (30 + 20 * (i + 1), coordsstrs[j][1])
                mySurface.blit(texteSurface, texteRect)
        else:
            texteRect.topleft = coordsstrs[j]
            mySurface.blit(texteSurface, texteRect)
    pygame.display.update()


def rotateCylinders(mySurface,cylinder):
    coordsstrs = [(0, 560), (0, 580),\
    (30 + 20 * (len(cylinder) + 1), 144),\
    (30 + 20 * (len(cylinder) + 1), 264),\
    (30 + 20 * (len(cylinder) + 1), 560)]
    ft_print_env(mySurface, cylinder, coordsstrs)
    while 1:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                X, Y = event.pos
                print("X : " + str(X))
                print("Y : " + str(Y))
                if (X >= 30 + 20) and (X <= 30 + 20 * (len(cylinder) + 1))\
                    and (Y > coordsstrs[0][1]) and (Y < coordsstrs[1][1] + 20):
                    print(str((X - 30) / 20))
                    print(str((Y - 560) / 20))
                    cylinder = rotateCylinder(cylinder, int((X - 30) / 20), not bool(int((Y - 560) / 20)))
                    displayNewCylinders(mySurface, cylinder)
                    print(cylinder)
                    ft_print_env(mySurface, cylinder, coordsstrs)
                if (X > 30 + 20 * (len(cylinder) + 1)) and (X <= 30 + 20 * (len(cylinder) + 1) + 45):
                    print("lol")
                    if (Y >= coordsstrs[4][1]) and (Y <= coordsstrs[4][1] + 20):
                            print("lol")
                            return (0)

    pygame.display.update()

jeffersonGUI()
