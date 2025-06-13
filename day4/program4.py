class Father:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Father's name : {self.name}")
        print(f"Father's age : {self.age}")


class Son(Father):

    def __init__(self, name, age,school):
        super().__init__(name,age)
        self.school=school

    def display_son(self):
        self.display()
        print(f"son's school :{self.school}")


dad=Father("mishra",45)
dad.display()


son=Son("Navneet",19,"BLC")
son.display_son()