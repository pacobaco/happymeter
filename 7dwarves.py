import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import csv

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Sample corpus (replace with actual corpus loading functionality)
corpus = [
    {"id": 1, "content": "Doc is the leader of the seven dwarfs and is often portrayed as wise and knowledgeable."},
    {"id": 2, "content": "Grumpy is easily annoyed and is often pessimistic. Despite his gruff exterior, he cares deeply for his fellow dwarfs."},
    {"id": 3, "content": "Happy is cheerful and jovial, always looking on the bright side of life. His infectious laughter lifts the spirits of those around him."},
    {"id": 4, "content": "Sleepy is always tired and can fall asleep anywhere. He often yawns and struggles to stay awake during the day."},
    {"id": 5, "content": "Bashful is shy and often blushes when embarrassed. He speaks softly and tends to hide behind his hat when feeling self-conscious."},
    {"id": 6, "content": "Sneezy has hay fever and is always sneezing. His sneezes are powerful and frequent, but he remains endearing to his friends."},
    {"id": 7, "content": "Dopey is the youngest and silliest of the seven dwarfs. He communicates through gestures and facial expressions, often bringing laughter to the group."},
    {"id": 8, "content": "Doc, the leader, is respected for his intelligence and decision-making abilities. He guides the group with wisdom and clarity."},
    {"id": 9, "content": "Grumpy, though often irritable, shows a soft side when caring for injured animals in the forest."},
    {"id": 10, "content": "Happy's optimism is unwavering, even in challenging situations. He believes in finding joy in every moment."},
    {"id": 11, "content": "Sleepy's perpetual drowsiness leads to comical situations, but his gentle nature makes him a beloved member of the group."},
    {"id": 12, "content": "Bashful's shyness is endearing, and he often surprises others with acts of kindness despite his reserved demeanor."},
    {"id": 13, "content": "Sneezy's hay fever causes chaos at times, but his friends appreciate his sincerity and genuine concern for others."},
    {"id": 14, "content": "Dopey's innocence and playfulness bring a sense of joy and purity to the group, reminding them to enjoy life's simple pleasures."},
    {"id": 15, "content": "Doc takes his responsibilities seriously and ensures that everyone's opinions are considered before making decisions."},
    {"id": 16, "content": "Grumpy's grumpiness often masks his loyalty and protective nature towards his friends, whom he considers family."},
    {"id": 17, "content": "Happy spreads positivity wherever he goes, making him the heart of the group during challenging times."},
    {"id": 18, "content": "Sleepy's ability to sleep through any disturbance provides comedic relief and teaches patience to his companions."},
    {"id": 19, "content": "Bashful's bashfulness melts away in moments of bravery, where he surprises everyone, including himself."},
    {"id": 20, "content": "Sneezy's sneezes are a trademark, but his resilience and determination in overcoming challenges inspire others."},
    {"id": 21, "content": "Dopey's antics entertain and unite the dwarfs, showcasing the importance of humor and lightheartedness."},
    {"id": 22, "content": "Doc's leadership is based on fairness and wisdom, ensuring harmony among the dwarfs in all decisions."},
    {"id": 23, "content": "Grumpy's gruff exterior conceals a compassionate heart that shines through in times of adversity."},
    {"id": 24, "content": "Happy's laughter is contagious, lifting the spirits of his friends and creating a sense of camaraderie."},
    {"id": 25, "content": "Sleepy's constant need for naps leads to humorous situations, but he remains dedicated to his friends."},
    {"id": 26, "content": "Bashful's blushes reveal his vulnerability, but his courage in facing fears inspires others."},
    {"id": 27, "content": "Sneezy's sneezes are a source of amusement and concern, highlighting his unique personality."},
    {"id": 28, "content": "Dopey's innocence and curiosity bring a childlike wonder to the group, fostering a sense of adventure."},
    {"id": 29, "content": "Doc's decision-making is respected by all, ensuring the group operates smoothly and efficiently."},
    {"id": 30, "content": "Grumpy's protective instincts extend to all living creatures, demonstrating his caring nature."},
    {"id": 31, "content": "Happy's optimism is unwavering, providing hope and encouragement during challenging times."},
    {"id": 32, "content": "Sleepy's nap breaks are legendary, offering moments of rest and relaxation for the busy dwarfs."},
    {"id": 33, "content": "Bashful's quiet strength surprises his friends, proving that courage comes in quiet moments."},
    {"id": 34, "content": "Sneezy's hay fever keeps everyone on their toes, but his resilience in adversity is admired."},
    {"id": 35, "content": "Dopey's antics bring laughter and joy, reminding everyone to cherish the simple joys of life."},
    {"id": 36, "content": "Doc's leadership ensures that decisions are made with everyone's best interests in mind."},
    {"id": 37, "content": "Grumpy's protective nature extends to all creatures, showing his compassionate side."},
    {"id": 38, "content": "Happy's infectious laughter brightens the darkest days, uniting the dwarfs in joy."},
    {"id": 39, "content": "Sleepy's napping habits provide comic relief and moments of peace in a busy dwarf's life."},
    {"id": 40, "content": "Bashful's shy demeanor hides a brave heart that surprises everyone when faced with challenges."},
    {"id": 41, "content": "Sneezy's sneezes are memorable, but his determination in facing obstacles inspires others."},
    {"id": 42, "content": "Dopey's innocence and enthusiasm bring a sense of wonder and spontaneity to the group."},
    {"id": 43, "content": "Doc's wisdom and fairness make him a respected leader among the seven dwarfs."},
    {"id": 44, "content": "Grumpy's gruff exterior belies a caring nature that emerges in times of need."},
    {"id": 45, "content": "Happy's positivity uplifts the group, fostering a sense of optimism and unity."},
    {"id": 46, "content": "Sleepy's ability to nap anywhere provides comic relief and teaches patience to his friends."},
    {"id": 47, "content": "Bashful's moments of bravery surprise everyone, demonstrating courage in unexpected ways."},
    {"id": 48, "content": "Sneezy's hay fever brings challenges, but his resilience and humor make him a beloved companion."},
    {"id": 49, "content": "Dopey's playful antics bring laughter and joy to the dwarfs, reminding them of the importance of fun."},
    {"id": 50, "content": "Doc's leadership ensures that decisions are made with consideration for everyone's opinions."},
    {"id": 51, "content": "Grumpy's protective instincts extend to all creatures, showing his compassionate side."},
    {"id": 52, "content": "Happy's infectious laughter brightens the darkest days, uniting the dwarfs in joy."},
    {"id": 53, "content": "Sleepy's napping habits provide comic relief and moments of peace in a busy dwarf's life."},
    {"id": 54, "content": "Bashful's shy demeanor hides a brave heart that surprises everyone when faced with challenges."},
    {"id": 55, "content": "Sneezy's sneezes are memorable, but his determination in facing obstacles inspires others."},
    {"id": 56, "content": "Dopey's innocence and enthusiasm bring a sense of wonder and spontaneity to the group."},
    {"id": 57, "content": "Doc's wisdom and fairness make him a respected leader among the seven dwarfs."},
    {"id": 58, "content": "Grumpy's gruff exterior belies a caring nature that emerges in times of need."},
    {"id": 59, "content": "Happy's positivity uplifts the group, fostering a sense of optimism and unity."},
    {"id": 60, "content": "Sleepy's ability to nap anywhere provides comic relief and teaches patience to his friends."},
    {"id": 61, "content": "Bashful's moments of bravery surprise everyone, demonstrating courage in unexpected ways."},
    {"id": 62, "content": "Sneezy's hay fever brings challenges, but his resilience and humor make him a beloved companion."},
    {"id": 63, "content": "Dopey's playful antics bring laughter and joy to the dwarfs, reminding them of the importance of fun."},
    {"id": 64, "content": "Doc's leadership ensures that decisions are made with consideration for everyone's opinions."}]
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
keyword = "friend"
search_results = search_corpus_by_keyword(keyword, corpus)
ranked_results = rank_results_by_sentiment(search_results)

print("Ranked Search Results by Sentiment:")
for i, result in enumerate(ranked_results, start=1):
    print(f"{i}. {result['content']} - Sentiment Score: {result['sentiment_score']}")

# Export to CSV
export_to_csv(ranked_results)
