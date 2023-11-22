class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0) -> None:
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600        
        secs_left_over = totalsecs % 3600
        self.minutes = secs_left_over // 60
        self.seconds = secs_left_over % 60
    
    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
    
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        return self.to_seconds() > time2.to_seconds()
    
    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
    
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    def reverse(self):
        (self.x , self.y) = (self.y, self.x)

    def __str__(self) -> str:
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other):
        return Point(other * self.x,  other * self.y)


def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)

def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))
    

p = Point(3, 4)
front_and_back(p)