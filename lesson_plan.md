# 📘 Lesson Plan: Build a Mood2Emoji App
## Introduction to Text Classification for Ages 12–16

---

## 📋 Lesson Overview

**Topic**: Building a Mood2Emoji Text Sentiment Analyzer  
**Target Audience**: Students aged 12–16  
**Duration**: 60 minutes  
**Difficulty Level**: Beginner to Intermediate  
**Prerequisites**: Basic Python knowledge (variables, functions, if/else statements)

### Learning Goals
By the end of this lesson, students will be able to:
1. Explain what sentiment analysis is and why it's useful
2. Understand how computers classify text into categories
3. Identify the key components of a text classification system
4. Modify and experiment with a working sentiment analyzer
5. Discuss ethical considerations in emotion-detecting AI

---

## 📚 Topics Introduced

### Primary Concepts
1. **Sentiment Analysis**
   - Definition: The process of determining emotional tone from text
   - Real-world applications
   - Limitations and challenges

2. **Text Classification**
   - What classification means in computer science
   - Categories vs. continuous values
   - Decision-making with thresholds

3. **Natural Language Processing (NLP)**
   - How computers understand human language
   - Libraries that make NLP accessible
   - The difference between rule-based and machine learning approaches

4. **Polarity Scoring**
   - Positive vs. negative sentiment
   - Numerical representation of emotions (-1 to +1)
   - Neutral/ambiguous text handling

5. **Content Safety & Filtering**
   - Why filtering matters for kid-safe applications
   - Simple pattern matching techniques
   - Limitations of automated filtering

### Technical Skills
- Using Python libraries (Streamlit, TextBlob)
- Reading and understanding existing code
- Modifying parameters to change behavior
- Testing and experimentation
- Basic debugging

### Soft Skills
- Critical thinking about AI limitations
- Ethical reasoning about emotion detection
- Collaborative problem-solving
- Communicating technical concepts

---

## 📖 Topics in Detail

### 1. Sentiment Analysis Fundamentals

**What It Is**:
Sentiment analysis (also called opinion mining) is the computational study of people's emotions, opinions, and attitudes expressed in text.

**How It Works**:
- **Lexicon-based approach** (what we use): A dictionary of words with pre-assigned sentiment scores
  - "happy" = +0.8
  - "sad" = -0.7
  - "okay" = 0.0
- **Machine learning approach**: Training AI models on thousands of labeled examples

**Real-World Examples**:
- Social media platforms detecting hate speech
- Companies analyzing customer reviews
- Email spam filters
- Chatbots understanding user frustration
- Political campaigns measuring public opinion

**Why It Matters**:
- Helps businesses improve products
- Enables personalized user experiences
- Can identify mental health concerns
- Powers content moderation systems

---

### 2. TextBlob Library Deep Dive

**What is TextBlob?**
- A Python library for processing textual data
- Built on top of NLTK (Natural Language Toolkit)
- Provides a simple API for common NLP tasks

**How TextBlob Analyzes Sentiment**:
```python
from textblob import TextBlob

text = "I love this amazing app!"
blob = TextBlob(text)
print(blob.sentiment)
# Output: Sentiment(polarity=0.625, subjectivity=0.6)
```

**Understanding the Output**:
- **Polarity**: -1.0 (most negative) to +1.0 (most positive)
- **Subjectivity**: 0.0 (objective/factual) to 1.0 (subjective/opinion)

**TextBlob's Word Database**:
- Contains ~5,000 words with sentiment scores
- Based on human ratings and linguistic patterns
- Example words and scores:
  - "excellent" → +0.8
  - "terrible" → -0.7
  - "good" → +0.4
  - "bad" → -0.5

**Limitations**:
- Doesn't understand sarcasm ("Yeah, right, that's just great!")
- Context-dependent words confuse it ("sick" can mean ill or awesome)
- Cultural differences in language
- Slang and new words not in database

---

### 3. Decision Logic & Thresholds

**What Are Thresholds?**
Boundaries that determine which category something belongs to.

**In Our App**:
```python
if polarity > 0.1:
    emoji = "😀"  # Happy
elif polarity < -0.1:
    emoji = "😞"  # Sad
else:
    emoji = "😐"  # Neutral
```

**Why 0.1 and -0.1?**
- Provides a "buffer zone" around zero
- Text scoring between -0.1 and 0.1 is ambiguous
- Prevents misclassifying slightly-worded neutral text

**Experimenting with Thresholds**:
- **Higher threshold** (0.3): Only very positive text gets 😀
- **Lower threshold** (0.05): More text classified as happy/sad
- **Zero threshold** (0.0): No neutral zone at all

**Activity**: Students adjust thresholds and document how results change

---

### 4. Building User Interfaces with Streamlit

**What is Streamlit?**
- A Python framework for creating web apps
- No HTML/CSS/JavaScript required
- Perfect for data science and ML projects

**Key Components We Use**:
```python
st.title("My App")              # Large heading
st.text_area("Enter text")      # Input box
st.button("Click me")           # Button
st.markdown("**Bold text**")    # Formatted text
st.sidebar.checkbox("Option")   # Sidebar widget
```

**Why Streamlit?**
- Fast prototyping (build apps in minutes)
- Interactive by default
- Great for educational demos
- Easy to share and deploy

---

### 5. Safety & Ethics in AI

**Why Content Filtering?**
- Protects young users from harmful content
- Prevents misuse of technology
- Creates positive learning environment
- Teaches responsible tech design

**Our Simple Filter**:
```python
BAD_WORDS = ["hate", "stupid", "dumb", "idiot"]

if any(bad_word in text.lower() for bad_word in BAD_WORDS):
    return "😐", "Let's keep it friendly!"
```

**Limitations of Our Filter**:
- Doesn't catch misspellings ("st00pid")
- Context matters ("I hate when it rains" vs. hate speech)
- Different communities have different standards
- Over-filtering can censor legitimate content

**Ethical Discussion Points**:
- Should AI be able to "read" our emotions?
- Who decides what's appropriate?
- What if the AI makes mistakes?
- Privacy concerns with text analysis
- Bias in training data

---

## ⏱ 60-Minute Lesson Timeline

### **Phase 1: Introduction (0–10 minutes)**

#### Minute 0–2: Hook & Engagement
- **Activity**: Show students three text messages and ask them to rate the mood
  - "I can't believe I won the contest!"
  - "The book is on the table."
  - "This is the worst day ever."
- **Purpose**: Establish that humans naturally detect sentiment

#### Minute 2–5: Demo the App
- **Activity**: Live demo of Mood2Emoji
  - Type several example sentences
  - Show the emoji + explanation output
  - Toggle Teacher Mode on/off
- **Purpose**: Show what students will understand by lesson end

#### Minute 5–10: Big Picture Discussion
- **Questions**:
  - "How do you think a computer knows if text is happy or sad?"
  - "Where have you seen this technology before?"
- **Introduce Key Terms**: sentiment, polarity, classification, AI
- **Set Expectations**: We're learning how this works and experimenting with it

---

### **Phase 2: Understanding the System (10–20 minutes)**

#### Minute 10–12: Enable Teacher Mode
- **Activity**: Walk through the Teacher Mode diagram together
- **Focus**: The 5-step process (Input → Safety → Analysis → Decision → Output)

#### Minute 12–17: Polarity Score Exploration
- **Activity**: Prediction game
  - Show 10 sentences on screen
  - Students predict: Happy (😀), Neutral (😐), or Sad (😞)
  - Reveal actual TextBlob scores
  - Discuss surprises or disagreements

**Example Sentences**:
1. "I absolutely adore chocolate ice cream!" (Expected: 😀)
2. "I'm walking to the store." (Expected: 😐)
3. "That movie was incredibly boring." (Expected: 😞)
4. "This is fine." (Neutral or slightly positive?)
5. "I'm so excited I can't sleep!" (Expected: 😀)
6. "He's not bad at math." (Double negative - tricky!)
7. "Whatever." (Neutral but dismissive tone?)
8. "OMG this is amazing!!!!" (Very positive with emphasis)
9. "I failed the test." (Expected: 😞)
10. "The experiment results were unexpected." (Objective/neutral)

#### Minute 17–20: TextBlob Explanation
- **Concept**: TextBlob uses a word database
- **Analogy**: "Like a dictionary where each word has a happiness score"
- **Show Examples**:
  - "love" = +0.5
  - "hate" = -0.8
  - "okay" = 0.0
- **Key Point**: Computers don't "feel" emotions—they calculate scores

---

### **Phase 3: Code Exploration (20–35 minutes)**

#### Minute 20–25: Code Structure Overview
- **Activity**: Open `app.py` in a code editor
- **Walkthrough** (don't go line-by-line—focus on big chunks):
  1. **Import libraries** (top)
  2. **Bad words filter function**
  3. **Mood analysis function** (the main logic)
  4. **Teacher Mode function**
  5. **User interface code**

#### Minute 25–30: Deep Dive into Key Functions

**Focus Area 1: Safety Filter**
```python
def contains_bad_words(text):
    text_lower = text.lower()
    for word in BAD_WORDS:
        if word in text_lower:
            return True
    return False
```
- **Explain**: Loops through list, checks if any bad words are present
- **Question**: "What words would you add to make this safer?"

**Focus Area 2: Mood Analysis**
```python
blob = TextBlob(text)
polarity = blob.sentiment.polarity

if polarity > 0.1:
    emoji = "😀"
```
- **Explain**: Create TextBlob object, get polarity, use thresholds
- **Highlight**: The 0.1 threshold creates a neutral zone

#### Minute 30–35: Hands-On Modification
- **Activity**: Students modify thresholds
  - Change `0.1` to `0.3` and `0.5`
  - Run the app after each change
  - Test with the same sentences
  - Document how results differ

**Worksheet**:
| Sentence | 0.1 Threshold | 0.3 Threshold | 0.5 Threshold |
|----------|---------------|---------------|---------------|
| "I love this!" | 😀 | ? | ? |
| "It's pretty good." | 😀 | ? | ? |

---

### **Phase 4: Experimentation (35–50 minutes)**

#### Minute 35–40: Edge Case Testing
- **Activity**: Students work in pairs to find "problem sentences"
- **Goal**: Find text that the app handles poorly

**Testing Ideas**:
1. **Sarcasm**: "Oh great, another test. Just what I needed."
2. **Mixed emotions**: "I'm happy but also nervous about the presentation."
3. **ALL CAPS**: "I LOVE THIS!" vs. "I love this!"
4. **Punctuation**: "I'm so excited!!!!!!" vs. "I'm so excited."
5. **Negations**: "This isn't bad." vs. "This is bad."
6. **Neutral facts**: "Water boils at 100 degrees Celsius."

**Discussion**: Why do these confuse the AI?

#### Minute 40–45: Extension Challenges
- **Activity**: Students choose one enhancement to design (not necessarily code)

**Options**:
1. **More Emojis**: Add 😍 (very happy) and 😱 (very sad)
2. **Confidence Score**: Show how "sure" the AI is
3. **Word Highlighting**: Color positive words green, negative red
4. **Multilingual**: Make it work in Spanish or French
5. **Emotion Variety**: Detect anger, surprise, fear (not just happy/sad)
6. **Better Filter**: Improve the safety filter

**Deliverable**: Write pseudocode or draw a flowchart

#### Minute 45–50: Share & Discuss
- **Activity**: 3–4 students share their extension ideas
- **Class Feedback**: What would be challenging? What would be most useful?

---

### **Phase 5: Reflection & Real-World Connections (50–60 minutes)**

#### Minute 50–55: Critical Thinking Discussion

**Question 1**: "Where have you encountered sentiment analysis?"
- Possible answers: YouTube comments, social media, customer reviews, chatbots

**Question 2**: "What could go wrong with emotion-detecting AI?"
- Privacy concerns
- Misunderstanding cultural differences
- False accusations (detecting "hate" where there is none)
- Missing real problems (not detecting actual harmful content)

**Question 3**: "Should companies use AI to analyze your social media posts?"
- Debate: Benefits (safety, personalization) vs. Risks (privacy, surveillance)

**Question 4**: "How is our simple app different from 'real' AI?"
- We use a fixed word list
- Advanced systems learn from data
- Our app doesn't understand context

#### Minute 55–60: Takeaway & Assignment

**Key Takeaways** (review):
1. Computers classify text by analyzing word patterns
2. TextBlob uses a word database with sentiment scores
3. Thresholds help make decisions from continuous scores
4. AI isn't perfect—it has limitations
5. We must consider ethics and safety in tech design

**Homework Assignment**:
1. **Prediction Exercise**: Write 5 sentences, predict their polarity scores, then test
2. **Research Task**: Find one real-world use of sentiment analysis (news article or company)
3. **Design Challenge**: Sketch a new feature for Mood2Emoji (draw or describe)

**Bonus Challenge**:
- Modify the code to add a 4th emoji (choose 😍 or 😱)
- Update the threshold logic
- Test and screenshot your results

---

## 🎯 Learning Outcomes

By completing this lesson, students will demonstrate:

### Knowledge (Understanding)
- [ ] Define sentiment analysis and explain its purpose
- [ ] Describe how TextBlob analyzes text polarity
- [ ] Explain the role of thresholds in classification
- [ ] Identify limitations of simple sentiment analyzers

### Skills (Application)
- [ ] Run a Streamlit web app locally
- [ ] Read and interpret existing Python code
- [ ] Modify threshold values to change app behavior
- [ ] Test edge cases and identify failure modes
- [ ] Use Teacher Mode to understand system internals

### Analysis (Critical Thinking)
- [ ] Compare human emotion detection vs. AI
- [ ] Evaluate when sentiment analysis is appropriate
- [ ] Analyze why certain sentences confuse the AI
- [ ] Assess ethical implications of emotion-detecting technology

### Creativity (Extension)
- [ ] Design new features for the app
- [ ] Propose improvements to the safety filter
- [ ] Create test cases to challenge the system
- [ ] Imagine novel applications for sentiment analysis

---

## 📊 Assessment Rubric

### Participation & Engagement (20 points)
- Active participation in discussions (5 pts)
- Testing examples during demos (5 pts)
- Pair work collaboration (5 pts)
- Asking thoughtful questions (5 pts)

### Hands-On Activity (30 points)
- Successfully modified threshold values (10 pts)
- Documented changes in results (10 pts)
- Tested at least 3 edge cases (10 pts)

### Conceptual Understanding (30 points)
- Explains sentiment analysis clearly (10 pts)
- Understands polarity scores (10 pts)
- Identifies AI limitations (10 pts)

### Homework Completion (20 points)
- 5 prediction sentences (5 pts)
- Real-world research (10 pts)
- Feature design sketch/description (5 pts)

**Total: 100 points**

---

## 🛠 Teacher Preparation Checklist

### Before Class
- [ ] Install Python 3.9+ on classroom computers
- [ ] Pre-install Streamlit and TextBlob on all machines
- [ ] Run `python -m textblob.download_corpora` on each computer
- [ ] Test that the app runs successfully
- [ ] Prepare example sentences on slides
- [ ] Print edge case testing worksheet
- [ ] Set up screen sharing/projector

### Materials Needed
- [ ] Computers with internet (1 per student or pair)
- [ ] Projector for demonstrations
- [ ] Printed worksheets for threshold experiments
- [ ] Whiteboard/markers for diagramming
- [ ] Timer for activity transitions

### Optional Enhancements
- [ ] Create Kahoot quiz for key concepts
- [ ] Prepare video showing real-world sentiment analysis
- [ ] Print vocabulary cards (polarity, threshold, NLP, etc.)
- [ ] Set up a shared Google Doc for students to post findings

---

## 🔄 Differentiation Strategies

### For Advanced Students
- **Challenge 1**: Add subjectivity scores (not just polarity)
- **Challenge 2**: Create a sentiment history graph
- **Challenge 3**: Build a custom word database from scratch
- **Challenge 4**: Research machine learning alternatives to TextBlob

### For Struggling Students
- **Simplification 1**: Focus on using the app, not modifying code
- **Simplification 2**: Provide sentence templates for homework
- **Simplification 3**: Pair with a peer mentor
- **Simplification 4**: Use visual aids (flowcharts, emoji cards)

### For Visual Learners
- Draw the polarity number line (-1 to +1) on board
- Use color coding (green=positive, red=negative, yellow=neutral)
- Create physical emoji cards for voting activities

### For Kinesthetic Learners
- Act out different emotions while reading sentences
- Use hand gestures (thumbs up/down) for polarity predictions
- Move around room for "emoji corners" activity

---

## 📚 Extension Activities

### For Next Class
1. **Emoji Sentiment Art**: Students create posters mapping words to emojis
2. **Bias Detective**: Analyze if TextBlob is biased toward certain topics
3. **Cultural Comparison**: Compare sentiment in English vs. translated text
4. **Build Your Own**: Create a rule-based classifier without TextBlob

### Cross-Curricular Connections
- **English/Language Arts**: Analyze sentiment in literature (poems, speeches)
- **Social Studies**: Track sentiment in historical documents
- **Math**: Calculate average polarity across multiple texts
- **Science**: Sentiment analysis of research paper abstracts

---

## 📖 Additional Resources

### For Teachers
- TextBlob Documentation: https://textblob.readthedocs.io/
- Sentiment Analysis Overview: https://en.wikipedia.org/wiki/Sentiment_analysis
- AI Ethics for Educators: https://aiedu.org/

### For Students
- "How Computers Understand Text" (video): [Create custom link]
- Emoji History: https://home.unicode.org/emoji/
- Python for Beginners: https://www.python.org/about/gettingstarted/

### Related Projects to Explore
- Build a spam detector
- Create a chatbot with moods
- Analyze tweets about a topic
- Make a "compliment generator"

---

## ❓ Anticipated Student Questions & Answers

**Q: "Can the AI actually feel emotions?"**  
A: No, it only calculates scores based on word patterns. It doesn't have feelings.

**Q: "Why does it get sarcasm wrong?"**  
A: Sarcasm requires understanding context and tone, which is very hard for computers.

**Q: "What if I use emojis in my input?"**  
A: TextBlob focuses on words, so emojis might be ignored or cause unexpected results. Try it!

**Q: "Could this be used to spy on people's messages?"**  
A: Technically yes, which is why we discuss ethics. Privacy is important.

**Q: "Is TextBlob always right?"**  
A: No, like all AI, it makes mistakes. That's why we test it and understand its limits.

**Q: "Can I use this in other languages?"**  
A: TextBlob works best with English. Other languages need different tools or translation.

---

## 🎓 Teacher Notes

### Common Pitfalls
- Students may think AI "thinks" like humans—reinforce it's pattern matching
- Some may focus too much on perfect accuracy—emphasize learning process
- Advanced students may want to jump into complex ML—keep it accessible
- Discussions about bad words can get silly—maintain focus on learning

### Success Indicators
- Students explain concepts in their own words
- They test creative edge cases
- Ethical questions arise naturally
- Students want to modify/extend the project

### Timing Flexibility
- If short on time: Skip extension challenges, focus on core concepts
- If extra time: Add group presentations, deeper code walkthrough, or live coding demo

---

## 📝 Homework Answer Key

### Prediction Exercise Example
| Sentence | Prediction | Actual Polarity | Emoji | Notes |
|----------|-----------|----------------|-------|-------|
| "I love this app!" | Positive | +0.5 | 😀 | "love" is strong positive |
| "It's okay." | Neutral | 0.0 | 😐 | "okay" is neutral |
| "This is terrible." | Negative | -0.7 | 😞 | "terrible" is strong negative |
| "I'm excited but nervous." | Mixed | +0.1 | 😀 | Mixed emotions confuse AI |
| "The sky is blue." | Neutral | 0.0 | 😐 | Factual statement |

---

## 🌟 Conclusion

This lesson introduces students to a fundamental AI concept—sentiment analysis—through hands-on exploration. By building, testing, and critiquing a real working app, students gain both technical skills and critical thinking abilities essential for the AI age.

The Mood2Emoji project is intentionally simple to ensure accessibility while still revealing complex ideas about how computers process language. Most importantly, it sparks curiosity and ethical reflection about the technology shaping our world.

**Happy Teaching!** 🚀

---

**Document Version**: 1.0  
**Last Updated**: October 2025  
**Created for**: Mood2Emoji Educational Project
