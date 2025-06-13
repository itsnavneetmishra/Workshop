class Apple:
    def Sweet(self):
        print("Apple is sweet")

    def Sour(self):
        print("Apple is sour not")

class Orange(Apple):
    def Sweet(self):
        print("Apple is sweet of Orange Class")

    def Sour(self):
        print("Apple is a sour not")

obj1 = Orange()
obj1.Sweet()