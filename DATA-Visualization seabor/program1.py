# This is program1.py

import matplotlib as plt
import seaborn as sns
import pandas as pd

tips= sns.load_dataset("tips")

sns.boxplot(x='day',y='total_bill',data=tips)

df=pd.DataFrame({'A ' : [1,3,5], 'B' : [2,4,6]})

df.plot(kind='bar')

plt.show()