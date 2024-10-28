import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

# Step 1: Load your dataset
data = pd.read_csv(r"C:\Users\SNEHA SINGH\updated_wedding_data.csv")

# Step 2: Initialize geolocator
geolocator = Nominatim(user_agent="wedding_analysis")

# Step 3: Geocode locations
# Create a function to get latitude and longitude from a location
def geocode_location(location):
    try:
        location_data = geolocator.geocode(location)
        return location_data.latitude, location_data.longitude
    except:
        return None, None

# Step 4: Create latitude and longitude columns
data['Latitude'], data['Longitude'] = zip(*data['Location'].apply(geocode_location))

# Step 5: Check for missing latitude and longitude
missing_locations = data[data['Latitude'].isnull() | data['Longitude'].isnull()]
print("Locations with missing coordinates:")
print(missing_locations[['Location']])

# Step 6: Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))

# Step 7: Load a map of the world (or a specific region)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Step 8: Plot the world map with wedding locations
fig, ax = plt.subplots(figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
gdf.plot(ax=ax, color='orange', markersize=5, alpha=0.6, label='Wedding Locations')

# Step 9: Customize the plot
plt.title('Geographic Distribution of Weddings')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()

# Optional: Save the plot
plt.savefig('wedding_locations_map.png', bbox_inches='tight')

# Step 10: Show the plot
plt.show()
