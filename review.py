import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob

# Load your dataset (ensure it has a 'Caption' column)
data = pd.read_csv(r'C:\Users\SNEHA SINGH\Downloads\social_media_wedding_trends.csv')

# Sample Text Processing
data['Cleaned_Caption'] = data['Caption'].str.lower().str.replace('[^\w\s]', '', regex=True)

# Generate a Word Cloud
text = ' '.join(data['Cleaned_Caption'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Sentiment Analysis
data['Sentiment'] = data['Caption'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Plot sentiment scores
plt.figure(figsize=(10, 5))
plt.hist(data['Sentiment'], bins=20, color='blue', alpha=0.7)
plt.title('Sentiment Analysis of Wedding Themes')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Identify top themes
theme_counts = data['Theme'].value_counts().head(10)

# Bar chart of top themes
theme_counts.plot(kind='bar', figsize=(12, 6), color='purple')
plt.title('Top 10 Wedding Themes on Social Media')
plt.xlabel('Theme')
plt.ylabel('Frequency')
plt.show()
