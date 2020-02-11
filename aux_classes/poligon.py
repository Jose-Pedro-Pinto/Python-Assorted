import math
from semiline import line
import pygame
from vector2 import Vector2
class poligon(object):
    def __init__(self,lines):
        self.lines=lines
    def __str__(self):
        string = ""
        for line1 in self.lines:
            string+=str(line1)
            print(line1)
        return string
    def draw(self,screen,color=(255,0,0)):
        for line1 in self.lines:
            pygame.draw.line(screen,color,(line1.orig.x,line1.orig.y),(line1.vector.x+line1.orig.x,line1.vector.y+line1.orig.y),2)
    def colide(self,other,vector):
        min_mag=1
        for line1 in self.lines:
            line2 = line(line1.orig,vector)
            for line3 in other.lines:
                temp = line2.mag_intersect(line3)
                if temp:
                    m,n=temp
                    min_mag=min(min_mag,m)
        for line1 in other.lines:
            line2 = line(line1.orig,-vector)
            for line3 in self.lines:
                temp = line2.mag_intersect(line3)
                if temp:
                    m,n=temp
                    min_mag=min(min_mag,m)
        return min_mag
    def slide(self,other,vector):
        min_mag=1
        for line1 in self.lines:
            line2 = line(line1.orig,vector)
            for line3 in other.lines:
                temp = line2.mag_intersect(line3)
                if temp:
                    m,n=temp
                    if m<min_mag:
                        line4=line3
                        min_mag=m
        for line1 in other.lines:
            line2 = line(line1.orig,-vector)
            for line3 in self.lines:
                temp = line2.mag_intersect(line3)
                if temp:
                    m,n=temp
                    if m<min_mag:
                        line4=line3
                        min_mag=m
        v = vector*(min_mag-0.01)
        if min_mag==1:
            return v
        v1=vector-v
        angle = abs(v1.rel_angle(line4.vector))
        mag = v1.get_magnitude()
        v2=Vector2(line4.vector.x,line4.vector.y)
        v2.normalize()
        v1.x=mag*v2.x*math.cos(math.radians(angle))
        v1.y=mag*v2.y*math.cos(math.radians(angle))
        return v+v1
    def move(self,vector):
        for line1 in self.lines:
            line1.orig+=vector
def pos_to_pol(pos):
    lines=[]
    v0 = Vector2(pos[0][0],pos[0][1])
    for i in range(1,len(pos)):
        lines.append(line(v0,Vector2(pos[i][0],pos[i][1])-v0))
        v0=Vector2(pos[i][0],pos[i][1])
    lines.append(line(v0,Vector2(pos[0][0],pos[0][1])-v0))
    return poligon(lines)
def points_to_pol(points):
    lines=[]
    v0 = points[0]
    for i in range(1,len(points)):
        lines.append(line(v0,points[i]-v0))
        v0=points[i]
    lines.append(line(v0,points[0]-v0))
    return poligon(lines)
def rect_to_pol(pos,size):
    lines=[]
    lines.append(line(pos,size.get_x()))
    lines.append(line(pos+size.get_x(),size.get_y()))
    lines.append(line(pos+size,-size.get_x()))
    lines.append(line(pos+size.get_y(),-size.get_y()))
    return poligon(lines)
def circle_to_pol(center_pos,radius,pol_n):
    lines=[]
    v0 = center_pos+Vector2(radius,0)
    for i in range(1,pol_n+1):
        angle=2*i/pol_n
        v1 = center_pos+Vector2(math.cos(math.pi*angle),math.sin(math.pi*angle))*radius
        v2 = v1-v0
        lines.append(line(v0,v2))
        v0=v1
    return poligon(lines)
def elipse_to_pol(center_pos,width,height,pol_n):
    lines=[]
    v0 = center_pos+Vector2(width,0)
    for i in range(1,pol_n+1):
        angle=2*i/pol_n
        v1 = center_pos+Vector2(math.cos(math.pi*angle)*width,math.sin(math.pi*angle)*height)
        v2 = v1-v0
        lines.append(line(v0,v2))
        v0=v1
    return poligon(lines)
