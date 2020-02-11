from .entity import entity
from .poligon import *
import random
class enemy(entity):
    def __init__(self,pos,size,speed=0.1,hp=2,dmg=1,diff=1,max_diff=20,splatter=None):
        super(enemy,self).__init__(pos,dmg=dmg,speed=speed,hp=hp,size=size)
        #diff
        self.max_diff=max_diff
        self.diff=diff
        #enemy_splatter
        self.splatter=splatter
        #hitbox
        rand=random.randint(0,10)
        if rand<=9:
            self.hitbox = rect_to_pol(self.pos,self.size)
            self.shape="rectangle"
        if rand>9:
            self.hitbox = circle_to_pol((self.pos+self.size/2),self.size.x//2,10)
            self.shape="circle"
    def __str__():
        return "%s, %s, %s"%(self.speed,self.hp,self.dmg)
    def draw(self,screen):
        temp=(self.current_hp/self.base_hp)*(self.diff/self.max_diff)*255
        if self.shape=="rectangle":
            pygame.draw.rect(screen,(255-temp,0,0),(self.pos.x,self.pos.y,self.size.x,self.size.y))
        elif self.shape=="circle":
            temp2=(self.pos+self.size/2)
            pygame.draw.circle(screen,(255-temp,0,0),(int(temp2.x),int(temp2.y)),self.size.x//2)
    def move_to(self,enemy,others,time_passed):
        v=enemy.middle-self.pos
        v.normalize()
        v*=self.speed*time_passed
        temp = (self.size+v.abs()).get_magnitude()+100
        if (enemy.pos-self.pos).get_magnitude()<temp:
            mag = self.hitbox.colide(enemy.hitbox,v)
        else:
            mag=1
        if mag<1:
            self.hit(enemy)
        v*=mag
        for other in others:
            if self.pos==other.pos or (other.pos-self.pos).get_magnitude()>temp:
                continue
            v1=self.hitbox.slide(other.hitbox,v)
            v=v1
        self.pos+=v
        self.hitbox.move(v)

