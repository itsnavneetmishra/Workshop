# This is program2.py


import pandas as pd

ser=pd.Series(['geet',200,'shweta',300,'Nitya'],[1,2,3,4,5])

print(ser)


print(ser.index)

print(ser.loc[[1,5]])

print(ser.iloc[[2]])


print("--------------------------------")
print(ser*2)



print(ser[[2,4]]**2)


