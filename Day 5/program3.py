class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

        print("First name is {} and last name is {}".format(self.fname,self.lname))

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print("Inside Student class init")


s=Student("Navneet","Mishra")
