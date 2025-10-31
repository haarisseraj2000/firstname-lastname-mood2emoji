# 😀 Mood2Emoji Detector

A simple text mood analyzer I built for middle and high school students (ages 12-16). Type in a sentence, and it tells you if it's happy 😀, neutral 😐, or sad 😞. It's basically a fun way to learn how computers understand emotions in text.

---

## What Does This Thing Do?

So basically, **Mood2Emoji** reads whatever text you give it and figures out the mood. Then it shows you:
- An emoji that matches the vibe (😀 😐 😞)
- A quick explanation of why it picked that mood
- There's also a Teacher Mode if you want to see what's happening behind the scenes

I'm using this Python library called **TextBlob** to do the heavy lifting. It analyzes how positive or negative your text is, which is pretty cool when you see it in action. I also added some basic filtering to keep things appropriate for younger students.

---

## Getting Started

### What You'll Need
- Python 3.9 or higher (check with `python --version`)
- pip (usually comes with Python)
- Know how to use terminal/command prompt at least a little bit

### Setting Everything Up

1. **Grab the code**
```bash
   git clone https://github.com/haarisseraj2000/mood2emoji
   cd mood2emoji
```

2. **Make a virtual environment** (trust me, this keeps things clean)
```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install the packages**
```bash
   pip install -r requirements.txt
```

4. **Download TextBlob's data** (you only need to do this once)
```bash
   python -m textblob.download_corpora
```

---

## Running the App

1. **Turn on your virtual environment** (if you closed terminal)
```bash
   # Windows
   venv\Scripts\activate

   # Mac/Linux
   source venv/bin/activate
```

2. **Start it up**
```bash
   streamlit run app.py
```

3. **Check it out in your browser**
   - Should open automatically at `http://localhost:8501`
   - If not, just copy the URL from your terminal

4. **Play around with it**
   - Type anything in the text box
   - Hit "Analyze Mood"
   - See what emoji you get!
   - Turn on Teacher Mode in the sidebar to see how it actually works

---

## Cool Features I Added

- **Super Simple Design**: Made it clean so kids won't get confused
- **Works Instantly**: You get results right away
- **Safe Content**: Filters out inappropriate stuff
- **Teacher Mode**: Shows what's happening under the hood
- **Clear Results**: Big emoji + explanation so it's obvious what the app thinks
- **Example Sentences**: Some pre-made examples if you're not sure what to try

---

## What Students Actually Learn

I designed this with learning in mind, so here's what students pick up:

### Main Ideas

1. **AI/ML Basics**
   - What sentiment analysis actually means
   - How computers process and understand text
   - Why certain words are seen as positive or negative

2. **Text Classification**
   - How text gets sorted into categories
   - Understanding the polarity score thing (-1 to +1)
   - How thresholds help make decisions

3. **Real Python Code**
   - Working with actual libraries people use in industry
   - How functions and if/else statements work together
   - Building something that looks like a real web app

4. **Safety Stuff**
   - Why we need content filters
   - Making tech that's age-appropriate
   - Thinking about AI responsibility

5. **Real Life Uses**
   - How social media checks post vibes
   - Customer review analysis
   - Making chatbots understand emotions better

---

## Teaching Guide (About 1 Hour)

I wrote this up thinking about how a teacher might actually use this in class.

**Who It's For**: 12-16 year olds  
**How Long**: Around an hour  
**What They Should Know**: Basic Python (like what variables and if statements are)

### How I'd Break It Down

#### First 10 Minutes: Show Them What It Does
- Just open the app and try different sentences
- Ask them "How do you think it knows if something is happy or sad?"
- Main points to cover:
  - Computers find patterns in words
  - Words have different emotional weights
  - We're going to build our own version of this

#### Next 10 Minutes: Open the Hood (Teacher Mode)
- Turn on Teacher Mode and walk through what's shown
- Talk about:
  - The whole input → processing → output flow
  - Why the safety filter matters
  - What those polarity numbers mean
  - Quick intro to TextBlob
- Get them to guess scores before revealing them

#### Minutes 20-35: Look at the Actual Code
- Open up `app.py` and go through it together
- Key parts to explain:
  1. **Safety Filter** (around line 16-22): How it catches bad words
  2. **Mood Analysis** (around line 24-53): Where TextBlob does its thing
  3. **The Decision Part** (around line 42-51): How if/elif/else picks the emoji
  4. **The Interface** (around line 101-167): How Streamlit makes the UI

- **Hands-on bit**: Have them change 0.1 to 0.2 in the code and see what happens

#### Minutes 35-50: Let Them Experiment
- Students test weird cases and think of improvements
- Things to try:
  - Sentences with mixed feelings
  - ALL CAPS vs normal text
  - Adding lots of punctuation (!!!)
  - Stuff that's borderline neutral

- **Ideas for extensions**:
  - More emojis (like 😱 for super negative, 😍 for super positive)
  - Better bad word filter
  - Show a confidence percentage
  - Different modes for formal vs casual text

#### Last 10 Minutes: Talk About the Big Picture
- Discussion questions I'd ask:
  - Where have you seen this kind of thing before?
  - What could go wrong with AI detecting moods?
  - Do emojis mean the same thing everywhere?
  - Should AI always be reading our emotions?

- **Homework idea**:
  - Write 5 sentences and guess their scores
  - Find one real example of sentiment analysis being used
  - Think of a new feature you'd add

### Tips from My Experience
- **Different skill levels**: Advanced kids can modify code, others can just understand the concepts
- **Visual stuff helps**: Draw the flow on a whiteboard
- **Work in pairs**: They can test each other's sentences
- **Define terms clearly**: Not everyone knows "sentiment" or "polarity"

---

## Stuff That Doesn't Work Great

Being honest about the limitations:

### Technical Issues
1. **Pretty Basic Analysis**
   - TextBlob isn't super advanced
   - Completely misses sarcasm
   - Context is hard for it

2. **Simple Safety Filter**
   - My bad words list isn't exhaustive
   - Won't catch creative spelling or new slang
   - Not foolproof

3. **English Only**
   - TextBlob mainly works with English
   - Other languages give weird results

4. **Arbitrary Cutoffs**
   - The ±0.1 threshold I picked is kind of random
   - Some neutral stuff gets misread

### Teaching Notes
- This is for **learning**, not like a real product
- Good to show students that AI isn't perfect
- Use these limitations to talk about AI ethics and problems

### How I'd Improve It
- Support other languages
- Better filtering system
- Let users adjust sensitivity
- Show subjectivity scores too
- Add more emotions (angry, surprised, scared)

---

## Technical Stuff

### Libraries Used
- **Streamlit 1.29.0**: Makes the web interface
- **TextBlob 0.17.1**: Does the sentiment analysis

### How TextBlob Actually Works
- Uses a pre-trained model with word associations
- Looks up words in its lexicon to score them
- Gives back:
  - `polarity`: -1 (super negative) to +1 (super positive)
  - `subjectivity`: 0 (factual) to 1 (opinion-based)

### Project Structure
```
mood2emoji/
├── app.py              # Main app file
├── requirements.txt    # What to install
├── README.md          # You're reading it
└── lesson_plan.pdf    # Detailed teaching plan
```

### Want to Customize It?

**Change when emojis show up:**
```python
# In app.py around line 43-51
if polarity > 0.2:  # Changed from 0.1 - needs stronger positive vibes now
    emoji = "😀"
```

**Add more emojis:**
```python
if polarity > 0.5:
    emoji = "😍"
    explanation = "Super excited and happy!"
elif polarity > 0.1:
    emoji = "😀"
    explanation = "Pretty happy and positive!"
```

---

## Where I Got Help

### References I Used
- **TextBlob Docs**: https://textblob.readthedocs.io/
- **Streamlit Docs**: https://docs.streamlit.io/
- **Sentiment Analysis Info**: Pattern library docs (what TextBlob uses)

### About the Code
Everything here is stuff I wrote specifically for this project. I'm using open-source libraries (TextBlob and Streamlit) that are free to use.

### No Paid Services
This runs completely on your computer - no API keys or paid services needed.

---

## Try These Sentences!

Here's some good ones to start with:
- "I absolutely love learning new things!" → 😀
- "The weather is cloudy today." → 😐
- "I'm feeling really down and sad." → 😞
- "This homework is awesome and fun!" → 😀
- "I don't know what to think about this." → 😐

---

## Questions?

Feel free to reach out if something doesn't make sense. You can also check the lesson plan PDF for more detailed teaching instructions.

**Hope you find this useful! 🚀**

---

*Created by [@haarisseraj2000](https://github.com/haarisseraj2000)*
