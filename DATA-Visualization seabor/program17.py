# This is program17.py
import matplotlib.pyplot as plt 
import numpy as np

plt.figure(figsize=(7,7))
x1=[35,25,20,20]
labels=["Com","Elec","Mec","Chem"]
plt.pie(x1,labels=labels);
plt.show()