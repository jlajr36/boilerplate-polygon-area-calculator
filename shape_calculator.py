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

    def get_picture(self):
        strOut = ""
        if self.width > 25 or self.height > 25:
            strOut = "Too big for picture."
        else:
            for y in range(self.height):
                for x in range(self.width):
                    strOut += '*'
                strOut += '\n'
        return strOut

    def get_amount_inside(self, square):
        return self.get_area() // square.get_area()

    def __str__(self):
        return "Rectangle(width={width}, height={height})".format(width=self.width, height=self.height) 

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def get_diagonal(self):
        return self.width * math.sqrt(2)

    def __str__(self):
        return "Square(side={side})".format(side=self.width)