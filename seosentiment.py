import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from nltk.tokenize import word_tokenize
import random

nltk.download('movie_reviews')
nltk.download('punkt')

def extract_features(words):
    return dict([(word, True) for word in words])

# Load movie reviews dataset
movie_reviews_data = [(list(movie_reviews.words(fileid)), category)
                      for category in movie_reviews.categories()
                      for fileid in movie_reviews.fileids(category)]

# Shuffle the data
random.shuffle(movie_reviews_data)

# Create feature sets
feature_sets = [(extract_features(words), category) for (words, category) in movie_reviews_data]

# Split data into training and testing datasets
train_data, test_data = feature_sets[0:1600], feature_sets[1600:]

# Train the classifier
classifier = NaiveBayesClassifier.train(train_data)

# Evaluate the classifier
print(f'Accuracy: {nltk_accuracy(classifier, test_data):.2f}')
classifier.show_most_informative_features(10)

def analyze_sentiment(text):
    words = word_tokenize(text)
    features = extract_features(words)
    return classifier.classify(features)

# Test the sentiment analyzer
sample_text = "This product is amazing! I absolutely love it."
print(f'Sentiment: {analyze_sentiment(sample_text)}')
