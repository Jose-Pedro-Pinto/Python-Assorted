import pygame
from pygame.locals import *
from sys import exit
from random import *
import time
def colorblend(icolor,fcolor):
    deltar = icolor[0]-fcolor[0]
    deltag = icolor[1]-fcolor[1]
    deltab = icolor[2]-fcolor[2]
    icolor=(icolor[0]-deltar*0.005,icolor[1]-deltag*0.005,icolor[2]-deltab*0.005)
    if (deltar<=20 and deltag<=20 and deltab<=20):
        return icolor,randcolor()
    return icolor,fcolor
def randcolor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)
def run():
    pygame.init()
    screen = pygame.display.set_mode((1920,1080),FULLSCREEN,32)
    icolor = (0,0,0)
    fcolor = randcolor()
    screen.fill(icolor)
    while True:
        icolor,fcolor = colorblend(icolor,fcolor)
        screen.fill(icolor)
        pygame.display.update()
        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    screen=pygame.display.set_mode((1,1),NOFRAME,32)
                    return True
if __name__ == '__main__':
    run()
