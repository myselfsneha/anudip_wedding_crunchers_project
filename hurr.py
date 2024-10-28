import pandas as pd
from textblob import TextBlob

# Load your dataset
data = pd.read_csv(r"C:\Users\SNEHA SINGH\updated_wedding_data.csv")

# Create a list of 100 sample reviews (make sure this matches your DataFrame length)
reviews = [
    "Beautiful wedding, great service!" for _ in range(100)  # Placeholder for demonstration
]

# Now, you can modify this list to contain different reviews if you want
# For example:
# reviews = [
#     "Beautiful wedding, great service!",
#     "The food was excellent.",
#     "Had an amazing time!",
#     "The venue was stunning.",
#     "Wonderful experience overall."
# ] + ["Your review here"] * (100 - 5)  # Adjust this to have 100 reviews total

# Assign the reviews to the DataFrame
data['Review'] = reviews

# Function to get sentiment polarity
def get_sentiment(review):
    return TextBlob(review).sentiment.polarity

# Apply the function to the 'Review' column
data['Sentiment'] = data['Review'].apply(get_sentiment)

# Display the updated DataFrame with sentiment scores
print(data[['Review', 'Sentiment']])
