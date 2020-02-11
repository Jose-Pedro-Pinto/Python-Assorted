import pygame
from pygame.locals import *
class button(object):
    def __init__(self,screen,
                 pos,size,
                 iddleColor=(0,0,0),hoverColor=(0,0,0),pressedColor=(0,0,0),
                 iddleBorderColor=(0,0,0),hoverBorderColor=(0,0,0),pressedBorderColor=(0,0,0),
                 borderWidth=5,
                 image=None,
                 triggerFuncion=None,
                 held=False):
        self.screen=screen
        self.pos=pos
        self.size=size
        self.iddleImage=self.createImage(size,iddleColor,iddleBorderColor,borderWidth,image)
        self.hoverImage=self.createImage(size,hoverColor,hoverBorderColor,borderWidth,image)
        self.pressedImage=self.createImage(size,pressedColor,pressedBorderColor,borderWidth,image)
        self.image=self.iddleImage
        self.trigger=triggerFuncion
        self.held=held
    def createImage(self,size,color,borderColor,borderWidth,image):
        buttonImage=pygame.surface.Surface(size)
        buttonImage.fill(borderColor)
        if image:
            image=pygame.transform.scale(image,(size[0]-2*borderWidth,size[1]-2*borderWidth))
            buttonImage.blit(image,(borderWidth,borderWidth))
        else:
            pygame.draw.rect(buttonImage,color,Rect(borderWidth,borderWidth,size[0]-2*borderWidth,size[1]-2*borderWidth))
        return buttonImage
    def __str__(self):
        return "bacon"
    def hovered(self):
        x,y = pygame.mouse.get_pos()
        if x>self.pos[0] and x<self.pos[0]+self.size[0] and y>self.pos[1] and y<self.pos[1]+self.size[1]:
            self.image=self.hoverImage
            return True
        else:
            self.image=self.iddleImage
            return False
    def pressed(self):
        if self.hovered():
            if self.held:
                if not pygame.mouse.get_pressed()[0]:
                    self.held=False
                    return True
            if pygame.mouse.get_pressed()[0]:
                self.held=True
                self.image=self.pressedImage
        else:
            self.held=False
        return False
    def stdOperation(self):
        result=None
        if self.pressed():
                result=self.press()
        self.draw()
        return result
    def press(self):
        result=None
        if self.trigger:
            result=self.trigger()
        return result
    def draw(self):
        self.screen.blit(self.image,self.pos)
def run():
    def randomButton():
        def randomColor():
            return (randint(0,255),randint(0,255),randint(0,255))
        from random import randint
        buttonsize=(200,100)
        newButton= button(screen,pos=(randint(0,screen_size[0]-buttonsize[0]),randint(0,screen_size[1]-buttonsize[1])),size=buttonsize,
                              iddleColor=randomColor(),hoverColor=randomColor(),pressedColor=randomColor(),
                              iddleBorderColor=randomColor(),hoverBorderColor=randomColor(),pressedBorderColor=randomColor(),
                              triggerFuncion=randomButton)
        return newButton
    pygame.init()
    screen_size = (1920,1080)
    screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
    screen.fill((25,250,52))
    buttons = []
    buttons.append(button(screen,
                          pos=(200,200),size=(200,100),
                          iddleColor=(255,0,0),hoverColor=(0,255,0),pressedColor=(0,0,255),
                          iddleBorderColor=(50,0,0),hoverBorderColor=(0,100,0),pressedBorderColor=(200,0,0),
                          triggerFuncion=randomButton,
                          image=pygame.image.load("images/brick.png").convert()))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                screen = pygame.display.set_mode((1,1),NOFRAME,32)
                return True
        for buttoni in buttons:
            temp=buttoni.stdOperation()
            if temp:
                buttons.append(temp)
        pygame.display.update()
if __name__ == '__main__':
    run()
