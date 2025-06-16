#operator overloading

class School:
    def __init__(self,fee):
        self.fee=fee

    def __add__(self,other):
        return self.fee + other.fee

A=School(300)
B=School(400)
print("Operator Overloading (A+B):",A+B)


a=12
b=20
print("Built-in int.__add__(a,b):",int.__add__(a,b))



#mehod overloading

class ABC:
    def add(self,a,b=None,c=None):
        if c is not None:
            print("Method Overloading(3 args):",a+b+c)

        elif b is not None:
            print("Method Overloading (2 args):",a+b)

        else:
            print("Method Ovrloading (1 arg)",a)

obj=ABC()
obj.add(10,20)
obj.add(10,20,10)


#method overriding 




