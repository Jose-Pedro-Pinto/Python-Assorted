from .entity import entity
from .vector2 import Vector2
from .poligon import *
from pygame.locals import *
from .bullet import *
class player(entity):
    def __init__(self,pos,image,bullet_image,bullet_speed=1,hp=1,dmg=1,rof=5,speed=1,middle=None,rotation=0):
        super(player,self).__init__(pos,Vector2(image.get_size()),rotation,image=image,speed=speed,dmg=dmg,hp=hp)
        self.rof=rof
        self.bullet_image=bullet_image
        self.bullet_speed=bullet_speed
        if middle:
            self.middle=pos+middle
        else:
            self.middle=Vector2(pos.x+image.get_width()//2,pos.y+image.get_height()//2)
        self.hitbox=circle_to_pol(self.middle,self.image.get_height()//2,100)
    def draw(self,screen):
        rotated_player=pygame.transform.rotate(self.image,self.rotation)
        mult=self.image.get_width()//2-(self.middle-self.pos).x
        x=self.middle.x-rotated_player.get_width()//2+mult*math.cos(math.radians(self.rotation))
        y=self.middle.y-rotated_player.get_height()//2-mult*math.sin(math.radians(self.rotation))
        screen.blit(rotated_player,(x,y))
    def move(self,time_passed,screen):
        keys=pygame.key.get_pressed()
        vel=Vector2(0,0)
        if keys[K_a]:
            vel.x-=1
        if keys[K_d]:
            vel.x+=1
        if keys[K_w]:
            vel.y-=1
        if keys[K_s]:
            vel.y+=1
        border = []
        border.append(pos_to_pol([(0,0),(screen.get_width(),0)]))
        border.append(pos_to_pol([(screen.get_width(),0),(screen.get_width(),screen.get_height())]))
        border.append(pos_to_pol([(screen.get_width(),screen.get_height()),(0,screen.get_height())]))
        border.append(pos_to_pol([(0,screen.get_height()),(0,0)]))
        vel.normalize()
        vel*=time_passed*self.speed
        for x in border:
            v = self.hitbox.slide(x,vel)
            vel=v
        self.pos+=vel
        self.middle+=vel
        self.hitbox.move(vel)
    def shoot(self,time_passed):
        if self.rof>1000/time_passed:
            mult=self.image.get_width()-(self.middle-self.pos).x
            x=self.middle.x+mult*math.cos(math.radians(self.rotation))
            y=self.middle.y-mult*math.sin(math.radians(self.rotation))
            bullet1 = bullet(Vector2(x,y),self.rotation,self.bullet_image,dmg=self.dmg,speed=self.bullet_speed)
            return bullet1
        else:
            return None
    def mouse_rotate(self):
        mouse_x,mouse_y=pygame.mouse.get_pos()
        aim_dir=Vector2(mouse_x,mouse_y)-self.middle
        self.rotation=aim_dir.angle()-90
