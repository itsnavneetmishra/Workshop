# This is program1.py

import numpy as np
import random

# data cleaning
# create a 3x2 array
a=np.array([[11,12],[21,23],[33,34]])
print(a)







filter=(a>=15)

print(a[filter])



print(a[(a>15)&(a<25)])


a[(a%2==0)]+=100

print(a)



print("----------------------------------------")



ex4=np.array([11.1,12.7],dtype=np.int64)

print(ex4.dtype)

print()
print(ex4)



print("----------------------------------------")




x=np.array([[111,112],[121,122]],dtype=np.int32)

y=np.array([[211.1,212.1],[221.1,222.1]],dtype=np.float64)



print(x)
print()
print(y)




print("----------------------------------------")





print(x+y)

print()


print(np.add(x,y))


print(np.sqrt(x,y))

print("----------------------------------------")

arr=10*np.random.random((2,4))

print(arr)

print("----------------------------------------")

print(arr.mean(axis=1))

print(arr.mean(axis=0))


print("----------------------------------------")


print(arr.sum())


print("----------------------------------------")

print(np.median(arr,axis=1))