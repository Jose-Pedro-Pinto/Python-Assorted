#<imports>
import pygame
from pygame.locals import *
import time
import math
import random
import os
#</imports>
#<screen>
pygame.init()
screen_size = (1920,1080)
screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
screen.fill((0,123,123))
#</screen>
#<functions>
def quit_game():
    screen=pygame.display.set_mode((1,1),NOFRAME,0)
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)
def create_enemy(pos,size,base_speed=1,speed_scalling=1,base_hp=1,hp_scalling=1,base_dmg=1,dmg_scalling=1,diff=1,max_diff=20,splatter=None):
    hp=base_hp*(1+diff*hp_scalling)
    speed=base_speed*(1+diff*speed_scalling)
    dmg=base_dmg*(1+diff*dmg_scalling)
    return enemy(pos,size,speed,hp,dmg,diff,max_diff,splatter)
def create_player(player_image,bullet_image):
    player_image=pygame.image.load(player_image).convert_alpha()
    player_bullet=pygame.image.load(bullet_image).convert_alpha()
    player_i_pos=Vector2(screen_size[0]//2,screen_size[1]//2)
    player_middle=Vector2(player_image.get_height()//2,player_image.get_height()//2)
    return player(player_i_pos,player_image,player_bullet,middle = player_middle,bullet_speed=1)
def loss(pos):
    pygame.display.update()
    font=pygame.font.SysFont("arial",170)
    h=font.get_linesize()
    script_dir = os.path.dirname(__file__)
    death=pygame.image.load(os.path.join(script_dir, "images/death.png"))
    screen.blit(death,(pos.x-death.get_width()//2,pos.y-death.get_height()//2))
    screen.blit(font.render("GAME OVER",True,(255,0,255)),(1920-1500,(1080-h)//2))
    font=pygame.font.SysFont("arial",20)
    screen.blit(font.render("Press 'Esc' to exit",True,(255,0,255)),(1920-1500,(1080+h)//2))
    pygame.display.update()
    while True:
        #Waiting until you press escape
        event=pygame.event.wait()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                quit_game()
                return True
def win(pos):
    pygame.display.update()
    font=pygame.font.SysFont("arial",105)
    h=font.get_linesize()
    script_dir = os.path.dirname(__file__)
    win=pygame.image.load(os.path.join(script_dir, "images/win.png"))
    screen.blit(win,(screen_size[0]//2-win.get_width()//2,screen_size[1]//2-win.get_height()//2))
    screen.blit(font.render("CONGRATULATIONS YOU HAVE WON!",True,(255,255,0)),(0,(1080-h)//2))
    font=pygame.font.SysFont("arial",20)
    screen.blit(font.render("Press 'Esc' to exit",True,(255,255,0)),(1920-1500,(1080+h)//2))
    pygame.display.update()
    while True:
        #Waiting until you press escape
        event=pygame.event.wait()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                quit_game()
                return True
def add_enemys(enemys,dificulty,max_diff,splatter):
    for temp in range(dificulty):
        l=random.randint(0,3)
        if l==0:
            pos=Vector2(random.randint(0,screen_size[0]-50),0)
        if l==1:
            pos=Vector2(random.randint(0,screen_size[0]-50),screen_size[1]-50)
        if l==2:
            pos=Vector2(0,random.randint(0,screen_size[1]-50))
        if l==3:
            pos=Vector2(screen_size[0]-50,random.randint(0,screen_size[1]-50))
        enemys.append(create_enemy(pos,Vector2(50,50),diff=dificulty,max_diff=max_diff,splatter=splatter,base_speed=0.1,speed_scalling=0.1,hp_scalling=0.1))

    return enemys
def hit(bullets,enemys,screen,background,time_passed):
    for i in range(len(bullets)):
        for j in range(len(enemys)):
            if(bullets[i].hit(enemys[j],time_passed)):
                if not enemys[j].alive:
                    if enemys[j].splatter:
                        k=random.randint(0,len(enemys[j].splatter)-1)
                        x,y=enemys[j].splatter[k].get_size()
                        temp=enemys[j].pos+enemys[j].size/2
                        background.blit(enemys[j].splatter[k],(temp.x-x//2,temp.y-y//2))
                    del enemys[j]
                del bullets[i]
                return (bullets,enemys)
        if bullets[i].draw(screen):
            bullets[i].move(time_passed)
        else:
            del(bullets[i])
            return (bullets,enemys)
    return (bullets,enemys)
def handle_input():
    pause=False
    p=1
    while p!=0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                #<exit>
                if event.key == K_ESCAPE:
                    quit_game()
                    return True
                if event.key == K_p:
                    pause = not pause
                #</exit>
        if not pause:
            p-=1
        else:
            clock.tick(10)
def draw(screen,enemys,bullets,player,crosshair,default_mouse=False,draw_player=True,draw_enemys=True,draw_hitbox=False):
    mousePos=pygame.mouse.get_pos()
    if not default_mouse:
        screen.blit(crosshair,(mousePos[0]-crosshair.get_width()//2,mousePos[1]-crosshair.get_height()//2))
    if draw_enemys:
        for enemy1 in enemys:
            enemy1.draw(screen)
    if draw_player:
        player.draw(screen)
    if draw_hitbox:
        player.hitbox.draw(screen)
        for x in enemys:
            x.hitbox.draw(screen)
        for x in bullets:
            x.hitbox.draw(screen)
def draw_text(screen,clock,font_color,diff,n_enemys,max_lvls):
    font=pygame.font.SysFont("arial",20)
    screen.blit(font.render("fps:"+str(int(clock.get_fps())),True,font_color),(0,0))
    screen.blit(font.render("lvl:"+str(diff)+"/"+str(max_lvls),True,font_color),(0,20))
    screen.blit(font.render("enemies remaining:"+str(n_enemys),True,font_color),(0,35))
#</functions>
def run():
    #<variables>
    clock = pygame.time.Clock()
    time_passed = 0
    fps = 60
    #</variables>
    #<per program variables>
    #images and player
    script_dir = os.path.dirname(__file__)
    player = create_player(os.path.join(script_dir, "images/player.png"),os.path.join(script_dir, "images/bullet.png"))
    crosshair=pygame.image.load(os.path.join(script_dir, "images/crosshair.png")).convert_alpha()
    enemy_splatters=[]
    for x in range(6):
        enemy_splatters.append(pygame.image.load(os.path.join(script_dir, "images/Splatter"+str(x)+".png")).convert_alpha())
    #<background>
    tile = pygame.image.load(os.path.join(script_dir, "images/tile.png")).convert()
    background=pygame.surface.Surface(screen_size).convert()
    #background_color = (0,123,123)
    #background.fill(background_color)
    x,y=tile.get_size()
    w,z=background.get_size()
    for i in range(int(w/x+1)):
        for j in range(int(z/y+1)):
            background.blit(tile,(x*i,y*j))
    #</background>
    #entity lists
    enemys = []
    bullets= []
    #lvls
    diff=0
    max_lvls=20
    #stuff
    shot_time=0
    font_color=(0,0,0)
    #what to draw
    draw_hitbox=False
    draw_player=True
    draw_enemys=True
    default_mouse=False
    #</per program variables>
    pygame.mouse.set_visible(default_mouse)
    #<main loop>
    while True:
        #end game and lvl up
        if not player.alive:
            loss(player.middle)
            return True
        if len(enemys)==0:
            diff+=1
            if diff>max_lvls:
                win(player.middle)
                return True
            #lvl up
            enemys=add_enemys(enemys,diff,max_lvls,enemy_splatters)
        #background
        screen.blit(background,(0,0))
        #<event handling>
        temp=pygame.mouse.get_pos()
        if handle_input():
            return True
        shot_time+=time_passed
        if pygame.mouse.get_pressed()[0] and shot_time>0:
            x=player.shoot(shot_time)
            if x is not None:
                shot_time=0
                bullets.append(x)
        #</event handling>
        #<moving entities>
        for enemy1 in enemys:
            enemy1.move_to(player,enemys,time_passed)
        player.move(time_passed,screen)
        player.mouse_rotate()
        bullets,enemys = hit(bullets,enemys,screen,background,time_passed)
        #</moving entities>
        #<draw to screen>
        draw(screen,enemys,bullets,player,crosshair,default_mouse,draw_player,draw_enemys,draw_hitbox)
        draw_text(screen,clock,font_color,diff,len(enemys),max_lvls)
        #</draw to screen>
        #<display update>
        pygame.display.update()
        time_passed = clock.tick(fps)
        #</display update>
    #</main loop>
if __name__ == '__main__':
    from code.vector2 import Vector2
    from code.player import player
    from code.enemy import enemy
    run()
else:
    from .code.vector2 import Vector2
    from .code.player import player
    from .code.enemy import enemy
