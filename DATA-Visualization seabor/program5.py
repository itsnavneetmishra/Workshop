# This is program5.py
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



plt.show()


print((plt.gca()))

