from button import *
import button as buttonn
import math
import pygame
from pygame.locals import *
import shoty_mcgee.gun as gun
import not_paint
import rainbow
import screen_unsaver
import Screen_locker.Screen_Locker as lock
import Flappy_Cube.FLAPPY_CUBE as flappy
import Chess.Derpy_Chess as chess
import BouncingBallSimulator.BouncingBallSimulator as bouncy
import allgames as gamelobby
def rowscols(screen_size,games,button_size):
    temp = math.sqrt(len(games))
    x = math.ceil(temp)

    if x*button_size[0]>screen_size[0]:
        x-=1
    y = math.ceil(len(games)/x)
    temp=button_size[0]*x
    temp=screen_size[0]-temp
    temp/=x+1
    offsetx=temp
    temp=button_size[1]*y
    temp=screen_size[1]-temp
    temp/=y+1
    offsety=temp
    return(x,y,offsetx,offsety)
def posbuttons(screen,games,imageNames):
    iddlecolor=(0,150,150)
    hovercolor=(0,200,200)
    pressedcolor=(0,255,255)
    button_size=(1600,800)
    while math.ceil(math.sqrt(len(games)))*button_size[0]>screen.get_size()[0] and math.ceil(math.sqrt(len(games)))*button_size[1]>screen.get_size()[1]:
        button_size=(button_size[0]//2,button_size[1]//2)
    x,y,ofsetx,ofsety = rowscols(screen.get_size(),games,button_size)
    counter=0
    buttons=[]
    images=loadImages(imageNames)
    for i in range(1,y+1):
        for j in range(1,x+1):
            if counter==len(games):
                break
            buttons.append(button(screen,
                                  (ofsetx*j+(j-1)*button_size[0],ofsety*i+(i-1)*button_size[1]),
                                  button_size,
                                  iddleBorderColor=iddlecolor,
                                  hoverBorderColor=hovercolor,
                                  pressedBorderColor=pressedcolor,
                                  triggerFuncion=games[counter].run,
                                  borderWidth=10,
                                  image=images[counter]))
            counter+=1
    return buttons
def loadImages(imageNames):
    images=[]
    for imageName in imageNames:
        if imageName:
            images.append(pygame.image.load("images/"+imageName+".png").convert())
        else:
            images.append(None)
    return images
def run():
    pygame.init()
    screen_size = (1920,1080)
    screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
    background=pygame.image.load("images/background.png").convert()
    background=pygame.transform.scale(background,screen_size)
    buttons=posbuttons(screen,
                       [gun,not_paint,rainbow,screen_unsaver,lock,flappy,chess,bouncy,buttonn,gamelobby],
                       ["gun","not_paint","rainbow","screen_unsaver","screen_locker","flappy_cube","derpy_chess","bouncy","brick","background"])
    while True:
        screen.blit(background,(0,0))
        for buttoni in buttons:
            if buttoni.stdOperation():
                pygame.mouse.set_visible(True)
                screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                screen = pygame.display.set_mode((1,1),NOFRAME,32)
                return True
if __name__ == '__main__':
    run()
