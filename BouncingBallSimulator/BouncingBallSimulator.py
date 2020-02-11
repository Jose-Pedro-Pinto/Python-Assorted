import pygame
import math
import random
from pygame.locals import *
from sys import exit
import os
def run():
    p=True
    size=(1920,1080)
    screen=pygame.display.set_mode(size,DOUBLEBUF|HWSURFACE|FULLSCREEN,32)
    clock = pygame.time.Clock()
    def quit_game():
        screen=pygame.display.set_mode((1,1),NOFRAME,0)
    background = pygame.Surface(size).convert()
    script_dir = os.path.dirname(__file__)
    brick = pygame.image.load(os.path.join(script_dir,"brick.jpg")).convert()
    for i in range(size[1]//brick.get_height()+1):
        for j in range(size[0]//brick.get_width()):
            background.blit(brick,(j*brick.get_width(),i*brick.get_height()))
    while True:
        if p:
            pygame.init()
            script_dir = os.path.dirname(__file__)
            ball=pygame.image.load(os.path.join(script_dir,"Floater.png")).convert_alpha()
            font=pygame.font.SysFont("arial",16)
            x=10
            y=10
            mx=0
            my=0
            ax=0
            ay=0
            x1=[]
            y1=[]
            mx1=[]
            my1=[]
            time=[]
            acceleration = 1
            g=1
            bounciness = 0.9
            ball_duration = 500
            extra=False
            screen.fill((255,0,0))
            while True:
                if not extra:
                    screen.fill((255,0,0))
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            quit_game()
                            return True
                        if extra:
                            if event.key == K_SPACE:
                                for i in range(8):
                                    x1.append(x)
                                    y1.append(y)
                                for i in range(-1,2):
                                    for j in range(-1,2):
                                        if (i!=0 or j!=0):
                                            if (i*j!=0):
                                                mx1.append(mx+math.sqrt(9/2)*i)
                                                my1.append(my+math.sqrt(9/2)*j)
                                            else:
                                                mx1.append(mx+3*i)
                                                my1.append(my+3*j)
                                            time.append(ball_duration)
                        if event.key == K_LEFT or event.key == K_a:
                            ax-=acceleration
                        if event.key == K_RIGHT or event.key == K_d:
                            ax+=acceleration
                        if event.key == K_DOWN or event.key == K_s:
                            ay+=acceleration
                        if event.key == K_UP or event.key == K_w:
                            ay-=acceleration
                        if event.key == K_j:
                            extra = not extra
                            if extra:
                                font = pygame.font.SysFont("arial",100)
                                screen.blit(font.render("Extra Mode Activated",True,(0,255,255)),(size[0]-1500,(size[1]-font.get_linesize())//2))
                        if event.key == K_p:
                            p=not p
                    if event.type == KEYUP:
                        if event.key == K_LEFT or event.key == K_a:
                            ax+=acceleration
                        if event.key == K_RIGHT or event.key == K_d:
                            ax-=acceleration
                        if event.key == K_DOWN or event.key == K_s:
                            ay-=acceleration
                        if event.key == K_UP or event.key == K_w:
                            ay+=acceleration
                mx+=ax
                my+=ay
                if y+my>size[1]-ball.get_height():
                    y=size[1]-ball.get_height()
                    my=-bounciness*my
                    mx=bounciness*mx
                elif y+my<0:
                    y=0
                    my=-bounciness*my
                    mx=bounciness*mx
                else:
                    y+=my
                    my+=ay
                if x+mx>size[0]-ball.get_width():
                    x=size[0]-ball.get_width()
                    mx=-bounciness*mx
                    my=bounciness*my
                elif x+mx<0:
                    x=0
                    mx=-bounciness*mx
                    my=bounciness*my
                else:
                    x+=mx
                    mx+=ax
                my+=g
                for i in range(len(y1)):
                    if i>=len(y1):
                        break
                    if y1[i]+my1[i]>size[1]-ball.get_height():
                        y1[i]=size[1]-ball.get_height()
                        my1[i]=-bounciness*my1[i]
                        mx1[i]=bounciness*mx1[i]
                    elif y1[i]+my1[i]<0:
                        y1[i]=0
                        my1[i]=-bounciness*my1[i]
                        mx1[i]=bounciness*mx1[i]
                    else:
                        y1[i]+=my1[i]
                    if x1[i]+mx1[i]>size[0]-ball.get_width():
                        x1[i]=size[0]-ball.get_width()
                        mx1[i]=-bounciness*mx1[i]
                        my1[i]=bounciness*my1[i]
                    elif x1[i]+mx1[i]<0:
                        x1[i]=0
                        mx1[i]=-bounciness*mx1[i]
                        my1[i]=bounciness*my1[i]
                    else:
                        x1[i]+=mx1[i]
                    my1[i]+=g
                    screen.blit(ball,(x1[i],y1[i]))
                    time[i]-=1
                    if time[i]==0:
                        del time[i]
                        del mx1[i]
                        del my1[i]
                        del x1[i]
                        del y1[i]
                screen.blit(ball,(x,y))
                clock.tick(60)
                pygame.display.update()
                if not p:
                    break
        else:
            n=False
            pygame.init()
            font_color = (0,0,255)
            def elipse_circle_hitbox(pos1,width,height,pos2):
                if (pos2[0]-pos1[0])**2/width**2 + (pos2[1]-pos1[1])**2/height**2 <= 1:
                    return True
                else:
                    return False
            def blit_alpha(target, source, location, opacity):
                x = location[0]
                y = location[1]
                temp = pygame.Surface((source.get_width(), source.get_height())).convert()
                temp.blit(target, (-x, -y))
                temp.blit(source, (0, 0))
                temp.set_alpha(opacity)        
                target.blit(temp, location)
            #game over screen
            def loss():
                font=pygame.font.SysFont("arial",170)
                h=font.get_linesize()
                screen.blit(death,(x+96-death.get_width()//2,y+32-death.get_height()//2))
                screen.blit(font.render("GAME OVER",True,font_color),(size[0]-1500,(size[1]-h)//2))
                font=pygame.font.SysFont("arial",20)
                screen.blit(font.render("Press 'Esc' to exit or 'R' to retry",True,font_color),(size[0]-1500,(size[1]+h)//2))
                pygame.display.update()
                while True:
                    #Waiting until you press escape
                    event=pygame.event.wait()
                    if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                            quit_game()
                            return "exit"
                        if event.key==K_p:
                            return True
                        if event.key==K_r:
                            return False
            #Loading Images
            script_dir = os.path.dirname(__file__)
            coin=pygame.image.load(os.path.join(script_dir,"coin2.png")).convert_alpha()
            player=pygame.image.load(os.path.join(script_dir,"mario.png")).convert_alpha()
            enemy=pygame.image.load(os.path.join(script_dir,"Spike.png")).convert_alpha()
            death=pygame.image.load(os.path.join(script_dir,"death.png")).convert_alpha()
            jump=pygame.image.load(os.path.join(script_dir,"jump.png")).convert_alpha()
            floater=pygame.image.load(os.path.join(script_dir,"Skull.png")).convert_alpha()
            #Font on screen
            font=pygame.font.SysFont("arial",50)
            #initialization of variables
            x=0
            y=size[1]-player.get_height()
            mx=0
            my=0
            score=0
            g=-1
            acceleration = 15
            pos1=[random.randint(coin.get_width(),size[0]-coin.get_width()),random.randint(coin.get_height(),size[1]-coin.get_height())]
            pos2=[]
            pos4=[]
            pos5=[]
            time=[]
            replay=[]
            rposx=x
            rposy=y
            sprite=2
            spriteaux=0
            cloud_duration=200
            FullScreen=True
            replaying=False
            #Main game cycle
            while True:  
                #Input handling
                if replaying and len(replay)==0:
                    replaying=False
                elif replaying:
                    eventList=replay.pop(0)
                else:
                    eventList=pygame.event.get()
                    replay.append(eventList)
                for event in eventList:
                    if event.type == QUIT:
                        quit_game()
                        return True
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            quit_game()
                            return True
                        if event.key == K_r:
                            replaying=True
                            eventList=replay
                            temp=x
                            x=rposx
                            rposx=x
                            temp=y
                            y=rposy
                            rposy=temp
                            break
                        if event.key == K_f:
                            FullScreen = not FullScreen
                            if FullScreen:
                                screen=pygame.display.set_mode(size,DOUBLEBUF | FULLSCREEN | HWSURFACE,32)
                            else:
                                screen=pygame.display.set_mode(size,0,32)
                        if event.key == K_a or event.key == K_LEFT:
                            mx-=acceleration
                            spriteaux+=1
                            if spriteaux == 1:
                                sprite = 0
                            else:
                                sprite = 2
                        elif event.key == K_d or event.key == K_RIGHT:
                            mx+=acceleration
                            spriteaux+=1
                            if spriteaux == 1:
                                sprite = 1
                            else:
                                sprite = 2
                        elif event.key == K_w or event.key == K_UP:
                            my=acceleration
                            #Creating jump clouds
                            if y!=size[1]-player.get_height():
                                pos4.append([x+player.get_width()//2-jump.get_height()//2,y+player.get_height()//2-jump.get_height()//2,cloud_duration])
                        if event.key == K_p:
                            p=not p
                    elif event.type == KEYUP:
                        if event.key == K_a or event.key == K_LEFT:
                            mx+=acceleration
                            spriteaux-=1
                            if spriteaux == 0:
                                sprite = 2
                            else:
                                sprite = 1
                        elif event.key == K_d or event.key == K_RIGHT:
                            mx-=acceleration
                            spriteaux-=1
                            if spriteaux == 0:
                                sprite = 2
                            else:
                                sprite = 0
                #Preventing out of borders
                if y-my>=size[1]-player.get_height():
                    y=size[1]-player.get_height()
                    my=0
                elif y-my<0:
                    y=0
                    my=-0.2*my
                else:
                    y-=my
                    my+=g
                if x+64+mx<0:
                    x=-64
                elif x-64+mx>size[0]-player.get_width():
                    x=size[0]+64-player.get_width()
                else:
                    x+=mx
                #Score
                if elipse_circle_hitbox((x+player.get_width()//2,y+player.get_height()//2),64,player.get_height(),(pos1[0],pos1[1])):
                    score+=1
                    success = False
                    while not success:
                        success = True
                        temp1 = random.randint(coin.get_width(),size[0]-coin.get_width())
                        temp2 = random.randint(coin.get_height(),size[1]-coin.get_height())
                        if math.sqrt((temp1-x+player.get_width()//2)**2+(temp2-y+player.get_height()//2)**2) < 200:
                            success = False
                            continue
                        #Still enemies
                        elif len(pos2)<20:
                            pos2.append((temp1,temp2))
                        #Moving enemies
                        else:
                            w,h = floater.get_size()
                            pos5.append([temp1+w/2,temp2+h/2,0])
                    #new coin
                    success = False
                    while not success:
                        success = True
                        pos1[0]=random.randint(coin.get_width(),size[0]-coin.get_width())
                        pos1[1]=random.randint(coin.get_height(),size[1]-coin.get_height())
                        for pos in pos2:
                            if math.sqrt((pos[0]-pos1[0])**2+(pos[1]-pos1[1])**2) < 50:
                                success = False
                #creating background on screen
                screen.blit(background,(0,0))
                #placing jump clouds
                for pos in pos4:
                    blit_alpha(screen,jump,(pos[0],pos[1]),pos[2]/200*255)
                    pos[2]-=1
                    if pos[2]<=0:
                        del pos
                #placing coins and player
                screen.blit(coin,(pos1[0],pos1[1]))
                screen.blit(player,(x+64,y),(64*sprite,0,64,79))
                scores="score:"+str(score)
                #scoreboard
                screen.blit(font.render(scores,True,font_color),(0,0))
                #fps
                fps = int(round(clock.get_fps()))
                screen.blit(font.render("fps:"+str(fps),True,font_color),(size[0]-140,0))
                #placing enemies
                for pos in pos2:
                    screen.blit(enemy,(pos[0],pos[1]))
                for pos in pos5:
                    rotated_floater = pygame.transform.rotate(floater,pos[2])
                    w,h=rotated_floater.get_size()
                    screen.blit(rotated_floater,(pos[0]-w/2,pos[1]-h/2))
                    pos[2]+=1
                    if pos[0]<x+64:
                        pos[0]+=score/20
                    elif pos[0]>x+64:
                        pos[0]-=score/20
                    if pos[1]<y:
                        pos[1]+=score/20
                    elif pos[1]>y:
                        pos[1]-=score/20
                #game over screen
                for pos in pos2:
                    #Still enemies hitbox
                    if elipse_circle_hitbox((x+player.get_width()//2,y+player.get_height()//2),64,player.get_height(),(pos[0]+enemy.get_width()//2,pos[1]+enemy.get_height()//2)):
                        p=loss()
                        if p == "exit":
                            return True
                        n=True
                        break
                for pos in pos5:
                    #Moving enemies hitbox
                    if elipse_circle_hitbox((x+player.get_width()//2,y+player.get_height()//2),64,player.get_height(),(pos[0],pos[1])):
                        p=loss()
                        if p == "exit":
                            return True
                        n=True
                        break
                #updating screen with the new info
                clock.tick(60)
                if FullScreen:
                    pygame.display.flip()
                else:
                    pygame.display.update()
                if p or n:
                    break
if __name__ == '__main__':
    run()
