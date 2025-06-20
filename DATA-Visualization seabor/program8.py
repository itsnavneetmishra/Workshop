# This is program8.py
# This is program7.py
# This is program6.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



x=np.linspace(0,2,100)


plt.plot(x,x,label='linear')

plt.plot(x,x**2,label='quadratic')

plt.plot(x,x**3,label='cubic')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('simple plot')
plt.legend()
plt.show()