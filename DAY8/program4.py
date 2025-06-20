# This is program4.py
import numpy as np


today=np.datetime64('2023-06-17')

print("Date is : ",today)

print("year is : ",np.datetime64(today,'Y'))



# creating array of dates in a month 
dates = np.arange('2025-02', '2025-03', dtype='datetime64[D]') 
print("\nDates of June, 2025:\n", dates) 
print("Today is June:", today in dates)