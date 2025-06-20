# This is program4.py
# create a plot figure


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



x1 = np.linspace(0, 10, 100)
# create a plot figure
fig = plt.figure()
plt.plot(x1, np.sin(x1), '-')
plt.plot(x1, np.cos(x1), '--');


plt.figure()
# create the first of two panels and set current axis
plt.subplot(2, 1, 1)   # (rows, columns, panel number)
plt.plot(x1, np.sin(x1))
# create the second of two panels and set current axis
plt.subplot(2, 1, 2)   # (rows, columns, panel number)
plt.plot(x1, np.cos(x1));
plt.show()



