from abc import ABC , abstractmethod

class Vegetable(ABC):
    @abstractmethod
    def Tomato(self):
        pass

    @abstractmethod
    def Cucumber(self):
        pass

class itscolor(Vegetable):
    def __init__(self,color):
        self.color=color


    def Tomato(self):
        return self.color
    

obj=itscolor("red")

print(obj.Tomato())
