import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load your dataset
data = pd.read_csv(r"C:\Users\SNEHA SINGH\updated_wedding_data.csv")

# Step 2: Group by location and plot a box plot of wedding costs
plt.figure(figsize=(12, 6))
data.boxplot(column='Cost', by='Location', rot=90)
plt.title('Wedding Cost by Region')
plt.suptitle('')  # Remove automatic title
plt.xlabel('Location')
plt.ylabel('Cost (in currency)')
plt.tight_layout()  # Adjust layout to fit labels
plt.show()
