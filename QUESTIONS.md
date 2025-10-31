# ❓ Questions & Clarifications

This document contains optional clarification questions about the Mood2Emoji project requirements.

---

## Project Clarifications (Max 3 Questions)

### Question 1: Deployment Requirements
**Question**: For the Streamlit link submission, should the app be deployed to Streamlit Cloud (streamlit.io/cloud), or is a localhost link acceptable? If cloud deployment is required, should we include deployment instructions in the README?

**Reason**: Streamlit Cloud deployment requires additional setup (GitHub integration, account creation) that may affect the timeline.

---

### Question 2: Lesson Plan Format
**Question**: The requirements specify "lesson_plan.pdf" as a deliverable. Should this be a formal PDF document, or is a Markdown file (lesson_plan.md) that can be converted to PDF acceptable? 

**Reason**: We've created a comprehensive Markdown lesson plan that can be easily converted to PDF using tools like Pandoc or exported from VS Code, but want to confirm the preferred format.

---

### Question 3: Bad Word Filter Scope
**Question**: What level of content filtering is expected for ages 12–16? Should the filter focus on:
- Basic inappropriate language (profanity, hate speech)
- All negative words (including mild terms like "dislike", "annoying")
- A comprehensive list covering multiple categories

**Reason**: This affects the safety implementation approach and helps ensure age-appropriate responses without over-filtering educational content.

---

## Additional Notes

If any of these questions require immediate clarification, please respond via the preferred communication channel. Otherwise, we've implemented reasonable defaults:

- **Deployment**: Included instructions for both local and Streamlit Cloud deployment
- **Lesson Plan**: Created comprehensive Markdown (easily convertible to PDF)
- **Filter**: Implemented basic filter with expandable word list (currently ~10 words)

---

**Document Purpose**: Optional clarification questions (not part of core submission)  
**Status**: Template for student use
