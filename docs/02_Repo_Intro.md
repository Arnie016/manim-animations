# Repository Intro Animation

## Video
- **File:** `videos/02_Repo_Intro.mp4`
- **Code:** `code/02_repo_intro.py`
- **Sound:** `sounds/02_Repo_Intro.mp3` (ElevenLabs)
- **YouTube:** https://www.youtube.com/watch?v=7rnUQ21SjiE

## Description
12-second intro video for the repository. Shows repository structure, author info, goal, and educational quote with background animations.

## Development History

### Initial Prompts
- "Make it 12 seconds, cut in half the time too long"
- "Add more subtle animations"
- "The quote should be at the center with spark to be ignited"
- "Animation happens in left and right side like different experiments"
- "Start zooming after credentials"
- "Add relativistic and black hole spacetime equations"
- "Remove sine wave animation, it looks odd"

### What Worked
- Sequential text display (one snippet at a time)
- Background animations: planets, pendulum, equations, pole-zero plots
- Slow zoom effect throughout
- Subtle animations (reduced opacity, smaller sizes)
- Audio integration with ElevenLabs music

### What Didn't Work / Challenges
- Initial video was too long (1:30) - trimmed to match animation
- Sine wave phase animation looked odd - removed
- Spark animation effect was too much - simplified to text emphasis
- GitHub markdown doesn't support embedded video - used YouTube instead
- Audio required ffmpeg/ffprobe installation

### Key Insights
- Sequential text keeps focus clear
- Background animations add visual interest without distraction
- Subtle is better - less opacity, smaller elements
- Quote needs enough time to read (extended to 2s wait)
- YouTube embedding works better than GitHub file links

### Technical Notes
- Duration: ~23 seconds (with extended quote timing)
- Audio: AAC, 44100 Hz, stereo, 195 kb/s
- Background animations: planets, pendulum, equations, graphs
- Zoom effect: Scales container groups smoothly
- Audio integration: `self.add_sound()` with duration limit

### Prompt Style Used
- Iterative refinement based on feedback
- Focus on clarity and readability
- Balance between visual interest and information
- Educational quote as centerpiece

