import pandas as pd
import numpy as np

# Creating a sample dataset
data = {
    'Date': pd.date_range(start='2021-01-01', periods=100, freq='ME'),  # Updated 'M' to 'ME'
    'Location': np.random.choice(['New York', 'Los Angeles', 'Miami', 'Chicago', 'Austin'], size=100),
    'Guest Size': np.random.randint(50, 300, size=100),
    'Cost': np.random.randint(15000, 100000, size=100)
}
'''
# Creating DataFrame
wedding_data = pd.DataFrame(data)

# Saving as CSV
wedding_data.to_csv('wedding_data.csv', index=False)

# To view the dataset
print(wedding_data.head())
'''
import pandas as pd
import numpy as np

# Assuming you've already loaded your dataset
data = pd.read_csv('wedding_data.csv')

# Add a new 'Theme' column with random wedding themes
possible_themes = ['Rustic', 'Beach', 'Vintage', 'Traditional', 'Modern', 'Fairytale']
data['Theme'] = np.random.choice(possible_themes, size=len(data))

# Save the updated dataset
data.to_csv('updated_wedding_data.csv', index=False)

# Check the updated dataset
print(data.head())

# Add the 'Theme' column to the dataset
data['Theme'] = ['Modern', 'Classic', 'Rustic', 'Vintage']  # Replace with actual values

# Check if the column was added
print(data.head())

# Save the updated dataset
data.to_csv('updated_wedding_data.csv', index=False)
