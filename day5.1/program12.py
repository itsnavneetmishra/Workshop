#Inheritance
"""When one class(child/derived) derives the properties and methods of another class (parent/base)"""

class Car:

    color="Black"

    @staticmethod
    def start():
        print("car Started")

    @staticmethod
    def Stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fourtuner")
car2=ToyotaCar("velfire")

print(car1.start())

print(car1.name)

print(car1.color)

