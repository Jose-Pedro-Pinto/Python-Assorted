#<imports>
import pygame
from pygame.locals import *
import time
import os
#</imports>
def run():
    #<screen>
    pygame.init()
    screen_size = (1920,1080)
    screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
    script_dir = os.path.dirname(__file__)
    background = pygame.image.load(os.path.join(script_dir, "Background.png")).convert()
    screen.blit(background,(0,0))
    #</per program variables>
    #<main loop>
    while True:
        for event in pygame.event.get():
            pass
        pygame.display.update()
        time.sleep(1)
        screen.blit(background,(0,0))
        #</display update>
#</main loop>
if __name__=='__main__':
    run()
