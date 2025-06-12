class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
   
        print("Adding new student in database ")

s1=Student("Navneet",99)
print(s1.name,s1.marks)