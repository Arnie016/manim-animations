# Upload to GitHub - Step by Step

## Your GitHub: https://github.com/Arnie016

## Option 1: Create New Repo (Recommended)

### Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Repository name: `manim-animations` (or any name you prefer)
3. Description: "Educational Manim animations - control systems visualizations"
4. **Public** (so videos are viewable)
5. **Don't** check "Initialize with README" (we already have one)
6. Click "Create repository"

### Step 2: Upload Your Code
```bash
cd /Users/hema/Desktop/manim

# Add all files
git add .

# Commit
git commit -m "Initial commit: Educational Manim animations

- Polar poles & zeros visualization
- Split-screen s-plane and Nyquist plot
- Progressive pole/zero addition demonstration"

# Connect to your GitHub repo
git remote add origin https://github.com/Arnie016/manim-animations.git

# Push
git branch -M main
git push -u origin main
```

## Option 2: Add to Existing Repo

If you want to add to an existing repo:

```bash
cd /Users/hema/Desktop/manim

# Add existing repo as remote
git remote add origin https://github.com/Arnie016/EXISTING_REPO_NAME.git

# Pull first (if repo has content)
git pull origin main --allow-unrelated-histories

# Then push
git add .
git commit -m "Add Manim animations"
git push -u origin main
```

## Repository Structure

Your repo will be organized like:
```
manim-animations/
├── README.md                    # Main docs (shows on GitHub homepage)
├── requirements.txt             # Dependencies
├── LICENSE                      # MIT License
├── code/
│   └── polar_poles_zeros_educational.py
├── videos/
│   └── PolarPolesZerosEducational.mp4
└── docs/
    ├── README.md
    ├── GITHUB_SETUP.md
    └── GITHUB_UPLOAD.md
```

## Adding More Animations Later

When you create new animations:

```bash
# 1. Create new file: code/new_animation.py

# 2. Render it
python3 -m manim code/new_animation.py NewScene -pqh

# 3. Copy video
cp media_temp/.../NewScene.mp4 videos/

# 4. Update README.md to add new animation section

# 5. Commit and push
git add code/new_animation.py videos/NewScene.mp4 README.md
git commit -m "Add new animation: description"
git push
```

## Viewing on GitHub

After upload:
- **Code**: Viewable with syntax highlighting
- **Videos**: Click MP4 files to play inline
- **README**: Shows on repo homepage
- **Structure**: Easy to browse `code/` and `videos/`

## Quick Commands Reference

```bash
# Check status
git status

# See what will be uploaded
git add -n .

# Commit changes
git commit -m "Your message"

# Push updates
git push

# View remote
git remote -v
```

