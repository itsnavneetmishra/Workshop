class AREA:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def recarea(self):
        print(self.l*self.b)

a=int(input("Enter length : "))
b=int(input("Enter breadth : "))
R1=AREA(a,b)
R1.recarea()