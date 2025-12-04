# 🎬 Manim Animations

Visualizing complex math through beautiful animations.

## 🎬 Intro Video

<video width="100%" controls>
  <source src="https://github.com/Arnie016/manim-animations/raw/main/videos/repo_intro.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Or watch directly: [videos/repo_intro.mp4](videos/repo_intro.mp4)

## Current Animation

**Polar Poles & Zeros** - Split-screen visualization of transfer functions with progressive pole/zero addition.

📹 [Full Video](videos/PolarPolesZerosEducational.mp4) | 📝 [Code](code/polar_poles_zeros_educational.py)

## Quick Start

```bash
git clone https://github.com/Arnie016/manim-animations.git
cd manim-animations
pip install -r requirements.txt
python3 -m manim code/polar_poles_zeros_educational.py PolarPolesZerosEducational -pqh
```

## Libraries

- Manim 0.18.1
- NumPy

## Structure

- `code/` - Animation scripts
- `videos/` - Rendered MP4s
- `sounds/` - Audio files (MP3, WAV) for each animation
- `docs/` - Documentation

## Audio

Each animation may have accompanying audio. See [Audio Documentation](docs/AUDIO.md) for details.

**Current audio:**
- `repo_intro.mp3` - Background music for intro video (ElevenLabs)
