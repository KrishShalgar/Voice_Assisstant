import collections
import matplotlib.pyplot as plt
import calendar
from typing import List

def analyze_time_queries(time_queries: List):
    if not time_queries:
        print("No time queries to analyze.")
        return
    hours = [t.hour for t in time_queries]
    plt.hist(hours, bins=24, range=(0,24), align="left")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Frequency")
    plt.title("Time Distribution of Queries")
    plt.show()

def analyze_query_lengths(lengths: List[int]):
    if not lengths:
        print("No query lengths to analyze.")
        return
    plt.hist(lengths, bins=20)
    plt.xlabel("Query Length")
    plt.ylabel("Frequency")
    plt.title("Distribution of Query Lengths")
    plt.show()

def analyze_query_words(words: List[str]):
    if not words:
        print("No query words to analyze.")
        return
    counts = collections.Counter(words)
    labels, values = zip(*counts.most_common(25))  # top 25 words
    plt.bar(labels, values)
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.title("Top Query Words")
    plt.xticks(rotation=45)
    plt.show()

def analyze_user_intents(user_intents: List[str]):
    if not user_intents:
        print("No user intents to analyze.")
        return
    counts = collections.Counter(user_intents)
    labels, values = zip(*counts.items())
    plt.bar(labels, values)
    plt.xlabel("User Intent")
    plt.ylabel("Frequency")
    plt.title("Distribution of User Intents")
    plt.xticks(rotation=45)
    plt.show()

def analyze_query_length_vs_word_count(query_texts: List[str]):
    if not query_texts:
        print("No query texts to analyze.")
        return
    pairs = [(len(q), len(q.split())) for q in query_texts]
    xs, ys = zip(*pairs)
    plt.scatter(xs, ys)
    plt.xlabel("Query Length")
    plt.ylabel("Word Count")
    plt.title("Query Length vs. Word Count")
    plt.show()
