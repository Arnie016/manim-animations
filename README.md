# 🎬 Manim Animations

Visualizing complex math through beautiful animations.

## 🎬 Animations

### 01. Poles and Zeroes
Educational split-screen visualization of transfer functions with progressive pole/zero addition.

📹 [Video](videos/01_Poles_and_Zeroes.mp4) | 📝 [Code](code/01_poles_and_zeros.py) | 📄 [Docs](docs/01_Poles_and_Zeroes.md)

### 02. Repository Intro
12-second intro video showcasing repository structure, author info, and educational philosophy.

📹 [YouTube](https://www.youtube.com/watch?v=7rnUQ21SjiE) | 📝 [Code](code/02_repo_intro.py) | 📄 [Docs](docs/02_Repo_Intro.md) | 🎵 [Sound](sounds/02_Repo_Intro.mp3)

## Quick Start

```bash
git clone https://github.com/Arnie016/manim-animations.git
cd manim-animations
pip install -r requirements.txt
python3 -m manim code/01_poles_and_zeros.py PolarPolesZerosEducational -pqh
```

## Libraries

- Manim 0.18.1
- NumPy

## Structure

- `code/` - Animation scripts
- `videos/` - Rendered MP4s
- `sounds/` - Audio files (MP3, WAV) for each animation
- `docs/` - Documentation

## Structure

Each animation is organized as a bundle:
- **Video:** `videos/XX_Name.mp4`
- **Code:** `code/XX_name.py`
- **Sound:** `sounds/XX_Name.mp3` (if applicable)
- **Docs:** `docs/XX_Name.md` (prompts, insights, development history)

See individual doc files for detailed development history, prompts used, and insights.
