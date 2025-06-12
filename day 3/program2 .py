class Person:
    def __new__(cls):
        print("Thid is a new method")
        instance=super().__new__(cls)
        return instance

    def __int__(self):
        print("Init Method")

p=Person()
