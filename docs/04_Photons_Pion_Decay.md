# Photons & Pion Decay

## Video
- **File:** `videos/04_Photons_Pion_Decay.mp4`
- **Code:** `code/04_Photons_Pion_Decay.py`
- **Sound:** N/A

## Description
TikTok animation explaining Einstein's discovery of photons (1905), neutral pion decay π⁰ → γ + γ, and relativistic beaming. Shows how cosmic rays create pions that decay into gamma radiation, and how relativistic beaming concentrates radiation in the forward direction.

## Development History

### Initial Prompt
"Make a video on this. Photons. Around the same time the scientific community was digesting Einstein's new and radical theory of relativity, Einstein was making inroads on other problems in physics. In 1905, Einstein published a paper on an interaction between light and electrons on the surfaces of materials. By carefully observing the electrons, he discovered that the radiant energy carried by light is absorbed in particle-like 'packets' called photons."

### What Worked
- **Photon visualization** - Wavy line with arrow representing light as particle
- **Pion decay animation** - Clear π⁰ → γ + γ transition with energy conservation
- **Relativistic beaming** - Side-by-side comparison of rest frame (uniform) vs Earth frame (beamed)
- **Cosmic ray journey** - Visual story from cosmic ray → pion → gamma rays → Earth

### What Didn't Work / Challenges
- Need to balance detail vs TikTok pacing - kept it concise
- Relativistic beaming math is complex - simplified to visual comparison

### Key Insights
- Animation structure: Historical discovery → Physics concept → Real-world application
- Visual comparison (rest frame vs Earth frame) makes relativistic beaming intuitive
- Connecting cosmic rays to everyday radiation makes abstract physics tangible

### Technical Notes
- Uses `PhotonParticle` class for visual representation
- `PionParticle` shows neutral pion with mass label
- Relativistic beaming shown by comparing uniform vs narrow ray distributions
- Cosmic ray simulation shows full chain: cosmic ray → atmosphere → pion → decay → gamma → Earth

### Prompt Style Used
- Direct physics content with clear narrative structure
- Educational content broken into digestible segments
