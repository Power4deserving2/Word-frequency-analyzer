import re
from collections import Counter
import matplotlib.pyplot as plt

# Stop words list (can be expanded)
STOP_WORDS = set([
    "the", "a", "and", "of", "in", "on", "for", "is", "to", "but", "been", "have", "has", "are", "with", "was", "an"
])

def clean_and_tokenize(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation (preserve hyphens), replace with space
    text = re.sub(r"[^\w\s-]", "", text)
    # Split into words
    words = text.split()
    # Filter out stop words
    return [word for word in words if word not in STOP_WORDS]

def analyze_text(text):
    words = clean_and_tokenize(text)
    word_counts = Counter(words)

    # Word frequencies
    print("Word frequencies:")
    for word, count in word_counts.items():
        print(f"- {word}: {count}")

    print("\nTop 5 most common words:")
    for i, (word, count) in enumerate(word_counts.most_common(5), start=1):
        print(f"{i}. {word} ({count})")

    # Words that appear only once
    unique_words = [word for word, count in word_counts.items() if count == 1]
    print("\nWords that appear exactly once:")
    print(", ".join(unique_words))

    # Visualization
    plot_word_frequencies(word_counts)

def plot_word_frequencies(word_counts):
    top_items = word_counts.most_common(10)
    words, freqs = zip(*top_items)

    plt.figure(figsize=(10, 6))
    plt.bar(words, freqs)
    plt.title("Top 10 Word Frequencies")
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.grid(axis='y')
    plt.show()
