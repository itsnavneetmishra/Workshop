# This is program2.py


import numpy as np
import matplotlib as plt
import seaborn as sns
import pandas as pd


x1=np.limespace(0.10,100)


fig=plt.figure()

plt.plot(x1,np.sin(x1),'-')

plt.plot(x1,np.cos(x1),'-')