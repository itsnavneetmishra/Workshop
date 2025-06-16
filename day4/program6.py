class Father:
    money=1000
    def show(self):
        print("Parent class instance method")

    @classmethod
    def moneyshow(cls):
        print("Parent class method : Money")