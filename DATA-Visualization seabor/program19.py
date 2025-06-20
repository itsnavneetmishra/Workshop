import matplotlib.pyplot as plt 
import seaborn as sns


tips=sns.load_dataset('tips')
tips.corr(numeric_only=True)
tips.head()
# Correlation Matrix
sns.heatmap(tips.corr(numeric_only=True),annot=True,cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()