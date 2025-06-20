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
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type


car1=Fortuner("diesel")
car1.start()
 

