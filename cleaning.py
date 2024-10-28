import pandas as pd

# Load the dataset
data = pd.read_csv('wedding_data.csv')

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Check for missing values
print(data.isnull().sum())

# Drop or fill missing values if any (optional)
data = data.dropna()  # or use data.fillna() for specific columns

# View the cleaned dataset
print(data.head())
