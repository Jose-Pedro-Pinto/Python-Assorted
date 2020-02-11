from pygame.locals import *
import pygame
import os
class chess_piece(object):
    def __init__(self,pos,name,image=None,team=None):
        self.alive=True
        self.pos=pos
        self.name=name
        if team:
            self.team=team
        else:
            if pos[1]>=4:
                self.team=-1
            else:
                self.team=1
        if image:
            self.image=image
        else:
            if self.team==1:
                color="black"
            else:
                color="white"
            script_dir = os.path.dirname(__file__)
            self.image=pygame.image.load(os.path.join(script_dir,"../../images/"+name+"_"+color+".png"))
    def __str__(self):
        return self.name+str(self.pos)
    def get_moves(self):
        return []
    def move(self,pos):
        self.pos=pos
    def draw(self,screen,pos):
        if self.image:
            screen.blit(self.image,pos)
        else:
            pygame.draw.circle(screen,(0,0,255),(pos[0]+60,pos[1]+60),50)
    def correct_size(self,size):
        self.image=pygame.transform.scale(self.image,size)
    def is_cheking(self,pieces,pos=None):
        if pos:
            temp=self.pos
            p=pieces[pos]
            pieces[pos]=self
            self.pos=pos
            pieces[temp]=None
        moves=self.get_moves(pieces)
        if pos:
            pieces[temp]=self
            pieces[pos]=p
            self.pos=temp
        for move in moves:
            p=pieces[move]
            if p:
                if p.name=='king' and p.team!=self.team:
                    return True
        return False
