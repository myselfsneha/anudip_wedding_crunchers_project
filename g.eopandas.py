import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('wedding_data.csv')

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])
# Example: Create a dictionary for locations and their corresponding latitude/longitude
location_data = {
    'Location': ['New York', 'Los Angeles', 'Miami', 'Chicago', 'Austin'],
    'Latitude': [40.7128, 34.0522, 25.7617, 41.8781, 30.2672],
    'Longitude': [-74.0060, -118.2437, -80.1918, -87.6298, -97.7431]
}

location_df = pd.DataFrame(location_data)

# Merge the wedding data with the location data based on 'Location'
data = data.merge(location_df, on='Location')
# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['Longitude'], data['Latitude']))

# Set the coordinate reference system (CRS) to WGS 84
gdf.set_crs(epsg=4326, inplace=True)
# Load a map of the world or specific country/region
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the world map
fig, ax = plt.subplots(figsize=(10, 10))
world.boundary.plot(ax=ax, linewidth=1)

# Plot wedding locations
gdf.plot(ax=ax, color='red', markersize=5, alpha=0.5)

# Add title
plt.title('Geographic Distribution of Weddings')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
