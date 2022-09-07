class Shape:
    def __init__(self):
        self.area = 0

    def Area(self):
        print(self.area)


class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = 0

    def Area(self):
        area = self.length * self.length
        print(area)

x = int(input())
square1 = Square(x)
square1.Area()

    

