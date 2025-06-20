# This is program4.py

import pandas as pd
import numpy as np

obj=pd.Series([4,2,4,-5])


print(obj)

print(type(obj))
print(obj.values)
print(obj.index)


obj2=pd.Series([1,2,3,4],index=['a','b','c','d'])

print(obj2)


obj2['b']=6

obj2[['a','c','d']]=100

print(obj2)



print(np.exp(obj2))


print('b' in obj2)

print('e' in obj2)


