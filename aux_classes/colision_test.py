#<imports>
import pygame
from pygame.locals import *
import time
from poligon import *
from semiline import line
from vector2 import Vector2
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
    exit()
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)
#</functions>
#<variables>
background_color = (0,123,123)
clock = pygame.time.Clock()
time_passed = 0
fps = 60
#</variables>
#<per program variables>
poligon1 = circle_to_pol(Vector2(51,50),50,20)
poligon2 = elipse_to_pol(Vector2(50,150),50,30,20)
poligon1.draw(screen)
poligon2.draw(screen)
#</per program variables>
#<main loop>
while True:
    screen.fill(background_color)
    poligon2.draw(screen)
    poligon1.draw(screen)
    v1=Vector2(0,0.25)*time_passed
    mag1 = poligon1.colide(poligon2,v1)
    poligon1.move(poligon1.slide(poligon2,v1))
    v2=Vector2(0,0.2)*time_passed
    poligon2.move(poligon2.slide(poligon1,v2))

    #<event handling>
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #<exit>
            if event.key == K_ESCAPE:
                quit_game()
            if event.key == K_d:
                v1.x=1
            if event.key == K_a:
                v1.x=-1
            if event.key == K_w:
                v1.y=-1
            #</exit>
    v1.y+=0.01
    #</event handling>
    #<draw to screen>
    #</draw to screen>
    #<display update>
    pygame.display.update()
    time_passed = clock.tick(fps)
    #</display update>
#</main loop>
