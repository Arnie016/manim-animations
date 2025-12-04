# Poles and Zeroes Animation

## Video
- **File:** `videos/01_Poles_and_Zeroes.mp4`
- **Code:** `code/01_poles_and_zeros.py`

## Description
Split-screen visualization of transfer functions with progressive pole/zero addition. Shows s-plane (pole-zero map) and polar plot (Nyquist) side-by-side.

## Development History

### Initial Prompts
- "Make an animation 9:16 for a polar plot visualization of a transfer function"
- "Add poles and zeros progressively to show how the polar plot behaves"
- "Make it educational with split-screen view (s-plane and polar plot)"
- "Center pole/zero plots, render equations one at a time"

### What Worked
- Split-screen layout for comparison
- Progressive disclosure (adding poles/zeros one at a time)
- Color coding: Poles (red X), Zeros (green O)
- LaTeX math rendering for transfer functions
- Glow dot cursor with trail effect

### What Didn't Work / Challenges
- Initial 9:16 aspect ratio was too zoomed in
- Changed to 16:9 (1920x1080) for better fit
- Had to escape special characters in LaTeX (`&`, `°`, `→`)
- GlowDot class doesn't exist - created custom `create_glow_dot()` function

### Key Insights
- Visual clarity: Split-screen layouts work well for educational content
- Progressive disclosure: Building complexity gradually helps understanding
- Color coding helps distinguish poles from zeros
- Real-time visualization makes concepts more intuitive

### Technical Notes
- Uses Manim's `ParametricFunction` for polar curves
- Frequency array: `np.logspace(-2.5, 1.5, 800)`
- Transfer function evaluation: `H(s) = K * Π(s-z) / Π(s-p)`
- Phase unwrapping: `np.unwrap(np.angle(H))`

