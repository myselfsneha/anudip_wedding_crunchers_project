import matplotlib.pyplot as plt

# Assuming `data` contains a 'Year' and 'Cost' columns
average_costs = data.groupby('Year')['Cost'].mean()
plt.figure(figsize=(10, 5))
plt.plot(average_costs.index, average_costs.values, marker='o')
plt.title('Average Wedding Costs Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Cost')
plt.grid()
plt.show()
