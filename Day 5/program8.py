from abc import ABC, abstractmethod


class Computer:
    @abstractmethod
    def process(self):
        """Subclasses must implement this method"""
        pass

    def message(self):
        print("Computer is an electronic device")

class Laptop(Computer):
    def process(self):
        print("Executing laptop process")

class Desktop(Computer):
    def process(self):
        print("Executing desktop process")

com1=Laptop()
com2=Desktop()

com1.process()
com1.message()
com2.process()