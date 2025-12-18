# Could Spider-Man Actually Swing Between Buildings?

## Video
- **File:** `videos/06_Spiderman_Physics.mp4`
- **Code:** `code/06_Spiderman_Physics.py`
- **Sound:** N/A

## Description
TikTok animation (9:16) answering "Could Spider-Man actually swing between buildings?" Features Spider-Man in iconic red suit as the visual centerpiece, with physics calculations shown in side panels. Big emphasized numbers for key results (speed: 100 MPH, tension: 3,000N, G-forces: 2-4G). Includes progress bar showing current section (Setup → Physics → G-Force → Damage → Verdict). Verdict: Normal humans can't do it, but Spider-Man's superpowers make it work!

## Development History

### Initial Prompts
1. "Make plan of video for 'Could Spider-Man Actually Swing Between Buildings?'"
2. "ok make this emphasize visuals red suit of spiderman and do calculation to side but final number should be emphasized and make sure video progresses in title sequence and the current title sequence is visible"
3. "Calculations should only be relevant and visible at the bottom right now. They are too small, only focusing on specific aspects to make it interesting. I don't want the whole calculation, and I don't like the pendulum idea. Improve it, and I should actually see the animation of the web flying. So, just one line please."
4. "Now I want you to make it super clear the calculation for G-forces only. Like I want to know the reason behind the G-forces, why they occur, why they would occur from a physics standpoint, and do the calculation clearly visible."

### What Worked
- **Web shooting animation** - "THWIP!" text with web flying across screen in single line (rush_into rate function)
- **Bottom-right calculation boxes** - Larger (4×1.2), focused one-liners, positioned at DR corner
- **NO pendulum references** - Removed technical jargon, just "The Swing!"
- **Detailed G-force explanation** - 3-part breakdown:
  1. WHY: Direction changes rapidly at bottom of swing
  2. DIAGRAM: Circular motion with velocity (green) and acceleration (red) vectors
  3. STEP-BY-STEP CALCULATION: Formula → Values → Result → G-conversion (all visible, large text)
- **Step-by-step math** - Formula (a = v²/r) → v=44 m/s, r=100m → 44²/100 = 19.4 m/s² → 19.4/9.8 = 2 G's
- **Physics reasoning clear** - Explains centripetal force requirement, not just showing numbers
- **Progress bar** - Shows 5 sections with current highlighted
- **BIG number reveals** - Key results in large boxes: Speed (100 MPH), Tension (675 lbs), G-Force (2-4G's)
- **Split-screen verdict** - Normal human (❌ RED) vs Spider-Man (✅ GREEN)
- **Flash effects** - Used for dramatic reveals

### What Didn't Work / Challenges
- Balancing technical accuracy with entertainment value
- Making calculations visible but not overwhelming
- Spider-Man character design - keeping it recognizable but simple enough for Manim

### Key Insights
- **Visual hierarchy matters** - Main character/concept should dominate, math supports it
- **Progress indicators work** - Viewers know where they are in the story
- **Big reveals need emphasis** - Use size, color, animation (Flash, scale) for impact
- **Split comparisons are powerful** - Side-by-side "human vs superhero" makes point instantly
- **Comic book aesthetics** - Bold colors, thick outlines, POW! style fits superhero theme

### Technical Notes
- Scene configured for 9:16 TikTok (1080×1920), content in top 3/4
- Spider-Man colors: `SPIDERMAN_RED = "#DC143C"`, `SPIDERMAN_BLUE = "#0047AB"`
- `ProgressBar` class: Shows 5 sections with current highlighted (larger dot + label)
- `SpiderMan` class: Custom character with red body, blue legs, white eyes, web pattern
- `Building` class: NYC skyscraper with yellow window grid
- **`CalculationBox` class (NEW):** Bottom-right boxes (4×1.2), 32pt font, positioned at DR corner with `.to_edge(DR, buff=0.4)`
  - Replaced side panels with focused one-liners
  - Examples: "Building: 300m tall", "Web holds 75 kg person", "Centripetal force at bottom"
- **Web shooting animation:** Line extends from Spider-Man to building with `rush_into` rate function, "THWIP!" text appears
- **G-Force detailed section:**
  - Circular motion diagram: `Arc` with velocity arrow (GREEN) and centripetal acceleration arrow (RED)
  - Step-by-step calculation displayed large on screen (font_size 48-56)
  - Formula: `a_c = v²/r`
  - Calculation: `44²/100 = 19.4 m/s²`
  - Conversion: `19.4/9.8 = 2 G's`
- **Big number boxes:**
  - Speed: 6×1.5 red box, 48pt font
  - Tension: 6×1.5 orange box, 48pt font
  - G-Force: 7×2 dark red box, 72pt font (LARGEST with Flash effect!)
- Animation techniques:
  - `MoveAlongPath` for swing motion with `angle=-PI/2.5`
  - `Flash` effect for G-force reveal
  - `LaggedStart` for sequential list items
  - `rush_into` rate function for web shooting
- Final verdict: Split screen with colored boxes (RED for impossible, GREEN for possible)

### Physics Calculations
1. **Swing Speed:** v = √(2gL) = √(2 × 9.8 × 100) ≈ 44 m/s (100 MPH)
2. **Web Tension:** T = mg(3 - 2cosθ) ≈ 3,000 N (675 pounds)
3. **G-Force:** a = v²/r = 44²/100 = 19 m/s² ≈ 2G (up to 4G with direction changes)
4. **Human Arm Strength:** ~400N vs Required: 3,000N (7.5× too weak!)

### Narrative Structure
1. **Setup (0-10s)** - Spider-Man swinging between NYC buildings, "Can a REAL human do this?"
2. **Physics (10-25s)** - It's a pendulum! Show swing, calculate speed (100 MPH) and tension (675 lbs)
3. **G-Force (25-35s)** - The REAL problem: 2-4 G's (fighter pilot level)
4. **Damage (35-45s)** - What happens: dislocated shoulders, whiplash, internal injuries
5. **Verdict (45-55s)** - Normal human: ❌ IMPOSSIBLE, Spider-Man: ✅ WORKS (with superpowers)
6. **Outro (55-60s)** - "You Need SUPERPOWERS!" + follow CTA

### Visual Hierarchy
**Primary (Center, Large):**
- Spider-Man character in red suit
- Big number reveal boxes
- Verdict split screen

**Secondary (Side, Smaller):**
- Calculation panels with equations
- Buildings (background)
- Web line

**Tertiary (Top):**
- Title
- Progress bar
- Section labels

### Prompt Style Used
- User requested emphasis on visuals over math
- Calculations shown but de-emphasized (side panels)
- Final numbers dramatically emphasized (large boxes)
- Progress tracking visible throughout
- Comic book / superhero aesthetic

