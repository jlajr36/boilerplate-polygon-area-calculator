import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return math.sqrt((pow(self.width,2)) + (pow(self.height,2)))

    def __str__(self):
        return "Rectangle(width={width}, height={height})".format(width=self.width, height=self.height) 

class Square(Rectangle):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def set_side(self, side):
        self.side = side

    def set_width(self, width):
        self.side = width

    def get_diagonal(self):
        return self.side * math.sqrt(2)

    def get_perimeter(self):
        return self.side * 4

    def __str__(self):
        return "Square(side={side})".format(side=self.side)
