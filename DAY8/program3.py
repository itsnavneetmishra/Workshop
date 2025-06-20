# This is program3.py
import numpy as np

s1=np.array(['desk','chair','bulb'])
s2=np.array(['lamb','bulb','chair'])

print(s1,s2)


print(np.union1d(s1,s2))

print(np.intersect1d(s1,s2))


print(np.setdiff1d(s1,s2))


print(np.isin(s1,s2))