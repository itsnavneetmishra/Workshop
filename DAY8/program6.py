# This is program6.py
import numpy as np


###### Boradcasting
a = np.array([1.0,2.0,3.0])
b = 2.0
print(a * b)
c = [2.0,3.0,4.0]
print(a * c)
a = np.array([1.0,2.0,3.0,4.0])
b = np.array([0.0,1.0,2.0])
print(a[:, np.newaxis] + b)
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
print(a) 
print(b) 
print(a + b)