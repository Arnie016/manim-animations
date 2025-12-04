# GitHub Setup Guide

## Initial Upload

### 1. Create GitHub Repository
1. Go to [GitHub](https://github.com/new)
2. Create a new repository (e.g., `manim-animations`)
3. **Don't** initialize with README (we already have one)

### 2. Upload to GitHub

```bash
cd /Users/hema/Desktop/manim

# Add all files
git add .

# Commit
git commit -m "Initial commit: Educational polar plot animation

# Add remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push
git branch -M main
git push -u origin main
```

## Video File Size Considerations

**GitHub File Limits:**
- Files > 50MB: Warning
- Files > 100MB: Blocked (need Git LFS)

**Current video size:** ~5.7MB ✅ (well under limit)

If videos get larger:
```bash
# Install Git LFS
brew install git-lfs  # macOS
git lfs install

# Track MP4 files
git lfs track "*.mp4"
git add .gitattributes
```

## Repository Structure on GitHub

Your repo will show:
```
manim-animations/
├── README.md          # Main documentation (visible on GitHub homepage)
├── LICENSE            # MIT License
├── requirements.txt   # Dependencies
├── .gitignore         # Ignore temp files
├── code/
│   └── polar_poles_zeros_educational.py
├── videos/
│   └── PolarPolesZerosEducational.mp4  # Viewable on GitHub!
└── docs/
    ├── README.md
    └── GITHUB_SETUP.md
```

## Viewing Videos on GitHub

- **MP4 files** are automatically previewable on GitHub
- Click the video file to play it inline
- No external hosting needed for small videos (< 50MB)

## Adding More Animations

When you create new animations:

```bash
# 1. Create new code file
# code/new_animation.py

# 2. Render it
python3 -m manim code/new_animation.py NewScene -pqh

# 3. Copy video to videos/
cp media_temp/.../NewScene.mp4 videos/

# 4. Commit
git add code/new_animation.py videos/NewScene.mp4
git commit -m "Add new animation: description"
git push
```

## Best Practices

1. **Keep videos organized**: One MP4 per animation in `videos/`
2. **Document prompts**: Add notes in code comments
3. **Update README**: Add new animations to main README
4. **Commit frequently**: Small, focused commits

## Example Commit Messages

```bash
git commit -m "Add polar plot animation with s-plane visualization"
git commit -m "Fix glow dot implementation"
git commit -m "Add complex pole-zero example"
```

