# This is program25.py


import numpy as np

arr1=np.array([[1,2,3],[4,5,6]])

print(type(arr1))

print(arr1.ndim)

print(arr1.shape)

print(arr1.size)

print(arr1.dtype)



c=np.zeros((3,4))

print(c)


d=np.full((3,4),6,dtype='complex')
print(d)


e=np.random.random((2,2))
print(e)


f=np.arange(0,30,5)
print(f)


g=np.linspace(0,5,10)
print(g)


