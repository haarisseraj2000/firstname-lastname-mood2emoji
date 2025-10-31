"""
Kid-safe Text-Mood Detector
A simple web app for ages 12-16 that analyzes text sentiment and returns kid-friendly emojis.
"""

import streamlit as st
from textblob import TextBlob
import re
import nltk

# Download required NLTK data for TextBlob (for cloud deployment)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('brown', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

# Bad words filter (basic list - expand as needed)
BAD_WORDS = [
    "hate", "stupid", "dumb", "idiot", "kill", "die", "suck",
    "crap", "damn", "hell", "shut up"
]

def contains_bad_words(text):
    """Check if text contains inappropriate words."""
    text_lower = text.lower()
    for word in BAD_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
            return True
    return False

def analyze_mood(text):
    """
    Analyze text sentiment and return emoji + explanation.
    
    Returns:
        tuple: (emoji, explanation, polarity_score)
    """
    # Safety check
    if not text.strip():
        return "😐", "Please enter some text!", 0.0
    
    if contains_bad_words(text):
        return "😐", "Let's keep it friendly and positive!", 0.0
    
    # Use TextBlob for sentiment analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Range: -1 (negative) to +1 (positive)
    
    # Classify mood based on polarity
    if polarity > 0.1:
        emoji = "😀"
        explanation = "Sounds happy and positive!"
    elif polarity < -0.1:
        emoji = "😞"
        explanation = "Sounds sad or negative."
    else:
        emoji = "😐"
        explanation = "Sounds neutral or uncertain."
    
    return emoji, explanation, polarity

def show_teacher_mode():
    """Display educational diagram explaining how the app works."""
    st.markdown("### 🎓 How Does This Work?")
    
    st.markdown("""
    **Step-by-step process:**
    
    1. **Input**: You type a sentence
    2. **Safety Check**: Filter inappropriate words
    3. **Analysis**: TextBlob examines the words
       - Looks at positive words (happy, great, love)
       - Looks at negative words (sad, bad, hate)
       - Calculates a "polarity score" from -1 to +1
    4. **Decision**:
       - Score > 0.1 → 😀 Happy
       - Score < -0.1 → 😞 Sad
       - Otherwise → 😐 Neutral
    5. **Output**: Show emoji + explanation
    
    **What is TextBlob?**
    - A Python library for text processing
    - Uses a pre-trained model to understand sentiment
    - Analyzes word patterns and context
    
    **Example Scores:**
    - "I love this!" → +0.5 (positive)
    - "This is terrible" → -0.8 (negative)
    - "The sky is blue" → 0.0 (neutral)
    """)
    
    # Visual diagram
    st.markdown("---")
    st.markdown("**📊 Visual Flow:**")
    st.code("""
    Text Input
        ↓
    [Safety Filter]
        ↓
    [TextBlob Analysis] → Polarity Score
        ↓
    [Mood Classifier]
        ↓
    Emoji + Explanation
    """, language="text")

# Main app
def main():
    st.set_page_config(
        page_title="Mood2Emoji Detector",
        page_icon="😀",
        layout="centered"
    )
    
    st.title("😀 Mood2Emoji Detector")
    st.markdown("### Discover the mood in your words!")
    st.markdown("*A kid-safe text sentiment analyzer for ages 12-16*")
    
    # Sidebar for Teacher Mode
    with st.sidebar:
        st.header("Options")
        teacher_mode = st.checkbox("🎓 Teacher Mode", help="Show how the app works")
        
        st.markdown("---")
        st.markdown("**About**")
        st.markdown("This app uses TextBlob to analyze the mood of your text and returns a kid-friendly emoji.")
        st.markdown("Created for learning about text classification!")
    
    # Main input area
    st.markdown("---")
    user_text = st.text_area(
        "Type a sentence below:",
        placeholder="Example: I had a great day at school!",
        height=100,
        max_chars=500
    )
    
    # Analyze button
    if st.button("Analyze Mood", type="primary", use_container_width=True):
        if user_text:
            emoji, explanation, polarity = analyze_mood(user_text)
            
            # Display results with styling
            st.markdown("---")
            st.markdown("### Result:")
            
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"# {emoji}")
            with col2:
                st.markdown(f"## {explanation}")
                if polarity != 0.0 and not contains_bad_words(user_text):
                    st.caption(f"Sentiment score: {polarity:.2f}")
        else:
            st.warning("Please enter some text to analyze!")
    
    # Teacher Mode display
    if teacher_mode:
        st.markdown("---")
        show_teacher_mode()
    
    # Footer
    st.markdown("---")
    st.markdown("**Try these examples:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("😀 'I love learning Python!'")
    with col2:
        st.info("😐 'The book is on the table.'")
    with col3:
        st.info("😞 'I feel sad today.'")

if __name__ == "__main__":
    main()
