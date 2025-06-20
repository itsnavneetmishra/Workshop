# This is program10.py
# This is program9.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




fig, ax = plt.subplots(2)

x1 = np.linspace(0, 10, 100)

ax[0].plot(x1, np.sin(x1), 'b-')
ax[1].plot(x1, np.cos(x1), 'b-');
plt.xlabel('x axis')
plt.ylabel('y axis')


plt.legend()
plt.show()