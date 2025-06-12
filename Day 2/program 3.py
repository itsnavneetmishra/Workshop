class AREA:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def recarea(self):
        print(self.l*self.b)


R1=AREA(10,20)
R2=AREA(2,5)
R1.recarea()
R2.recarea()