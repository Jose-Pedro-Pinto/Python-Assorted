from .entity import entity
from .vector2 import Vector2
from .poligon import *
class bullet(entity):
    def __init__(self,pos,rotation,image,speed,dmg):
        super(bullet,self).__init__(pos,rotation=rotation,image=image,dmg=dmg)
        self.vel=Vector2(speed*math.cos(math.radians(rotation)),-speed*math.sin(math.radians(rotation)))
        self.hitbox= points_to_pol([self.pos,self.pos])
    def move(self,time_passed):
        v=self.vel*time_passed
        self.pos+=v
        self.hitbox.move(v)
    def draw(self,screen):
        temp=screen.get_size()
        if self.pos.x<0 or self.pos.y<0 or self.pos.x>temp[0] or self.pos.y>temp[1]:
            return False
        rotated_bullet=pygame.transform.rotate(self.image,self.rotation)
        screen.blit(rotated_bullet,(self.pos.x,self.pos.y))
        return True
    def hit(self,enemy,time_passed):
        vel = self.vel*time_passed*(1+enemy.speed)
        if self.hitbox.colide(enemy.hitbox,vel)<1:
            enemy.get_hit(self.dmg)
            return True
        False
