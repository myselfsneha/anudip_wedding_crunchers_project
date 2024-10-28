# Example: Create a dictionary for locations and their corresponding latitude/longitude
location_data = {
    'Location': ['New York', 'Los Angeles', 'Miami', 'Chicago', 'Austin'],
    'Latitude': [40.7128, 34.0522, 25.7617, 41.8781, 30.2672],
    'Longitude': [-74.0060, -118.2437, -80.1918, -87.6298, -97.7431]
}

location_df = pd.DataFrame(location_data)

# Merge the wedding data with the location data based on 'Location'
data = data.merge(location_df, on='Location')
