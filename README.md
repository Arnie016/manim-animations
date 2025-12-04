# 🎬 Manim Animations

> **Visualizing complex math through beautiful animations**

Educational animations that bring control systems theory to life. Watch transfer functions evolve, poles and zeros dance across the s-plane, and frequency responses trace elegant curves—all rendered in stunning detail with Manim.

**Perfect for:** Students learning control systems, engineers visualizing transfer functions, or anyone who wants to see math in motion.

## 📁 Structure

```
manim/
├── code/          # Python animation scripts
├── videos/        # Rendered MP4 files
└── docs/          # Planning and documentation
```

## 🎬 Animations

### 🎯 Polar Poles & Zeros Educational
**File:** `code/polar_poles_zeros_educational.py`  
**Video:** `videos/PolarPolesZerosEducational.mp4`

Watch transfer functions come alive as poles and zeros are added progressively. This split-screen visualization shows:
- **Left:** Real-time s-plane pole-zero placement (X marks poles, O marks zeros)
- **Right:** Live polar plot (Nyquist) tracing frequency response
- **Dynamic:** Equations render one at a time, phase angles update, educational commentary guides you

See how each pole pulls the response inward, each zero pushes it outward, and complex poles create beautiful spirals.

[![Polar Poles & Zeros](videos/PolarPolesZerosEducational.mp4)](videos/PolarPolesZerosEducational.mp4)

---

*More animations coming soon!*

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- LaTeX (for math rendering): `brew install --cask basictex` (macOS) or install MacTeX/TeXLive

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd manim

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Render Animation
```bash
python3 -m manim code/polar_poles_zeros_educational.py PolarPolesZerosEducational -pqh --media_dir ./videos
```

Flags:
- `-p` - Preview after rendering
- `-q` - Quality (h=high, m=medium, l=low)
- `-h` - High quality (1080p60)

## 📚 Libraries Used

- **Manim** (`manim==0.18.1`) - Mathematical animation engine
- **NumPy** - Numerical computations for transfer functions
- **LaTeX** - Math equation rendering

## 💡 How This Was Built

This project was crafted iteratively with AI assistance, focusing on clarity and visual storytelling.

### Development Philosophy
1. **Start Simple** → Begin with basic visualization, then layer complexity
2. **Iterate Fast** → Build, render, refine, repeat
3. **Educate First** → Every animation should teach something
4. **Clean Code** → Organized structure for easy experimentation

### Key Prompts That Shaped This
- *"Make an animation 9:16 for a polar plot visualization of a transfer function"*
- *"Add poles and zeros progressively to show how the polar plot behaves"*
- *"Make it educational with split-screen view (s-plane and polar plot)"*
- *"Center pole/zero plots, render equations one at a time"*

### Design Principles
- **Visual Clarity**: Split-screen layouts for side-by-side comparison
- **Progressive Disclosure**: Build complexity gradually, don't overwhelm
- **Color Coding**: Poles (red X), Zeros (green O), unique colors per stage
- **Rich Annotations**: Phase angles, transfer functions, educational text

## ✨ What Makes These Animations Special

- **🎯 Real-Time Visualization**: Watch poles and zeros appear and transform the response instantly
- **📐 Dual View**: S-plane and Nyquist plot side-by-side for complete understanding
- **✨ Visual Effects**: Glowing cursor trails, smooth transitions, color-coded stages
- **📝 LaTeX Math**: Beautifully rendered transfer function equations
- **🎓 Educational**: Commentary explains *why* each change happens, not just *what*
- **🎬 Cinematic**: 1080p60 renders with smooth animations and professional polish

## 📝 Adding New Animations

1. Create new Python file in `code/`
2. Define a Scene class inheriting from `manim.Scene`
3. Render: `python3 -m manim code/your_file.py YourScene -pqh`
4. Copy final MP4 to `videos/` directory

## 🤝 Contributing

Feel free to experiment! This is a learning project. Suggestions:
- Add more transfer function examples
- Create animations for other control systems concepts
- Improve visualizations or add new features

## 📄 License

MIT License - feel free to use and modify

## 🙏 Acknowledgments

- Manim Community Edition for the animation framework
- Control systems theory for the mathematical concepts

