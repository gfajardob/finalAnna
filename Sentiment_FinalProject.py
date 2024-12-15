import pandas as pd
from textblob import TextBlob
import nltk

# Download necessary corpora using nltk *CB suggested 
nltk.download('vader_lexicon')

# Load the CSV file with path
df = pd.read_csv(r'/Users/gabrielafajardobocanegra/Programming Fundamentals/Final project/landmarks_comments.csv', encoding='ISO-8859-1', names=["landmark", "review"], header=0)

# Check the first few rows 
#print(df.head())

# Sentiment Analyzer to review column
df['sentiment'] = df['review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Ask the user to select a landmark
landmark = input("Please select a landmark (Liberty Bell, Independence Hall, Elfreth's Alley): ").strip()

# Normalize the input to match the format in the CSV (case insensitive)
df['landmark'] = df['landmark'].str.strip().str.lower()
landmark = landmark.strip().lower()

# Filter the dataframe based on what the user selected
selected_review = df[df['landmark'] == landmark]

if not selected_review.empty:
    sentiment = selected_review['sentiment'].iloc[0]
    if sentiment > 0:
        print(f"Review for {landmark.title()}: Positive experience. Highly recommended!")
    elif sentiment < 0:
        print(f"Review for {landmark.title()}: Negative experience. Not recommended.")
    else:
        print(f"Review for {landmark.title()}: Neutral experience.")
else:
    print("Sorry, that landmark is not in the database yet.")
