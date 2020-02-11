#<imports>
import pygame
from pygame.locals import *
import time
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
#</per program variables>
#<main loop>
while True:
    screen.fill(background_color)
    #<event handling>
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #<exit>
            if event.key == K_ESCAPE:
                quit_game()
            #</exit>
    #</event handling>
    #<draw to screen>
    #</draw to screen>
    #<display update>
    pygame.display.update()
    fps = clock.get_fps()
    time_passed = clock.tick(fps)
    #</display update>
#</main loop>
