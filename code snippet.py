import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\SNEHA SINGH\updated_wedding_data.csv")

# Ensure the 'Date' column is in datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Extract year from the 'Date' column
data['Year'] = data['Date'].dt.year

# Group by 'Year' and 'Theme'
theme_trends = data.groupby(['Year', 'Theme']).size().unstack()

