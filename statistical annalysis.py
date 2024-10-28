import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the wedding dataset
data = pd.read_csv('wedding_data.csv')  # Ensure the path is correct

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Select only numeric columns for correlation analysis
numeric_data = data.select_dtypes(include=['number'])

# Perform correlation analysis
correlation_matrix = numeric_data.corr()

# Visualization of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Wedding Data')
plt.show()
