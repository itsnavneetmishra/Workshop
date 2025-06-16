class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        if not isinstance(other,Student):
            return NotImplemented
        m1=self.m1+other.m1
        m2=self.m2+other.m2

        return Student(m1,m2)
s1=Student(58,59)
s2=Student(60,65)


s3=s1+s2

print(s3,m1)
