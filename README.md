# 🎬 Manim Animations

Visualizing complex math through beautiful animations.

## 🎬 Intro Video

[![Repo Intro Video](https://img.youtube.com/vi/7rnUQ21SjiE/maxresdefault.jpg)](https://www.youtube.com/watch?v=7rnUQ21SjiE)

**Watch on YouTube:** [https://www.youtube.com/watch?v=7rnUQ21SjiE](https://www.youtube.com/watch?v=7rnUQ21SjiE)

Or download: [videos/repo_intro.mp4](videos/repo_intro.mp4)

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
