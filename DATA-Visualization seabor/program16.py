# This is program16.py
import matplotlib.pyplot as plt 

x4=range(1,5)
plt.plot(x4,[xi*1 for xi in x4])
plt.plot(x4,[xi*2 for xi in x4])
plt.plot(x4,[xi/2 for xi in x4])
plt.show()


