import math
class Vector3(object):
    def __init__(self,x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "(%s, %s, %s)" %(self.x,self.y,self.z)
    def __add__(self,other):
        return Vector3(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return Vector3(self.x-other.x,self.y-other.y,self.z-other.z)
    def __neg__(self):
        return Vector3(-self.x,-self.y,-self.z)
    def __mul__(self,other):
        if type(other)==type(self):
            return Vector3(self.x*other.x,self.y*other.y,self.z*other.z)
        else:
            return Vector3(self.x*other,self.y*other,self.z*other)
    __rmul__=__mul__
    def __truediv__(self,scalar):
        return Vector3(self.x/scalar,self.y/scalar,self.z/scalar)
    @classmethod
    def from_points(self,P1,P2):
       return self(P2[0]-P1[0],P2[1]-P1[1],P2[2]-P1[2])
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude>0:
            self.x/=magnitude
            self.y/=magnitude
            self.z/=magnitude
        else:
            self.x=0
            self.y=0
            self.z=0
    def get_normalized(self):
        magnitude = self.get_magnitude()
        if magnitude>0:
            x=self.x/magnitude
            y=self.y/magnitude
            z=self.z/magnitude
        else:
            self.x=0
            self.y=0
            self.z=0
        return Vector3(x,y,z)
    def get_distance_to(self,other):
        temp = self-other
        return temp.get_magnutide()
    def __abs__(self):
        return Vector3(abs(self.x),abs(self.y),abs(self.z))
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n == 0:
            result = self.x
        elif self.n==1:
            result = self.y
        elif self.n==2:
            result = self.z
        else:
            raise StopIteration
        self.n += 1
        return result
    def angle(self):
        return (math.degrees(math.atan2(self.x,self.y)),math.degrees(math.atan2(self.y,self.z)))
    def rel_angle(self,other):
        angle1=self.angle()
        anlge2=self.angle()
        return (angle1[0]-angle2[0],angle1[1]-angle2[1])
    def get_x(self):
        return Vector3(self.x,0,0)
    def get_y(self):
        return Vector3(0,self.y,0)
    def get_y(self):
        return Vector3(0,0,self.z)
        
