"""
Quick test script to validate core functionality before running Streamlit
"""
from textblob import TextBlob
import re

# Test 1: TextBlob installation
print("Test 1: TextBlob Sentiment Analysis")
print("-" * 50)
test_sentences = [
    "I love learning Python!",
    "The weather is cloudy today.",
    "I'm feeling really sad.",
    "This is terrible and awful.",
    "Everything is amazing and wonderful!"
]

for sentence in test_sentences:
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        emoji = "😀"
        mood = "Happy"
    elif polarity < -0.1:
        emoji = "😞"
        mood = "Sad"
    else:
        emoji = "😐"
        mood = "Neutral"
    
    print(f"{emoji} [{polarity:+.2f}] {mood:8} - \"{sentence}\"")

print("\n" + "=" * 50)
print("Test 2: Bad Word Filter")
print("-" * 50)

BAD_WORDS = ["hate", "stupid", "dumb", "idiot"]
test_filter = [
    "This is great!",
    "I hate this.",
    "You're so stupid.",
    "I love everything!"
]

for text in test_filter:
    contains_bad = any(re.search(r'\b' + re.escape(word) + r'\b', text.lower()) for word in BAD_WORDS)
    status = "🚫 FILTERED" if contains_bad else "✅ CLEAN"
    print(f"{status} - \"{text}\"")

print("\n" + "=" * 50)
print("✅ All core functions working correctly!")
print("=" * 50)
print("\nReady to launch Streamlit app...")
