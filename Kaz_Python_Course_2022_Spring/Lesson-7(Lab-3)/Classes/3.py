from shutil import ReadError


class Shape:
    def __init__(self):
        self.area = 0

    def Area(self):
        print(self.area)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def getArea(self):
        Area = self.length * self.width
        print(Area)

length = int(input())
width = int(input())
Rectangle1 = Rectangle(length, width)
Rectangle1.getArea()


    

