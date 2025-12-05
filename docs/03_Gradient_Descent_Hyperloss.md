# Gradient Descent Hyperloss

## Video
- **File:** `videos/03_Gradient_Descent_Hyperloss.mp4`
- **Code:** `code/03_Gradient_Descent_Hyperloss.py`
- **Sound:** `sounds/03_Gradient_Descent_Hyperloss.mp3` (if applicable)

## Description
TikTok animation showing language model training with:
- **Traced loss curve** - Realistic fluctuating descent (goes down but bounces around like real SGD)
- **Regional weight cloud** - 5 labeled sub-regions (Food, Politics, Philosophy, Tech, General) with ~175 vectors
- **10 epochs** - Each shows gibberish → partial → aligned output
- **Region activation** - Vectors in relevant region glow and move when that topic is trained

## Layout
```
┌─────────────────────────────────┐
│   "Training a Language Model"   │
├─────────────────────────────────┤
│   [Loss Curve with tracer dot]  │  ← Realistic fluctuating descent
│    ●                            │
│     ╲●─●                        │
│         ╲●─●─●─●─●              │
├─────────────────────────────────┤
│       Epoch 5/10                │
├─────────────────────────────────┤
│   Input: [token] [chips]        │
├─────────────────────────────────┤
│  ┌─Food─┐    ┌─Politics─┐       │
│  │ ●●●● │    │  ●●●●    │       │
│  └──────┘    └──────────┘       │
│       ┌─General─┐               │  ← Regional cloud
│       │  ●●●●   │               │
│       └─────────┘               │
│  ┌Philosophy┐  ┌──Tech──┐       │
│  │  ●●●●    │  │  ●●●●  │       │
│  └──────────┘  └────────┘       │
├─────────────────────────────────┤
│   Output: "Aligned response"    │
└─────────────────────────────────┘
```

## Loss Trajectory
Realistic SGD behavior - trends down but explores:
```python
loss_trajectory = [
    (0, 4.8),                       # start high
    (1, 4.5), (2, 4.7), (3, 4.2),   # epoch 1 - bounces up
    (4, 3.8), (5, 4.0), (6, 3.5),   # epoch 2 - still bumpy
    ...
    (28, 0.5), (29, 0.45), (30, 0.4) # converged
]
```

## Training Examples
| Epoch | Input | Region | Final Output |
|-------|-------|--------|--------------|
| 1 | Pineapple on pizza? | Food | Pineapple on pizza is great! |
| 2 | Is chocolate healthy? | Food | Dark chocolate has benefits. |
| 3 | Best breakfast? | Food | Eggs provide protein. |
| 4 | Is democracy good? | Politics | Democracy enables voice. |
| 5 | Best economy? | Politics | Mixed economies balance. |
| 6 | Free will exists? | Philosophy | Philosophically debated. |
| 7 | Meaning of life? | Philosophy | Subjectively defined. |
| 8 | Who made internet? | Tech | ARPANET team created it. |
| 9 | Coffee or tea? | Food | Coffee gives energy. |
| 10 | Will AI help us? | Tech | AI augments humans. |

## Technical Notes
- `TracedLossCurve` - 30 data points, glowing yellow tracer dot
- `RegionalCloud` - 5 regions × 35 vectors = 175 total
- `activate_region()` - Highlights boundary, moves vectors in that region
- `backprop_wave()` - Expanding circle from output to cloud
- Fast pacing: 0.1-0.4s per animation

## Development History
1. "Gradient descent for TikTok"
2. "3D point cloud, tokenization, gibberish → aligned"
3. "Plot loss curve, 10 epochs, regional cloud"
4. "Trace the loss - realistic fluctuating descent"
