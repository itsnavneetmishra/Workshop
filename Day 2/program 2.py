class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print(self.l * self.b)

R1 = Rectangle(10, 5)
R2 = Rectangle(4, 3)

R1.area()   
R2.area()   
