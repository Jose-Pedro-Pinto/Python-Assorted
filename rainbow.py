import pygame
from pygame.locals import *
from sys import exit
import time
def run():
    screen = pygame.display.set_mode((1,1),NOFRAME,32)
    if input("fullscreen? y/anything else\n")=="y":
        width=1920
        height=1080
        screen = pygame.display.set_mode((width,height),FULLSCREEN,32)
    else:
        width=int(input("width?\n"))
        height=int(input("height?\n"))
        screen = pygame.display.set_mode((width,height),0,32)
    ratio = float(width)/600
    val = int(ratio*256)
    rainbow = pygame.surface.Surface((width,height))
    for x in range(val):
        line = Rect(x,0,1,height)
        pygame.draw.rect(rainbow,(int(255-x/ratio),int(x/ratio),0),line)
    for x in range(val):
        line = Rect(x+val,0,1,height)
        pygame.draw.rect(rainbow,(0,int(255-x/ratio),int(x/ratio)),line)
    for x in range(width-2*val):
        line = Rect(x+val*2,0,1,height)
        pygame.draw.rect(rainbow,(int(x/ratio),0,int(255-x/ratio)),line)
    screen.blit(rainbow,(0,0))
    print("done")
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                screen = pygame.display.set_mode((1,1),NOFRAME,32)
                return True
        time.sleep(1)
if __name__=='__main__':
    run()
