# Manim Animation Project

## Structure
- `code/` - All Python animation scripts
- `videos/` - All rendered MP4 files  
- `docs/` - Planning and documentation

## Render Animation
```bash
cd /Users/hema/Desktop/manim
python3 -m manim code/polar_poles_zeros_educational.py PolarPolesZerosEducational -pqh --media_dir ./videos
```

The MP4 will be saved to `videos/polar_poles_zeros_educational/1080p60/PolarPolesZerosEducational.mp4`

To copy it to the root of videos/:
```bash
cp videos/polar_poles_zeros_educational/1080p60/PolarPolesZerosEducational.mp4 videos/
```

