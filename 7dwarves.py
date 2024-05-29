import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Sample descriptions of the 7 dwarves
dwarves_descriptions = {
    "Doc": "Doc is the leader of the seven dwarfs and is often portrayed as wise and knowledgeable.",
    "Grumpy": "Grumpy is easily annoyed and is often pessimistic.",
    "Happy": "Happy is cheerful and jovial, always looking on the bright side of life.",
    "Sleepy": "Sleepy is always tired and can fall asleep anywhere.",
    "Bashful": "Bashful is shy and often blushes when embarrassed.",
    "Sneezy": "Sneezy has hay fever and is always sneezing.",
    "Dopey": "Dopey is the youngest and silliest of the seven dwarfs."
}

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Calculate sentiment scores for each dwarf
sentiment_scores = {}
for dwarf, description in dwarves_descriptions.items():
    sentiment_scores[dwarf] = sid.polarity_scores(description)["compound"]

# Rank dwarves by sentiment score
ranked_dwarves = sorted(sentiment_scores.items(), key=lambda x: x[1], reverse=True)

# Print the ranked dwarves
print("Ranked Dwarves by Sentiment:")
for i, (dwarf, score) in enumerate(ranked_dwarves, start=1):
    print(f"{i}. {dwarf}: {score}")
