class Student:
    
    college_name = "ABC college"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("Welcome students")\
        
    def get_marks(self):
        return self.marks

s1=Student("Navneet",99)
print(s1.name,s1.marks) 
print(s1.college_name)

s1.welcome()

print(s1.get_marks())


s2=Student("Gaurav",98)
print(s2.name,s2.marks,s2.college_name)