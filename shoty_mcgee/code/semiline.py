import math
from .vector2 import Vector2
class line(object):
    def __init__(self,orig,vector):
        self.orig=orig
        self.vector=vector
    def __str__(self):
        return "(%s,%s)" %(self.orig,self.vector)
    def __add__(self,other):
        return line(self.orig,self.vector+other.vector)
    def intersect(self,other):
        if self.vector.y == 0:
            if other.vector.y == 0:
                return False
            elif self.vector.x == 0:
                m = 0
                n = (self.orig.y-other.orig.y)/other.vector.y
                if other.vector.x == 0:
                    if self.orig.x == other.orig.x:
                        return 0,n
                    else:
                        return False
                else:
                    if n == (self.orig.x-other.orig.x)/other.vector.x:
                        return 0,n
                    else:
                        return False
            else:
                n = (self.orig.y-other.orig.y)/other.vector.y
                m = (other.orig.x-self.orig.x + n*other.vector.x)/self.vector.x
                return m,n
        else:
            k0 = (other.vector.x*self.vector.y-self.vector.x*other.vector.y)
            if k0 == 0:
                return False
            else:
                n = (self.vector.y*(self.orig.x-other.orig.x) + self.vector.x*(other.orig.y-self.orig.y))/k0
                m = (other.orig.y-self.orig.y + n*other.vector.y)/self.vector.y
                return m,n
    def mag_intersect(self,other):
        temp = self.intersect(other)
        if temp:
            m,n=temp
            if m<1 and n<1 and m>=0 and n>=0:
                return m,n
            else:
                return 1,1
