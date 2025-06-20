# This is program9.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



x=np.linspace(0,2,100)


plt.plot([1,2,3,4],[1,4,9,16],'r')
plt.axis([0,6,0,20])

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('simple plot')
plt.legend()
plt.show()