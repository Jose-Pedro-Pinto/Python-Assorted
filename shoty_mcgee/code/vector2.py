import math
class Vector2(object):
    def __init__(self,x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)" %(self.x,self.y)
    def __add__(self,other):
        return Vector2(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector2(self.x-other.x,self.y-other.y)
    def __neg__(self):
        return Vector2(-self.x,-self.y)
    def __mul__(self,scalar):
        return Vector2(self.x*scalar,self.y*scalar)
    def __truediv__(self,scalar):
        return Vector2(self.x/scalar,self.y/scalar)
    @classmethod
    def from_points(self,P1,P2):
       return self(P2[0]-P1[0],P2[1]-P1[1])
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude>0:
            self.x/=magnitude
            self.y/=magnitude
        else:
            self.x=0
            self.y=0
    def get_normalized(self):
        magnitude = self.get_magnitude()
        if magnitude>0:
            x=self.x/magnitude
            y=self.y/magnitude
        else:
            self.x=0
            self.y=0
        return Vector2(x,y)
    def get_distance_to(self,other):
        temp = self-other
        return temp.get_magnutide()
    def abs(self):
        if self.x<0:
            x=-self.x
        else:
            x=self.x
        if self.y<0:
            y=-self.y
        else:
            y=self.y
        return Vector2(x,y)
    def angle(self):
        return math.degrees(math.atan2(self.x,self.y))
    def rel_angle(self,other):
        return self.angle()-other.angle()
    def get_x(self):
        return Vector2(self.x,0)
    def get_y(self):
        return Vector2(0,self.y)
