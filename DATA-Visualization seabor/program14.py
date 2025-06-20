import seaborn as sns
import pandas as pd

import matplotlib 
import matplotlib.pyplot
import matplotlib.pyplot as plt 

import numpy as np
import pandas as pd
tips=sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill",data=tips)
plt.show()