#<imports>
import pygame
from pygame.locals import *
import time
#</imports>
#<functions>
def create_scales(size):
    red_scale_surface = pygame.surface.Surface(size)
    green_scale_surface = pygame.surface.Surface(size)
    blue_scale_surface = pygame.surface.Surface(size)
    for x in range(size[0]):
        c = int((x/size[0])*255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, size[1])
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface
#</functions>
def run():
    #<screen>
    pygame.init()
    screen_size = (1920,1080)
    screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
    backgroud = (255,255,255)
    screen.fill(backgroud)
    #</screen>
    #<variables>
    scale_size = (60,20)
    scales = create_scales(scale_size)
    #</variables>
    #<per program variables>
    lines = []
    line = []
    ptsn = 0
    color = [0,0,0]
    #</per program variables>
    #<main loop>
    while True:
        screen.fill(backgroud)
        for pts in lines:
            pygame.draw.lines(screen,pts[1],False,pts[0],2)
        if len(line)>1:
            pygame.draw.lines(screen,color,False,line,2)
        #<event handling>
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                #<exit>
                if event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((1,1),NOFRAME,32)
                    return True
                if event.key == K_c:
                    lines = []
                    line = []
                if event.key == K_s:
                    image=pygame.surface.Surface(screen_size)
                    image.blit(screen,(0,0))
                    screen = pygame.display.set_mode((1,1),NOFRAME,32)
                    image_name=input("name for the image?\n")
                    screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
                    pygame.image.save(image,image_name+".png")
                #</exit>
            if event.type == MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    line.append(event.pos)
                elif len(line)>1:
                    lines.append((line,(color[0],color[1],color[2])))
                    line = []
                else:
                    line = []
        #</event handling>
        #<draw to screen>
        for i in range(3):
            screen.blit(scales[i],(0,i*scale_size[1]))
        pygame.draw.rect(screen,color,[scale_size[0],0,scale_size[1],scale_size[1]*3])
        x, y = pygame.mouse.get_pos()
        if x<scale_size[0] and y<scale_size[1]*3:
            if pygame.mouse.get_pressed()[0]:
                for i in range(3):        
                    if y > i*scale_size[1] and y < (i+1)*scale_size[1]:
                        color[i] = int((x/(scale_size[0]))*255.)
            for i in range(3):        
                pos = ( int((color[i]/255.)*(scale_size[0])), i*scale_size[1]+scale_size[1]//2 )
                pygame.draw.circle(screen, (255, 255, 255), pos, 4)
        #</draw to screen>
        #<display update>
        pygame.display.update()
        #</display update>
    #</main loop>
if __name__=='__main__':
    run()
