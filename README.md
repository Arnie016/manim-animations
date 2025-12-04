# Manim Animation Project

Educational animations created with Manim, focusing on control systems and transfer function visualizations.

## 📁 Structure

```
manim/
├── code/          # Python animation scripts
├── videos/        # Rendered MP4 files
└── docs/          # Planning and documentation
```

## 🎬 Current Animation

**Polar Poles & Zeros Educational** (`code/polar_poles_zeros_educational.py`)
- Split-screen visualization showing s-plane (pole-zero map) and polar plot (Nyquist)
- Progressive animation adding poles and zeros to demonstrate their effects
- Educational commentary explaining phase angles and stability

### Watch the Animation
[![Polar Poles & Zeros](videos/PolarPolesZerosEducational.mp4)](videos/PolarPolesZerosEducational.mp4)

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

## 💡 Prompt Style & Approach

This project was developed iteratively using AI assistance with the following approach:

### Development Process
1. **Start Simple**: Begin with basic visualization (polar plot)
2. **Iterate**: Add features progressively (poles, zeros, s-plane)
3. **Educational Focus**: Each animation explains concepts clearly
4. **Clean Structure**: Separate code, videos, and docs

### Key Prompts Used
- "Make an animation 9:16 for a polar plot visualization of a transfer function"
- "Add poles and zeros progressively to show how the polar plot behaves"
- "Make it educational with split-screen view (s-plane and polar plot)"
- "Center pole/zero plots, render equations one at a time"

### Design Principles
- **Visual Clarity**: Split-screen layout for comparison
- **Progressive Disclosure**: Build complexity gradually
- **Color Coding**: Poles (red X), Zeros (green O), different colors per stage
- **Annotations**: Phase angles, transfer functions, educational text

## 🎨 Animation Features

- **S-Plane Visualization**: Real-time pole-zero placement
- **Polar Plot (Nyquist)**: Frequency response visualization
- **Glow Effects**: Animated cursor with trail
- **LaTeX Math**: Transfer function equations rendered beautifully
- **Educational Commentary**: Explains each stage's effects

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

