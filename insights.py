import matplotlib.pyplot as plt

# Create a boxplot to visualize outliers in wedding costs
plt.figure(figsize=(8, 6))
plt.boxplot(data['Cost'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Boxplot of Wedding Costs')
plt.xlabel('Cost (in currency)')
plt.show()
