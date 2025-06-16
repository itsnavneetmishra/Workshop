class Father:
    def __init_(self):
        self.money=2000
        print("Father class constructor")

class Son(Father):
    def __init__(self):
        self.money=5000
        print("Son class Constructor")

    def display(self):
        print(self.money)


s=Son()


s.display()