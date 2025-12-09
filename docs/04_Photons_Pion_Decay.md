# Photons & Pion Decay

## Video
- **File:** `videos/04_Photons_Pion_Decay.mp4`
- **Code:** `code/04_Photons_Pion_Decay.py`
- **Sound:** N/A

## Description
TikTok animation (9:16) explaining Einstein's discovery of photons (1905), with detailed step-by-step derivation of neutral pion decay π⁰ → γ + γ using energy-momentum conservation. Shows Lorentz invariant approach to solving for photon energies, frame transformations, and relativistic beaming. Demonstrates how cosmic rays create pions that decay into gamma radiation. Content positioned in top 3/4 of screen (bottom 1/4 reserved for TikTok descriptions).

## Development History

### Initial Prompt
"Make a video on this. Photons. Around the same time the scientific community was digesting Einstein's new and radical theory of relativity, Einstein was making inroads on other problems in physics. In 1905, Einstein published a paper on an interaction between light and electrons on the surfaces of materials. By carefully observing the electrons, he discovered that the radiant energy carried by light is absorbed in particle-like 'packets' called photons."

### User Feedback (Iteration 2)
"Make the animations better by making the text bigger and explanations better. Also, try to derive some stuff and sometimes it gets jumbled up. I don't want to be jumbled up. Equally spaced out more things should be at the top of the three-quarters because I think there will be descriptions and stuff in the TikTok video. But generally a good job. Try to improve it. Please provide a bit of contact. I like the pacing, but it should just be more derivations of how pions decay into photons and in different frames of reference. This photon decay what it means."

### What Worked
- **Step-by-step derivation** - Clear mathematical steps showing energy-momentum conservation: p_π = p_γ,R + p_γ,L
- **Lorentz invariant approach** - Shows (p_π - p_γ,R)² = 0, then expands in rest frame to derive ω_R = E_π₀/(2ℏ)
- **Larger text sizes** - All font sizes increased (titles 52pt, formulas 44-56pt, body text 28-36pt) for better readability
- **Better spacing** - Content confined to top 3/4 of screen (TOP_REGION_TOP = 6.0, TOP_REGION_BOTTOM = -4.0) with generous buff spacing between elements
- **Frame transformations** - Clear side-by-side comparison of rest frame (uniform photon distribution) vs Earth frame (relativistic beaming)
- **Organized layout** - Less jumbled with clear sections: Introduction → Derivation → Visualization → Beaming → Cosmic rays
- **Photon four-momentum** - Shows p_γ = (ℏω/c)(1, cos α, sin α, 0) explicitly
- **Derivation steps labeled** - "Step 1: Use Lorentz invariant", "Step 2: Expand in pion rest frame" for clarity

### What Didn't Work / Challenges
- Initial version had smaller text and jumbled layout
- Missing derivation steps - user wanted to see HOW we get E_γ = E_π₀/2, not just state it
- Frame transformations needed clearer explanation of what happens to photon directions
- Balancing mathematical rigor with TikTok pacing requires careful timing

### Key Insights
- **Derivations are crucial** - Users want to see the mathematical steps, not just the result
- **Bigger text = better** - TikTok viewers need larger fonts to read quickly on mobile
- **Top 3/4 layout** - Leaving bottom 1/4 empty gives space for TikTok captions/descriptions
- **Step labels help** - Numbering derivation steps ("Step 1", "Step 2") guides viewer through complex math
- **Frame-by-frame comparison** - Showing rest frame vs Earth frame side-by-side makes relativistic effects intuitive
- **Mathematical progression** - Starting with conservation law → invariant → expansion → solution builds understanding naturally

### Technical Notes
- Scene configured for 9:16 TikTok aspect ratio (1080×1920)
- Content region defined by `TOP_REGION_TOP = 6.0` and `TOP_REGION_BOTTOM = -4.0` constants
- Font sizes: Titles 48-52pt, Math formulas 38-56pt, Body text 28-36pt, Labels 28-32pt
- `PhotonParticle` class creates wavy line with arrow representing photon
- `PionParticle` class shows neutral pion with π⁰ label and mass (135 MeV)
- Derivation sequence:
  1. Conservation: p_π = p_γ,R + p_γ,L
  2. Invariant: (p_π - p_γ,R)² = 0 (zero in all frames)
  3. Rest frame: p_π = (E_π₀, 0, 0, 0), p_γ,R = (ℏω_R/c)(1, cos α_R, sin α_R, 0)
  4. Expand: E_π₀² - 2E_π₀(ℏω_R/c) = 0
  5. Solve: ω_R = E_π₀/(2ℏ) → E_γ = E_π₀/2 = 67.5 MeV
- Relativistic beaming shown with side-by-side ray distributions and formula α_max = cos⁻¹(v/c)
- Cosmic ray chain: Cosmic ray (>1 GeV) → Atmosphere (30 km) → Pion creation → Decay → Gamma rays → Earth

### Prompt Style Used
- Direct physics content with mathematical derivations
- User requested improvements: bigger text, more derivations, better spacing, less jumbled
- Iterative refinement based on specific feedback about layout and mathematical content
