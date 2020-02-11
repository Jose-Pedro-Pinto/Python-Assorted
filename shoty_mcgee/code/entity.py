from .vector2 import Vector2
class entity(object):
    def __init__(self,pos=Vector2(0,0),size=Vector2(0,0),rotation=0,image=None,speed=0,dmg=0,hp=1):
        self.alive=True
        self.pos=pos
        self.size=size
        self.rotation=rotation
        self.speed=speed
        self.image=image
        self.dmg=dmg
        self.base_hp=hp
        self.current_hp=hp
    def move(self,screen,vel):
        self.pos+=vel
        self.hitbox.move(vel)
        return self.check_borders(screen)
    def check_borders(self,screen):
        x,y=screen.get_size()
        if self.pos.x>x:
            return False
        if self.pos.y>y:
            return False
        if self.pos+self.size.x<0:
            return False
        if self.pos+self.size.y<0:
            return False
        return True
    def draw(self,screen):
        rotated_player=pygame.transform.rotate(self.image,self.rotation)
        x=self.pos.x-rotated_player.get_width()//2
        y=self.pos.y-rotated_image.get_height()//2
        screen.blit(self.image,self.pos)
    def hit(self,other):
        other.get_hit(self.dmg)
    def get_hit(self,dmg):
        self.current_hp-=dmg
        if self.current_hp<=0:
            self.alive=False
            self.death()
    def death(self):
        pass
