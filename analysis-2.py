import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='Guest Size', y='Cost', data=data)
plt.title('Cost vs Guest Size')
plt.show()
