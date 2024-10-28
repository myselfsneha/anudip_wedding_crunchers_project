import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('wedding_data.csv')

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract year for analysis
data['Year'] = data['Date'].dt.year

# Visualization: Plot average costs per year
average_cost_per_year = data.groupby('Year')['Cost'].mean()
average_cost_per_year.plot(kind='bar')
plt.title('Average Wedding Cost per Year')
plt.ylabel('Average Cost')
plt.xlabel('Year')
plt.show()

# Scatter plot: Cost vs Guest Size
sns.scatterplot(x='Guest Size', y='Cost', data=data)
plt.title('Cost vs Guest Size')
plt.show()
