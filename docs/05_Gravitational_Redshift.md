# Gravitational Redshift

## Video
- **File:** `videos/05_Gravitational_Redshift.mp4`
- **Code:** `code/05_Gravitational_Redshift.py`
- **Sound:** N/A

## Description
TikTok animation (9:16) showing gravitational redshift near a black hole. Follows an astronaut falling toward a black hole with a torch below them. Shows how light climbing out of the gravity well loses energy, causing its frequency to decrease (redshift). Visual demonstration of spacetime curvature and wave stretching. No mathematics - purely intuitive visual explanation.

## Development History

### Initial Prompt
"Make another video please about gravitation red shift near black hole, should be a good description of what happens as a traveller goes towards black hole and a light beam below him from a torch how it behaves as spacetime become more curved, light beam can be at the bottom and the astronaut on top of it and he sees the frequency change and u can try to use the simple intuitive ways to tell the view how they would view a light beam travelling be precise and make sure intuitively it looks good no math"

### What Worked
- **Visual setup** - Astronaut above, torch below, black hole at bottom creates clear vertical hierarchy
- **Spacetime grid** - Warped grid lines show curvature increasing near black hole
- **Color progression** - Blue → Cyan → Green → Yellow → Orange → Red → Infrared shows redshift clearly
- **Wave stretching analogy** - Side-by-side normal vs stretched sine waves makes frequency change intuitive
- **No math** - Pure visual/intuitive explanation without formulas
- **Step-by-step narrative** - Clear progression: Setup → Light climbing → Move closer → Curvature increases → Color changes → Wave explanation
- **Light becoming invisible** - Showing infrared (invisible) stage adds drama and accuracy

### What Didn't Work / Challenges
- Balancing accuracy with simplicity - gravitational redshift is complex but kept explanation accessible
- Showing spacetime curvature in 2D while maintaining TikTok layout
- Making the "light loses energy" concept intuitive without equations

### Key Insights
- **Gravity well analogy** - "Light must climb out of gravity well" is intuitive
- **Wave stretching** - Visual wave comparison makes frequency change clear
- **Progressive demonstration** - Moving closer to black hole and seeing color change in real-time is powerful
- **Energy = Frequency** - Connecting energy loss to frequency decrease to color change builds understanding
- **Invisibility moment** - Light shifting to infrared (becoming invisible) is a memorable "wow" moment

### Technical Notes
- Scene configured for 9:16 TikTok (1080×1920), content in top 3/4
- `BlackHole` class: Circle with glowing accretion disk layers (orange gradient)
- `Astronaut` class: Simple stick figure with helmet, body, arms, legs
- `Torch` class: Flashlight with triangular beam cone
- `SpacetimeGrid` class: Warped grid showing curvature - points pulled toward black hole with 1/r^1.5 falloff
- Color progression: `[BLUE, BLUE_C, GREEN, YELLOW, ORANGE, RED]` with 0.4s transitions
- Wave demonstration: Normal wave (sin(4x)) vs stretched wave (sin(2x)) shows frequency halving
- Animations: Astronaut + torch move down 2.7 total (1.5 + 1.2), grid curvature increases from 0.5 to 1.2
- Light beam fades to 0.1 opacity for infrared (invisible) stage

### Narrative Structure
1. **Setup** - Astronaut, torch (blue light), black hole
2. **Light climbing** - Arrow showing light traveling up to astronaut
3. **Move closer** - Astronaut + torch descend toward black hole
4. **Spacetime curvature** - Grid appears showing warped spacetime
5. **Color change** - Blue → Red progression with labels
6. **Extreme redshift** - Move even closer, light becomes infrared/invisible
7. **Physics intuition** - 4-point explanation (no math)
8. **Wave demonstration** - Normal vs stretched waves side-by-side
9. **Summary** - Key takeaways

### Prompt Style Used
- User requested: "be precise and make sure intuitively it looks good no math"
- Focus on visual intuition over mathematical rigor
- Step-by-step visual narrative showing cause and effect
- Analogies: "climbing gravity well," "wave stretching"

