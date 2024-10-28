import pandas as pd

# Load dataset
data = pd.read_csv('wedding_data.csv')

# View the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Get summary statistics
print(data.describe())
