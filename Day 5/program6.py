class MYClass:
    def sum(self,a=None,b=None,c=None):
        if a != None and b!=None and c!=None:
            return a+b+c
        elif  a != None and b != None:
            return a+b
        elif a!=None:
            return a
        else:
            return 0
        

s=MYClass()

print(s.sum(1))

print(s.sum(1,2))

print(s.sum(1,2,3))
        