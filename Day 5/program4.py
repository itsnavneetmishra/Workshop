class School:
    def __init__(self,fee):
        self.fee=fee;

    def __add__(self,other):
        return self.fee + other.fee;

A=School(300);
B=School(400);
print(A+B)

a=12
b=20
int.__add__(a,b)



class ABC:
    def add(self,a,b=None,c=None):
        if c != None:
            print(A+B+c);

        else:
            print(a+b);

obj=ABC()

obj.add(10,20,10)




#method override

class A:
    def first(self):
        print("This is first value of A")

class B(A):
    def first(self):
        print("This is the first value of B")

obj1=B()

obj1.first()