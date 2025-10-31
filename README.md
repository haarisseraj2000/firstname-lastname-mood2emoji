# 😀 Mood2Emoji Detector

A kid-safe text sentiment analyzer for ages 12–16. This web app takes a sentence and returns a kid-friendly emoji (😀 😐 😞) with a simple explanation, teaching students the basics of text classification and natural language processing.

---

## 📋 Table of Contents
- [What This Project Does](#what-this-project-does)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Features](#features)
- [How Students Learn From This](#how-students-learn-from-this)
- [60-Minute Teaching Guide](#60-minute-teaching-guide)
- [Known Limitations](#known-limitations)
- [Technical Details](#technical-details)
- [Credits](#credits)

---

## 🎯 What This Project Does

**Mood2Emoji** analyzes the sentiment (mood) of text input and displays:
- A **kid-friendly emoji** representing the mood (😀 happy, 😐 neutral, 😞 sad)
- A **short explanation** of the detected mood
- An optional **Teacher Mode** that shows how the app works behind the scenes

The app uses **TextBlob**, a Python library for natural language processing, to analyze sentiment polarity (how positive or negative the text is). All content is filtered for age-appropriateness.

---

## 🛠 Setup Instructions

### Prerequisites
- **Python 3.9+** installed on your system
- **pip** (Python package installer)
- Basic command line knowledge

### Installation Steps

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd firstname-lastname-mood2emoji
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download TextBlob data** (one-time setup)
   ```bash
   python -m textblob.download_corpora
   ```

---

## 🚀 How to Run

1. **Activate your virtual environment** (if not already active)
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't, copy the URL from the terminal

4. **Use the app**
   - Type a sentence in the text box
   - Click "Analyze Mood"
   - See your emoji result!
   - Toggle "Teacher Mode" in the sidebar to learn how it works

---

## ✨ Features

- **Simple Interface**: Clean, kid-friendly design
- **Real-time Analysis**: Instant mood detection
- **Safety First**: Filters inappropriate words
- **Educational Mode**: Teacher Mode explains the logic
- **Visual Feedback**: Clear emoji + text explanations
- **Example Sentences**: Built-in examples to try

---

## 🎓 How Students Learn From This

### Core Learning Objectives

1. **Introduction to AI/ML**
   - Understand what sentiment analysis is
   - See how computers "read" and understand text
   - Learn about positive/negative word associations

2. **Text Classification Basics**
   - Discover how text gets categorized
   - Understand polarity scores (-1 to +1)
   - See decision-making with thresholds

3. **Python Programming**
   - Work with real libraries (Streamlit, TextBlob)
   - Understand functions and control flow
   - Learn basic web app structure

4. **Safety & Ethics**
   - Importance of content filtering
   - Designing age-appropriate tech
   - Responsible AI considerations

5. **Real-World Applications**
   - Social media mood detection
   - Customer feedback analysis
   - Chatbot emotion understanding

---

## ⏱ 60-Minute Teaching Guide

### Lesson Plan Overview
**Target Audience**: Ages 12–16  
**Duration**: 60 minutes  
**Prerequisites**: Basic understanding of Python (variables, functions, if/else)

### Minute-by-Minute Breakdown

#### **Minutes 0–10: Introduction & Demo**
- **Activity**: Launch the app and demonstrate with example sentences
- **Discussion**: "How do you think the computer knows if text is happy or sad?"
- **Key Points**:
  - Computers can analyze patterns in words
  - Different words have different "moods"
  - We're building our own mood detector today!

#### **Minutes 10–20: How It Works (Teacher Mode)**
- **Activity**: Enable Teacher Mode and walk through the diagram
- **Concepts Introduced**:
  - Input → Processing → Output flow
  - Safety filtering (why it matters)
  - Polarity scores and thresholds
  - TextBlob library overview
- **Interactive**: Ask students to predict scores for different sentences

#### **Minutes 20–35: Code Walkthrough**
- **Activity**: Open `app.py` and explain key sections
- **Topics Covered**:
  1. **Safety Filter** (lines 16–22): How bad word detection works
  2. **Mood Analysis** (lines 24–53): The TextBlob magic
  3. **Decision Logic** (lines 42–51): If/elif/else for emoji selection
  4. **User Interface** (lines 101–167): Streamlit components

- **Hands-on**: Students modify the polarity thresholds (change 0.1 to 0.2) and observe differences

#### **Minutes 35–50: Experiments & Extensions**
- **Activity**: Students test edge cases and brainstorm improvements
- **Experiments**:
  - Test sentences with mixed emotions
  - Try ALL CAPS vs. lowercase
  - Add punctuation (!!!) and see effects
  - Test borderline neutral cases

- **Extension Ideas**:
  - Add more emojis (😱 for very negative, 😍 for very positive)
  - Expand the bad words filter
  - Add a "confidence level" display
  - Create different modes (formal vs. casual text)

#### **Minutes 50–60: Reflection & Real-World Connections**
- **Discussion Questions**:
  - Where have you seen sentiment analysis in real life?
  - What could go wrong with mood detection?
  - How might different cultures interpret emojis differently?
  - Should AI always be able to read our emotions?

- **Takeaway Assignment**:
  - Write 5 sentences and predict their polarity scores
  - Research one real-world use of sentiment analysis
  - Design a new feature for the app

### Teaching Tips
- **Differentiation**: Advanced students can modify code; beginners can focus on concepts
- **Visual Learners**: Draw the flow diagram on a whiteboard
- **Group Work**: Pairs can test each other's sentences
- **Vocabulary**: Define "sentiment," "polarity," "classification" clearly

---

## ⚠️ Known Limitations

### Technical Limitations
1. **Simple Sentiment Model**
   - TextBlob uses basic lexicon-based analysis
   - Doesn't understand sarcasm or complex context
   - May misclassify nuanced emotions

2. **Limited Safety Filter**
   - Basic bad words list (not comprehensive)
   - Doesn't catch all inappropriate content
   - May miss creative misspellings or slang

3. **English Only**
   - TextBlob primarily supports English
   - Other languages may produce incorrect results

4. **Fixed Thresholds**
   - Polarity boundaries (±0.1) are arbitrary
   - Some neutral text might be misclassified

### Pedagogical Notes
- This is a **learning tool**, not production software
- Emphasize that AI isn't perfect
- Use limitations as discussion points about AI ethics

### Potential Improvements
- Add multilingual support
- Implement more sophisticated filtering
- Allow customizable sensitivity settings
- Include subjectivity scores
- Add emotion variety (anger, surprise, fear)

---

## 🔧 Technical Details

### Dependencies
- **Streamlit 1.29.0**: Web app framework
- **TextBlob 0.17.1**: NLP library for sentiment analysis

### How TextBlob Works
- Uses a **pre-trained sentiment classifier**
- Analyzes word polarity from a lexicon
- Returns:
  - `polarity`: -1 (negative) to +1 (positive)
  - `subjectivity`: 0 (objective) to 1 (subjective)

### File Structure
```
firstname-lastname-mood2emoji/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── lesson_plan.pdf    # Detailed lesson plan for educators
└── QUESTIONS.md       # Optional clarification questions
```

### Customization Guide
**Change emoji thresholds:**
```python
# In app.py, lines 43-51
if polarity > 0.2:  # Was 0.1 - now requires stronger positive sentiment
    emoji = "😀"
```

**Add new emojis:**
```python
if polarity > 0.5:
    emoji = "😍"
    explanation = "Very excited and happy!"
elif polarity > 0.1:
    emoji = "😀"
    explanation = "Sounds happy and positive!"
```

---

## 📚 Credits

### References
- **TextBlob Documentation**: https://textblob.readthedocs.io/
- **Streamlit Documentation**: https://docs.streamlit.io/
- **Sentiment Analysis Basics**: Pattern library (TextBlob's underlying model)

### Original Work
All code is original and created specifically for educational purposes. The app uses publicly available open-source libraries (TextBlob, Streamlit) under their respective licenses.

### No External APIs
This project runs entirely locally and does not require paid external services.

---

## 📝 License & Usage

This project is designed for **educational use** in classroom settings. Feel free to:
- Use it in teaching
- Modify for your curriculum
- Share with students and colleagues

---

## 🎉 Try It Out!

**Example Sentences to Test:**
- "I absolutely love learning new things!" → 😀
- "The weather is cloudy today." → 😐
- "I'm feeling really down and sad." → 😞
- "This homework is awesome and fun!" → 😀
- "I don't know what to think about this." → 😐

---

## 📧 Questions?

Check `QUESTIONS.md` for common questions and clarifications, or refer to the `lesson_plan.pdf` for detailed teaching instructions.

**Happy Teaching & Learning! 🚀**
