# This is program5.py
import numpy as np


start=np.zeros((4,3))

print(start)

print("************************************")

add_rows=np.array([1,0,2])
print(add_rows)

print("************************************")

y=start + add_rows
print(y)

print("************************************")

add_scalar=np.array([1])
print(start+add_scalar)

print("************************************")

arrA=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arrA)


print("************************************")

#create our 1x3 array


arrB=np.array([[0,1,0]])

arrB=arrB.T

print(arrB)


print("************************************")

