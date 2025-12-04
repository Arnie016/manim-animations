# Audio & Sound Design

This document tracks the audio/music used for each animation.

## Structure

- `sounds/` - Audio files (MP3, WAV, etc.) organized by animation name
- Each animation has its corresponding audio file named after the animation

## Current Audio Files

### `repo_intro.mp3`
**Animation:** `repo_intro.py` (Repository intro video)  
**Created with:** ElevenLabs  
**Description:** Background music for the intro/cover video  
**File:** `sounds/repo_intro.mp3`

### Future Animations
When creating new animations with audio:
1. Place audio file in `sounds/` directory
2. Name it after the animation (e.g., `polar_poles_zeros.mp3`)
3. Update this document with:
   - Animation name
   - Creation tool (ElevenLabs, etc.)
   - Description
   - File path

## Adding Audio to Manim Animations

To add audio to a Manim scene:

```python
from manim import *

class YourScene(Scene):
    def construct(self):
        # Add audio
        self.add_sound("sounds/your_audio.mp3")
        
        # Your animation code here
        # ...
```

Or use `add_sound()` with timing:
```python
self.add_sound("sounds/your_audio.mp3", time_offset=0.5)
```

## Audio Creation Tools

- **ElevenLabs** - Text-to-speech and voice synthesis
- Other tools can be added here as used

## Notes

- Keep audio files reasonably sized (< 10MB per file recommended)
- Use MP3 format for compatibility
- Name files consistently: `{animation_name}.mp3`

