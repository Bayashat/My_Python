import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The coordinates of this point is ({self.x},{self.y})")

    def move(self):
        x,y = y,x

    def dist(self, point):
        distance = math.sqrt(  ((point.x - self.x)**2)   + ((point.y - self.y)**2)      )
        print(distance)

    '''
    def dist(self):
        distance = math.sqrt( ((self.x - self.y)**2 ) + ((self.y - self.x)**2))
        print(distance)
    '''

Point1 = Point(3,7)
Point2 = Point(2,4)  # 1 + 9

Point1.dist(Point2)
