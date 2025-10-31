# 🚀 Deployment Guide

## Step-by-Step Deployment Instructions

### Prerequisites
- GitHub account (free at github.com)
- Git installed on your system ✅ (Already done!)
- Streamlit Cloud account (free at share.streamlit.io)

---

## Step 1: Create GitHub Repository ✅ COMPLETED

Your local Git repository is initialized and committed!

```
✅ Git initialized
✅ Files committed (7 files, 1237 lines)
✅ Commit ID: fbc2651
```

---

## Step 2: Push to GitHub

### Option A: Using GitHub Desktop (Easiest)
1. Download GitHub Desktop: https://desktop.github.com/
2. Open GitHub Desktop
3. Click "Add" → "Add Existing Repository"
4. Select folder: `C:\Users\HP\firstname-lastname-mood2emoji`
5. Click "Publish repository" button
6. Name it: `firstname-lastname-mood2emoji`
7. Uncheck "Keep this code private" (or keep it private, up to you)
8. Click "Publish Repository"

### Option B: Using Command Line (Manual)

1. **Create a new repository on GitHub.com:**
   - Go to: https://github.com/new
   - Repository name: `firstname-lastname-mood2emoji`
   - Description: "Kid-safe text sentiment analyzer for ages 12-16"
   - Public or Private: Your choice
   - Do NOT initialize with README (we already have one)
   - Click "Create repository"

2. **Connect and push:**
   ```powershell
   # Replace YOUR_USERNAME with your actual GitHub username
   git remote add origin https://github.com/YOUR_USERNAME/firstname-lastname-mood2emoji.git
   git branch -M main
   git push -u origin main
   ```

3. **Enter credentials when prompted:**
   - Username: Your GitHub username
   - Password: Use a Personal Access Token (not your password)
   
   **Get a token:**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select "repo" scope
   - Copy the token and use it as password

---

## Step 3: Deploy to Streamlit Cloud

### Setup Process:

1. **Go to Streamlit Cloud:**
   - Visit: https://share.streamlit.io/
   - Click "Sign up" or "Sign in with GitHub"

2. **Create New App:**
   - Click "New app" button
   - Select your repository: `firstname-lastname-mood2emoji`
   - Branch: `main` (or `master`)
   - Main file path: `app.py`
   - Click "Deploy!"

3. **Wait for deployment (2-3 minutes):**
   - Streamlit will install dependencies
   - App will automatically start
   - You'll get a public URL like: `https://your-app-name.streamlit.app`

4. **Important: TextBlob Data Issue:**
   
   If the app fails to load, you need to add a `packages.txt` file.
   
   **Create this file:**
   ```powershell
   # Run this in your project directory
   echo "python3-pip" > packages.txt
   git add packages.txt
   git commit -m "Add packages.txt for deployment"
   git push
   ```

   **Or create a setup script:**
   Create `.streamlit/config.toml`:
   ```toml
   [server]
   headless = true
   port = 8501
   ```

---

## Step 4: Verify Deployment

### Test your deployed app:
1. Open the Streamlit Cloud URL
2. Test with these sentences:
   - "I love learning Python!" → Should show 😀
   - "The sky is blue." → Should show 😐
   - "I'm feeling sad." → Should show 😞
3. Toggle "Teacher Mode" in sidebar
4. Verify bad word filter works

### If issues occur:
- Check logs in Streamlit Cloud dashboard
- Verify `requirements.txt` is correct
- Ensure TextBlob corpora downloads in app startup

---

## Alternative: Add TextBlob Download to App

If deployment fails, modify `app.py` to download data on startup:

```python
# Add at the top of app.py, after imports:
import nltk
nltk.download('punkt', quiet=True)
nltk.download('brown', quiet=True)
nltk.download('wordnet', quiet=True)
```

---

## Your Submission Links

Once deployed, you'll have:

### 1. GitHub Repository Link:
```
https://github.com/YOUR_USERNAME/firstname-lastname-mood2emoji
```

### 2. Streamlit App Link:
```
https://YOUR_APP_NAME.streamlit.app
```

### 3. Lesson Plan Link:
See LESSON_PLAN_SHARE.md for sharing options

---

## Troubleshooting

### Issue: "Module not found"
**Solution:** Check `requirements.txt` has all dependencies

### Issue: "TextBlob sentiment error"
**Solution:** Add NLTK downloads to `app.py` startup

### Issue: "Port already in use"
**Solution:** This won't happen on Streamlit Cloud (only local)

### Issue: "Authentication failed" (Git push)
**Solution:** Use Personal Access Token instead of password

---

## Final Checklist

- [ ] Git repository initialized ✅
- [ ] Files committed ✅
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Streamlit Cloud account created
- [ ] App deployed
- [ ] App tested and working
- [ ] URLs copied for submission

---

**Need Help?**
- GitHub Docs: https://docs.github.com/
- Streamlit Docs: https://docs.streamlit.io/streamlit-community-cloud
- Git Tutorial: https://git-scm.com/docs/gittutorial
