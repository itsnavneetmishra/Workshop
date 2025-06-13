class MyClass:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def display(self):
        print(self.x)
        print(self.y)

obj=MyClass(5,8)
obj.display()