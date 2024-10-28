import pandas as pd

# Load the newly uploaded dataset to check column names
file_path = r"C:\Users\SNEHA SINGH\updated_wedding_data.csv"
data = pd.read_csv(file_path)

# Display the column names in the dataset
data.columns
import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot to explore correlation between guest size and wedding cost
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['Guest Size'], y=data['Cost'], color='blue', s=100, alpha=0.6)
plt.title('Correlation between Guest Size and Wedding Cost')
plt.xlabel('Guest Size')
plt.ylabel('Wedding Cost')
plt.show()
