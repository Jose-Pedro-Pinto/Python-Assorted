#Imports
import pygame
import random
from pygame.locals import *
from sys import exit
import os
pygame.init()
#game over screen
def loss(screen,x,y,size):
    font=pygame.font.SysFont("arial",170)
    h=font.get_linesize()
    script_dir = os.path.dirname(__file__)
    death=pygame.image.load(os.path.join(script_dir,"death.png"))
    screen.blit(death,(x-death.get_width()//2,y-death.get_height()//2))
    screen.blit(font.render("GAME OVER",True,(255,0,0)),(size[0]-1500,(size[1]-h)//2))
    font=pygame.font.SysFont("arial",20)
    screen.blit(font.render("Press 'Esc' to exit",True,(255,0,0)),(size[0]-1500,(size[1]+h)//2))
    pygame.display.update()
    while True:
        #Waiting until you press escape
        event=pygame.event.wait()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                return
def run():
    #Loading Images
    script_dir = os.path.dirname(__file__)
    coin=pygame.image.load(os.path.join(script_dir, "coin.png"))
    player=pygame.image.load(os.path.join(script_dir, "square.png"))
    enemy=pygame.image.load(os.path.join(script_dir, "danger.png"))
    trail=pygame.image.load(os.path.join(script_dir, "trail.png"))
    jump=pygame.image.load(os.path.join(script_dir, "jump.png"))
    floater=pygame.image.load(os.path.join(script_dir, "Floater.png"))
    #Font on screen
    font=pygame.font.SysFont("arial",50)
    #screen setup
    size=(1920,1080)
    screen=pygame.display.set_mode(size,FULLSCREEN,32)
    #initialization of variables
    x=0
    y=size[1]-player.get_height()
    mx=0
    my=0
    vy=0
    score=0
    x1=random.randint(coin.get_width(),size[0]-coin.get_width())
    y1=random.randint(coin.get_height(),size[1]-coin.get_height())
    x2=[]
    y2=[]
    x3=[]
    y3=[]
    x4=[]
    y4=[]
    x5=[]
    y5=[]
    time=[]
    FullScreen=True
    #Main game cycle
    while True:
        #Input handling
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    screen=pygame.display.set_mode((1,1),NOFRAME,32)
                    return True
                if event.key == K_f:
                    FullScreen = not FullScreen
                    if FullScreen:
                        screen=pygame.display.set_mode(size,DOUBLEBUF | FULLSCREEN | HWSURFACE,32)
                    else:
                        screen=pygame.display.set_mode(size,0,32)
                if event.key == K_a:
                    mx-=5
                elif event.key == K_d:
                    mx+=5
                elif event.key == K_w:
                    my=5
                    #Creating jump clouds
                    if y!=size[1]-player.get_height():
                        time.append(100)
                        x4.append(x+player.get_width()//2-jump.get_height()//2)
                        y4.append(y+player.get_width()//2-jump.get_height()//2)
            elif event.type == KEYUP:
                if event.key == K_a:
                    mx+=5
                elif event.key == K_d:
                    mx-=5
        #Preventing out of borders
        if y-my>=size[1]-player.get_height():
            y=size[1]-player.get_height()
            my=0
        elif y-my<0:
            y=0
            my=-0.2*my
        else:
            y-=my
            my-=0.1
        if x+mx<0:
            x=0
        elif x+mx>size[0]-player.get_width():
            x=size[0]-player.get_width()
        else:
            x+=mx
        #Score
        if (x+player.get_width()//2-x1-coin.get_width()//2)**2+(y+player.get_width()//2-y1-coin.get_width()//2)**2<=(coin.get_width()//1.5)**2:
            score+=1
            #new coin
            x1=random.randint(coin.get_width(),size[0]-coin.get_width())
            y1=random.randint(coin.get_height(),size[1]-coin.get_height())
            #Still enemies
            if len(x2)<20:
                x2.append(random.randint(coin.get_width(),size[0]-coin.get_width()))
                y2.append(random.randint(coin.get_height(),size[1]-coin.get_height()))
            #Moving enemies
            else:
                x5.append(random.randint(coin.get_width(),size[0]-coin.get_width()))
                y5.append(random.randint(coin.get_height(),size[1]-coin.get_height()))
        #creating trail
        x3.append(x+player.get_width()//2-trail.get_height()//2)
        y3.append(y+player.get_width()//2-trail.get_height()//2)
        if len(x3)>30:
            del x3[0]
            del y3[0]
        #creating image on screen
        screen.fill((0,255,255))
        k=0
        #placing jump clouds
        for i in x4:
            screen.blit(jump,(x4[k],y4[k]))
            time[k]-=1
            if time[k]<=0:
                del x4[k]
                del y4[k]
                del time[k]
            k+=1
        k=0
        #placing trail
        for i in x3:
            screen.blit(trail,(x3[k],y3[k]))
            k+=1
        #placing coins and player
        screen.blit(coin,(x1,y1))
        screen.blit(player,(x,y))
        scores="score:"+str(score)
        #scoreboard
        screen.blit(font.render(scores,True,(255,0,0)),(0,0))
        k=0
        #placing enemies
        for i in x2:
            screen.blit(enemy,(x2[k],y2[k]))
            k+=1
        k=0
        for i in x5:
            screen.blit(floater,(x5[k],y5[k]))
            if x5[k]<x:
                x5[k]+=score/20
            elif x5[k]>x:
                x5[k]-=score/20
            if y5[k]<y:
                y5[k]+=score/20
            elif y5[k]>y:
                y5[k]-=score/20
            k+=1
        #game over screen
        k=0
        for i in x2:
            #Still enemies hitbox
            if (x+player.get_width()//2-x2[k]-coin.get_width()//2)**2+(y+player.get_width()//2-y2[k]-coin.get_width()//2)**2<=(coin.get_width()//1.3)**2:
                loss(screen,x,y,size)
                return True
            k+=1
        k=0
        for i in x5:
            #Moving enemies hitbox
            if (x+player.get_width()//2-x5[k]-coin.get_width()//2)**2+(y+player.get_width()//2-y5[k]-coin.get_width()//2)**2<=(coin.get_width()//1.3)**2:
                loss(screen,x,y,size)
                return True
            k+=1
        #updating screen with the new info
        if FullScreen:
            pygame.display.flip()
        else:
            pygame.display.update()
if __name__ == '__main__':
    run()
