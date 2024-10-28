import pandas as pd

# Load the dataset
data = pd.read_csv('spam.csv', encoding='latin-1')

# Print the first few rows and the column names
print(data.head())  # Show the first few rows of the dataset
print(data.columns)  # Show the actual column names
data = data[['actual_column_name_1', 'actual_column_name_2']]  # Use the correct names here
data.columns = ['label', 'text']  # Rename for easier access
