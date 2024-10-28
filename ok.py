import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the updated dataset
data = pd.read_csv(r"C:\Users\SNEHA SINGH\updated_wedding_data.csv")

# Step 2: Print the columns to verify what’s loaded
print("Columns in the dataset:", data.columns)

# Step 3: Ensure 'Date' is in datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Step 4: Create the 'Year' column if it doesn't exist
if 'Year' not in data.columns:
    data['Year'] = data['Date'].dt.year

# Step 5: Verify if 'Year' column is now present
print("Columns after adding Year:", data.columns)

# Step 6: If you have a 'Theme' column, ensure it is also in the data
if 'Theme' not in data.columns:
    # If needed, you can add a 'Theme' column randomly for the example
    import numpy as np
    
    # Define some themes for illustration
    themes = ['Beach', 'Garden', 'Traditional', 'Destination', 'Rustic']
    
    # Assign random themes if 'Theme' doesn't exist
    data['Theme'] = np.random.choice(themes, size=len(data))

# Step 7: Group by Year and Theme to analyze trends
theme_trends = data.groupby(['Year', 'Theme']).size().unstack()
theme_trends.plot(kind='bar', stacked=True, figsize=(10, 5))
plt.title('Wedding Themes Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Weddings')
plt.legend(title='Theme')
plt.show()
