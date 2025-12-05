# Gradient Descent Hyperloss - Transformer Training Animation

## Video
- **File:** `videos/03_Gradient_Descent_Hyperloss.mp4`
- **Code:** `code/03_Gradient_Descent_Hyperloss.py`
- **Sound:** N/A

## Description
TikTok-ready (9:16) animation showing how a transformer learns through gradient descent. Displays Expected vs Output comparison where output evolves from gibberish → partial → aligned as backpropagation updates weights across all layers in real-time.

## Final Layout
```
┌───────────────────────────────────┐
│    Transformer Training           │
├───────────────────────────────────┤
│   [Traced Loss Curve]             │
│         Step 5                    │
├───────────────────────────────────┤
│   Input: "Pineapple pizza?"       │
├───────────────────────────────────┤
│   Embed     │ ●●●●●●●●●●●●●●●●   │
│   Attention │ ●●●●●●●●●●●●●●●●   │
│   MoE       │ ●●●●●●●●●●●●●●●●   │
│   FFN       │ ●●●●●●●●●●●●●●●●   │
│   Output    │ ●●●●●●●●●●●●●●●●   │
├───────────────────────────────────┤
│   Expected: "Pineapple is great!" │  ← GREEN target
├───────────────────────────────────┤
│   Output:   "<<0x7f3a>>"          │  ← RED → YELLOW → GREEN
└───────────────────────────────────┘
```

## Development History

### Initial Prompts (Verbatim)
1. "Let's do the gradient descent on a loss function. We will show many dimensions... a model has millions of weights... I want this in the animation step-by-step. It should be for TikTok."

2. "The particle clouds can have really tiny vectors, and you can show one of them having a floating point number. Then perhaps a loss function equation and the animation should be like the input goes into this cloud and the output is like a sentence."

3. "Only the point cloud should be 3D; all text/UI must stay perfectly 2D with loss at the top, input under it, point cloud in the middle, and output pinned to the bottom."

4. "Only make it 2D please... Improve the progress bar, and also the output should not be kept awaiting at each time it should first be gibberish then form sentences and then slowly align."

5. "Much better but make sure the vector and points are better animated and its like a spherical cloud shape perhaps 3D? Also make sure the texts don't overlap."

6. "The graphs should be traced. See a line going down was like kind of an exponential, but then it goes a bit here and there. So it's exploring the loss."

7. "Add more richer 3D vectors and filling up entire section with attention blocks and MoE simulated like basic point cloud vectors of the transformers."

8. "The text is kind of slanted; it should be 2D please. Also, I don't know why there's an unnecessary animation. I think it should flow through the network, and the weights should be seen updating in real-time."

9. "Ok currently much better but make sure there is output and expected output above it, like the output should first be gibberish then the model slowly learns after backpropagation and weight updates in the entire network."

10. "Much better I like it, space it all out please so it's visible entire 9:16 screen right now bottom space is empty."

### What Worked
- **Pure 2D Scene** - No slanted text, clean readability
- **Expected vs Output comparison** - Clear learning visualization
- **3-stage output progression** - RED gibberish → YELLOW partial → GREEN aligned
- **Traced loss curve** - Realistic fluctuating descent (not smooth)
- **Backprop wave** - Red line sweeps bottom to top
- **Simultaneous weight updates** - All 260 dots shift at once
- **Full screen layout** - Elements spread across entire 9:16

### What Didn't Work / Challenges
- **3D ThreeDScene** - Text was slanted, hard to read
- **Smooth loss curves** - Looked unrealistic, needed fluctuation
- **Small UI elements** - Wasted screen space on TikTok format
- **Sequential weight updates** - Too slow, simultaneous is better
- **Extra animations** - Removed unnecessary pauses and transitions
- **Regional cloud labels** - Added complexity without clarity

### Key Insights
- TikTok vertical format needs elements spread across full height
- Backprop visualization (wave + weight shift) sells the learning story
- Expected/Output comparison makes alignment visually obvious
- Loss curve fluctuation shows realistic SGD exploration
- Forward flow (yellow particles) + backward flow (red wave) = complete picture

### Technical Notes
```python
# Config
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# Loss trajectory - fluctuating descent
loss_data = [(0, 4.8), (1, 4.6), (2, 4.7), ...]  # Goes up and down

# Network layers
block_specs = [
    ("Embed", 0, 2.4, BLUE_B, 40),
    ("Attention", 0, 1.2, RED_C, 55),
    ("MoE", 0, 0, ORANGE, 70),
    ("FFN", 0, -1.2, PURPLE_B, 55),
    ("Output", 0, -2.4, GREEN_C, 40),
]  # Total: ~260 weight dots

# Output stages
stages = ["<<0x7f3a>>", "Maybe... fruit on...", "Pineapple on pizza is great!"]
colors = [RED_C, YELLOW_C, GREEN_C]
```

### Training Examples Used
| Step | Input | Expected | Gibberish | Partial | Aligned |
|------|-------|----------|-----------|---------|---------|
| 1 | Pineapple pizza? | Pineapple on pizza is great! | <<0x7f3a>> | Maybe... fruit on... | ✓ |
| 2 | Chocolate healthy? | Dark chocolate has benefits. | <<err_null>> | Sugar... cocoa... | ✓ |
| 3 | Best breakfast? | Eggs are very nutritious. | <<0xfood>> | Morning... protein... | ✓ |
| 4 | Democracy good? | Democracy enables citizen voice. | <<gov_??>> | System... voting... | ✓ |
| 5 | Free will exists? | Free will is philosophically debated. | <<choice>> | Determinism... agency... | ✓ |
| 6 | Life meaning? | Meaning is subjectively constructed. | <<exist??>> | Purpose... happiness... | ✓ |
| 7 | Internet inventor? | ARPANET team created internet. | <<Al_Gore>> | Network... DARPA... | ✓ |
| 8 | Coffee vs tea? | Coffee provides quick energy. | <<drink>> | Caffeine... taste... | ✓ |
| 9 | AI helpful? | AI augments human capabilities. | <<future>> | Automation... tools... | ✓ |
| 10 | Best economy? | Mixed economies balance needs. | <<money>> | Markets... welfare... | ✓ |

### Prompt Style That Worked
- Iterative refinement: Start broad, fix issues one by one
- Visual-first requests: "space it out", "fill the screen", "trace the line"
- Explicit rejection: "The text is slanted, should be 2D"
- Comparison requests: "Expected vs Output"

## Repro Command
```bash
cd /Users/hema/Desktop/manim
python3 -m manim -pqh code/03_Gradient_Descent_Hyperloss.py TikTokGradientDescent
cp media/videos/03_Gradient_Descent_Hyperloss/1920p30/TikTokGradientDescent.mp4 videos/
```
