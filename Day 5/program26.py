import numpy as np


arr = np.array([[1,2,3],[4,5,6]])
flarr = arr.flatten()
print(arr)
print(flarr)

arr = np.array([[1,2,3,4],

                [4,5,6,7],

                [8,7,6,5]])
temp = arr[:2,:2]
print(arr)
print(temp)

print("-------------------------------")

print(arr.T)
