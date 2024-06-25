import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import csv

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Sample corpus (replace with actual corpus loading functionality)
corpus = [
    {"id": 1, "content": "Doc is the leader of the seven dwarfs and is often portrayed as wise and knowledgeable."},
    {"id": 2, "content": "Grumpy is easily annoyed and is often pessimistic."},
    {"id": 3, "content": "Happy is cheerful and jovial, always looking on the bright side of life."},
    {"id": 4, "content": "Sleepy is always tired and can fall asleep anywhere."},
    {"id": 5, "content": "Bashful is shy and often blushes when embarrassed."},
    {"id": 6, "content": "Sneezy has hay fever and is always sneezing."},
    {"id": 7, "content": "Dopey is the youngest and silliest of the seven dwarfs."}
]

def search_corpus_by_keyword(keyword, corpus):
    results = [doc for doc in corpus if keyword.lower() in doc['content'].lower()]
    return results

def analyze_sentiment(content):
    return sid.polarity_scores(content)["compound"]

def rank_results_by_sentiment(results):
    for result in results:
        result['sentiment_score'] = analyze_sentiment(result['content'])
    ranked_results = sorted(results, key=lambda x: x['sentiment_score'], reverse=True)
    return ranked_results

def export_to_csv(ranked_results, filename='ranked_results.csv'):
    keys = ranked_results[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(ranked_results)

# Example usage
keyword = "happy"
search_results = search_corpus_by_keyword(keyword, corpus)
ranked_results = rank_results_by_sentiment(search_results)

print("Ranked Search Results by Sentiment:")
for i, result in enumerate(ranked_results, start=1):
    print(f"{i}. {result['content']} - Sentiment Score: {result['sentiment_score']}")

# Export to CSV
export_to_csv(ranked_results)
