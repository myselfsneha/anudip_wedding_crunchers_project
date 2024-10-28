import pandas as pd
import matplotlib.pyplot as plt

# Load the wedding dataset
data = pd.read_csv('wedding_data.csv')  # Ensure the path is correct

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Adding year and month columns
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month_name()

# Calculate average cost by month
avg_cost_by_month = data.groupby('Month')['Cost'].mean().reindex(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Visualization
avg_cost_by_month.plot(kind='bar', title='Average Wedding Cost by Month', xlabel='Month', ylabel='Average Cost')
plt.show()

# Assuming `data` contains a 'Month' column
weddings_per_month = data['Month'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
weddings_per_month.plot(kind='bar')
plt.title('Number of Weddings Per Month')
plt.xlabel('Month')
plt.ylabel('Number of Weddings')
plt.xticks(rotation=45)
plt.show()

# Assuming `data` contains 'Year' and 'Theme' columns
theme_trends = data.groupby(['Year', 'Theme']).size().unstack()
theme_trends.plot(kind='bar', stacked=True, figsize=(10, 5))
plt.title('Wedding Themes Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Weddings')
plt.legend(title='Theme')
plt.show()

