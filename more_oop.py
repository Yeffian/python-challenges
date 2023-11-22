from copy import copy

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    def __str__(self) -> str:
        return "({0}, {1})".format(self.x, self.y)
    
class Rectangle:
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

p1 = Point(3, 4)
p2 = copy(p1)

print(p1 is p2)
print(same_coordinates(p1, p2))