# Quick GitHub Upload

## One-Time Setup
```bash
cd /Users/hema/Desktop/manim

# 1. Create repo on GitHub.com (don't initialize with README)

# 2. Connect and push
git add .
git commit -m "Initial commit: Educational Manim animations"
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## What Gets Uploaded
✅ Code files (`code/*.py`)
✅ Videos (`videos/*.mp4`) - GitHub can preview these!
✅ Documentation (`docs/*.md`, `README.md`)
✅ Dependencies (`requirements.txt`)
✅ License (`LICENSE`)

## What Gets Ignored (via .gitignore)
❌ Python cache files
❌ Virtual environments
❌ Temporary Manim files
❌ IDE files

## Video Size: 5.7MB ✅ (well under GitHub's 100MB limit)

## After Upload
- People can view videos directly on GitHub
- Code is readable with syntax highlighting
- README shows libraries and prompt style
- Easy to clone and run locally
