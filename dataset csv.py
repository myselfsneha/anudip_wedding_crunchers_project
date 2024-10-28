import pandas as pd

# Sample data for social media trends related to wedding themes
data = {
    "Post_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Theme": [
        "Rustic", "Beach", "Vintage", "Bohemian", "Classic",
        "Modern", "Garden", "Fairytale", "Destination", "Minimalist"
    ],
    "Caption": [
        "Loving this rustic wedding vibe! #WeddingTrends #Rustic",
        "Beach weddings are the best! 🌊 #BeachWedding",
        "Vintage themes bring a touch of nostalgia. #VintageWedding",
        "Bohemian style is all about free-spirited fun! #Boho",
        "Classic elegance never goes out of style. #ClassicWedding",
        "Modern weddings with a twist! #ModernWedding",
        "Gardens are the perfect backdrop for weddings! 🌸 #GardenWedding",
        "Every fairytale deserves a happy ending! #FairytaleWedding",
        "Destination weddings are the ultimate adventure! #DestinationWedding",
        "Less is more! Loving minimalist wedding designs. #MinimalistWedding"
    ],
    "Likes": [150, 200, 120, 300, 250, 180, 90, 400, 350, 130],
    "Shares": [15, 25, 10, 50, 30, 20, 5, 70, 40, 15],
    "Comments": [5, 8, 3, 15, 10, 7, 2, 20, 12, 4],
    "Date": [
        "2024-01-15", "2024-02-10", "2024-02-25", "2024-03-05", "2024-03-20",
        "2024-04-15", "2024-05-01", "2024-05-20", "2024-06-10", "2024-06-25"
    ]
}

# Create a DataFrame
social_media_data = pd.DataFrame(data)

# Save to CSV
csv_file_path = '/mnt/data/social_media_wedding_trends.csv'
social_media_data.to_csv(csv_file_path, index=False)

csv_file_path
