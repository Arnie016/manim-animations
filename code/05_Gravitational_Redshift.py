from manim import *
import numpy as np

# TikTok 9:16 - use top 3/4 for content
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#000000"

TOP_REGION_TOP = 6.0
TOP_REGION_BOTTOM = -4.0


class BlackHole(VGroup):
    """Visual representation of a black hole."""
    def __init__(self, radius=0.8, **kwargs):
        super().__init__(**kwargs)
        # Event horizon
        horizon = Circle(radius=radius, color=BLACK, fill_opacity=1.0, stroke_width=0)
        
        # Accretion disk glow
        glow_layers = VGroup()
        for i in range(5):
            layer_radius = radius * (1.5 + i * 0.3)
            layer = Circle(
                radius=layer_radius,
                stroke_width=0,
                fill_color=interpolate_color(ORANGE, BLACK, i / 5),
                fill_opacity=0.3 - i * 0.05,
            )
            glow_layers.add(layer)
        
        # Inner bright ring (accretion disk)
        ring = Circle(
            radius=radius * 1.4,
            stroke_color=ORANGE,
            stroke_width=4,
            fill_opacity=0,
        )
        
        self.add(glow_layers, ring, horizon)
        self.horizon = horizon
        self.ring = ring


class Astronaut(VGroup):
    """Simple astronaut figure."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Helmet
        helmet = Circle(radius=0.25, color=WHITE, stroke_width=3, fill_color=BLUE_D, fill_opacity=0.3)
        # Body
        body = RoundedRectangle(
            width=0.35, height=0.5, corner_radius=0.1,
            color=WHITE, stroke_width=3, fill_color=GREY, fill_opacity=0.5,
        )
        body.next_to(helmet, DOWN, buff=0.05)
        # Arms
        left_arm = Line(body.get_corner(UL), body.get_corner(UL) + LEFT * 0.2 + DOWN * 0.15, color=WHITE, stroke_width=3)
        right_arm = Line(body.get_corner(UR), body.get_corner(UR) + RIGHT * 0.2 + DOWN * 0.15, color=WHITE, stroke_width=3)
        # Legs
        left_leg = Line(body.get_corner(DL), body.get_corner(DL) + LEFT * 0.1 + DOWN * 0.25, color=WHITE, stroke_width=3)
        right_leg = Line(body.get_corner(DR), body.get_corner(DR) + RIGHT * 0.1 + DOWN * 0.25, color=WHITE, stroke_width=3)
        
        self.add(helmet, body, left_arm, right_arm, left_leg, right_leg)


class Torch(VGroup):
    """Flashlight/torch emitting light."""
    def __init__(self, color=YELLOW, **kwargs):
        super().__init__(**kwargs)
        # Torch body
        body = RoundedRectangle(
            width=0.2, height=0.4, corner_radius=0.05,
            color=GREY, stroke_width=2, fill_color=GREY_D, fill_opacity=0.8,
        )
        # Light beam cone
        beam = Polygon(
            body.get_top(),
            body.get_top() + UP * 1.5 + LEFT * 0.4,
            body.get_top() + UP * 1.5 + RIGHT * 0.4,
            color=color,
            fill_opacity=0.4,
            stroke_width=0,
        )
        self.add(beam, body)
        self.body = body
        self.beam = beam


class SpacetimeGrid(VGroup):
    """Curved spacetime grid."""
    def __init__(self, black_hole_pos=ORIGIN, curvature=1.0, **kwargs):
        super().__init__(**kwargs)
        self.black_hole_pos = black_hole_pos
        self.curvature = curvature
        
        # Create grid lines
        grid_lines = VGroup()
        
        # Horizontal lines
        for y in np.linspace(-3, 5, 12):
            points = []
            for x in np.linspace(-4, 4, 50):
                pos = np.array([x, y, 0])
                # Apply curvature based on distance to black hole
                dist = np.linalg.norm(pos[:2] - black_hole_pos[:2])
                if dist > 0.1:
                    # Warp towards black hole
                    direction = (black_hole_pos[:2] - pos[:2]) / dist
                    warp_strength = curvature * (1 / (dist ** 1.5))
                    warped_pos = pos + np.append(direction * warp_strength, 0)
                    points.append(warped_pos)
                else:
                    points.append(pos)
            
            if len(points) > 1:
                line = VMobject(stroke_color=BLUE_D, stroke_width=1, stroke_opacity=0.3)
                line.set_points_as_corners(points)
                grid_lines.add(line)
        
        # Vertical lines
        for x in np.linspace(-4, 4, 12):
            points = []
            for y in np.linspace(-3, 5, 50):
                pos = np.array([x, y, 0])
                dist = np.linalg.norm(pos[:2] - black_hole_pos[:2])
                if dist > 0.1:
                    direction = (black_hole_pos[:2] - pos[:2]) / dist
                    warp_strength = curvature * (1 / (dist ** 1.5))
                    warped_pos = pos + np.append(direction * warp_strength, 0)
                    points.append(warped_pos)
                else:
                    points.append(pos)
            
            if len(points) > 1:
                line = VMobject(stroke_color=BLUE_D, stroke_width=1, stroke_opacity=0.3)
                line.set_points_as_corners(points)
                grid_lines.add(line)
        
        self.add(grid_lines)


class GravitationalRedshiftScene(Scene):
    def construct(self):
        self.camera.background_color = config.background_color
        
        # Title
        title = Text("Gravitational Redshift", font_size=52, weight=BOLD, color=WHITE)
        title.shift(UP * TOP_REGION_TOP)
        self.play(FadeIn(title), run_time=0.7)
        
        subtitle = Text("Light escaping a black hole's gravity", font_size=32, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(0.5)
        
        # Part 1: The Setup
        self.play(FadeOut(subtitle), run_time=0.3)
        
        setup_text = Text("An astronaut falls toward a black hole", font_size=36, color=BLUE_B)
        setup_text.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(setup_text), run_time=0.5)
        
        # Black hole at bottom
        black_hole = BlackHole(radius=0.6)
        black_hole.shift(DOWN * 3.5)
        self.play(FadeIn(black_hole, scale=0.5), run_time=0.8)
        
        # Astronaut above
        astronaut = Astronaut()
        astronaut.shift(UP * 2.5)
        self.play(FadeIn(astronaut), run_time=0.5)
        
        # Torch below astronaut
        torch = Torch(color=BLUE)
        torch.shift(UP * 0.5)
        torch_label = Text("Blue light torch", font_size=24, color=BLUE)
        torch_label.next_to(torch, RIGHT, buff=0.3)
        self.play(FadeIn(torch), FadeIn(torch_label), run_time=0.5)
        
        self.wait(0.6)
        self.play(FadeOut(setup_text), run_time=0.3)
        
        # Part 2: Light climbing out of gravity well
        climb_text = Text("Light must climb out of gravity well", font_size=34, color=YELLOW)
        climb_text.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(climb_text), run_time=0.5)
        
        # Animate light beam traveling up
        light_beam = Arrow(
            torch.get_top(),
            astronaut.get_bottom(),
            buff=0.2,
            color=BLUE,
            stroke_width=6,
        )
        self.play(GrowArrow(light_beam), run_time=0.7)
        
        energy_text = Text("Light loses energy climbing up", font_size=30, color=ORANGE)
        energy_text.next_to(climb_text, DOWN, buff=0.3)
        self.play(FadeIn(energy_text), run_time=0.5)
        
        self.wait(0.6)
        self.play(FadeOut(climb_text), FadeOut(energy_text), run_time=0.3)
        
        # Part 3: Move closer to black hole
        closer_text = Text("As they fall closer...", font_size=36, color=RED_C)
        closer_text.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(closer_text), run_time=0.5)
        
        # Move astronaut and torch down
        self.play(
            astronaut.animate.shift(DOWN * 1.5),
            torch.animate.shift(DOWN * 1.5),
            torch_label.animate.shift(DOWN * 1.5),
            light_beam.animate.shift(DOWN * 1.5),
            run_time=1.2,
        )
        
        gravity_text = Text("Gravity gets stronger", font_size=30, color=RED_C)
        gravity_text.next_to(closer_text, DOWN, buff=0.3)
        self.play(FadeIn(gravity_text), run_time=0.5)
        
        self.wait(0.5)
        self.play(FadeOut(closer_text), FadeOut(gravity_text), run_time=0.3)
        
        # Part 4: Spacetime curvature
        spacetime_text = Text("Spacetime curves more", font_size=36, color=TEAL_B)
        spacetime_text.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(spacetime_text), run_time=0.5)
        
        # Add spacetime grid
        grid = SpacetimeGrid(black_hole_pos=black_hole.get_center(), curvature=0.5)
        grid.set_opacity(0.5)
        self.play(FadeIn(grid), run_time=0.8)
        
        curve_explain = Text("Light must work harder to escape", font_size=30, color=GRAY_B)
        curve_explain.next_to(spacetime_text, DOWN, buff=0.3)
        self.play(FadeIn(curve_explain), run_time=0.5)
        
        self.wait(0.6)
        self.play(FadeOut(spacetime_text), FadeOut(curve_explain), run_time=0.3)
        
        # Part 5: Frequency change
        freq_text = Text("Astronaut sees color change!", font_size=36, color=YELLOW)
        freq_text.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(freq_text), run_time=0.5)
        
        # Show frequency shift progression
        colors = [BLUE, BLUE_C, GREEN, YELLOW, ORANGE, RED]
        color_names = ["Blue", "Cyan", "Green", "Yellow", "Orange", "Red"]
        
        for i, (color, name) in enumerate(zip(colors, color_names)):
            new_beam = Arrow(
                torch.get_top(),
                astronaut.get_bottom(),
                buff=0.2,
                color=color,
                stroke_width=6,
            )
            new_label = Text(f"{name} light", font_size=24, color=color)
            new_label.next_to(torch, RIGHT, buff=0.3)
            
            self.play(
                Transform(light_beam, new_beam),
                Transform(torch_label, new_label),
                run_time=0.4,
            )
            self.wait(0.2)
        
        redshift_explain = Text("This is gravitational redshift", font_size=30, color=RED_C)
        redshift_explain.next_to(freq_text, DOWN, buff=0.3)
        self.play(FadeIn(redshift_explain), run_time=0.5)
        
        self.wait(0.7)
        self.play(FadeOut(freq_text), FadeOut(redshift_explain), run_time=0.3)
        
        # Part 6: Even closer - extreme redshift
        extreme_text = Text("Even closer to the black hole...", font_size=36, color=RED_D)
        extreme_text.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(extreme_text), run_time=0.5)
        
        # Move even closer
        self.play(
            astronaut.animate.shift(DOWN * 1.2),
            torch.animate.shift(DOWN * 1.2),
            torch_label.animate.shift(DOWN * 1.2),
            light_beam.animate.shift(DOWN * 1.2),
            run_time=1.0,
        )
        
        # Increase curvature
        new_grid = SpacetimeGrid(black_hole_pos=black_hole.get_center(), curvature=1.2)
        new_grid.set_opacity(0.5)
        self.play(Transform(grid, new_grid), run_time=0.8)
        
        # Light becomes infrared (invisible)
        invisible_text = Text("Light shifts to infrared (invisible!)", font_size=30, color=DARK_GREY)
        invisible_text.next_to(extreme_text, DOWN, buff=0.3)
        self.play(FadeIn(invisible_text), run_time=0.5)
        
        # Fade out light beam
        self.play(
            light_beam.animate.set_opacity(0.1),
            torch_label.animate.set_opacity(0.3),
            run_time=0.7,
        )
        
        self.wait(0.6)
        self.play(FadeOut(extreme_text), FadeOut(invisible_text), run_time=0.3)
        
        # Part 7: The physics intuition
        intuition_text = Text("Why does this happen?", font_size=38, weight=BOLD, color=YELLOW)
        intuition_text.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intuition_text), run_time=0.5)
        
        explain1 = Text("1. Light is like a wave", font_size=32, color=BLUE_B)
        explain1.shift(UP * 1.5)
        self.play(FadeIn(explain1), run_time=0.5)
        
        explain2 = Text("2. Climbing gravity stretches the wave", font_size=32, color=GREEN_C)
        explain2.next_to(explain1, DOWN, buff=0.3)
        self.play(FadeIn(explain2), run_time=0.5)
        
        explain3 = Text("3. Stretched wave = lower frequency", font_size=32, color=YELLOW)
        explain3.next_to(explain2, DOWN, buff=0.3)
        self.play(FadeIn(explain3), run_time=0.5)
        
        explain4 = Text("4. Lower frequency = redder color", font_size=32, color=RED_C)
        explain4.next_to(explain3, DOWN, buff=0.3)
        self.play(FadeIn(explain4), run_time=0.5)
        
        self.wait(1.0)
        
        # Clear for finale
        self.play(
            FadeOut(VGroup(intuition_text, explain1, explain2, explain3, explain4,
                          astronaut, torch, torch_label, light_beam, grid)),
            run_time=0.5,
        )
        
        # Part 8: Visual wave demonstration
        wave_title = Text("Light wave stretching", font_size=38, weight=BOLD, color=YELLOW)
        wave_title.shift(UP * 3.5)
        self.play(FadeIn(wave_title), run_time=0.5)
        
        # Normal wave
        normal_label = Text("Far from black hole: Normal frequency", font_size=28, color=BLUE)
        normal_label.shift(UP * 2.0)
        self.play(FadeIn(normal_label), run_time=0.4)
        
        normal_wave = FunctionGraph(
            lambda x: 0.3 * np.sin(4 * x),
            x_range=[-4, 4],
            color=BLUE,
            stroke_width=4,
        )
        normal_wave.shift(UP * 1.0)
        self.play(Create(normal_wave), run_time=0.8)
        
        self.wait(0.5)
        
        # Stretched wave
        stretched_label = Text("Near black hole: Stretched (redshifted)", font_size=28, color=RED)
        stretched_label.shift(DOWN * 0.5)
        self.play(FadeIn(stretched_label), run_time=0.4)
        
        stretched_wave = FunctionGraph(
            lambda x: 0.3 * np.sin(2 * x),
            x_range=[-4, 4],
            color=RED,
            stroke_width=4,
        )
        stretched_wave.shift(DOWN * 1.5)
        self.play(Create(stretched_wave), run_time=0.8)
        
        comparison = Text("Fewer peaks = lower frequency = redder", font_size=26, color=ORANGE)
        comparison.shift(DOWN * 3.0)
        self.play(FadeIn(comparison), run_time=0.5)
        
        self.wait(1.0)
        
        # Final summary
        self.play(
            FadeOut(VGroup(wave_title, normal_label, normal_wave, stretched_label, 
                          stretched_wave, comparison, black_hole)),
            run_time=0.5,
        )
        
        summary_title = Text("Gravitational Redshift", font_size=48, weight=BOLD, color=YELLOW)
        summary_title.shift(UP * 2.5)
        
        sum1 = Text("Light loses energy escaping gravity", font_size=32, color=BLUE_B)
        sum1.shift(UP * 1.3)
        
        sum2 = Text("Energy loss = frequency decrease", font_size=32, color=GREEN_C)
        sum2.shift(UP * 0.3)
        
        sum3 = Text("Lower frequency = redder color", font_size=32, color=ORANGE)
        sum3.shift(DOWN * 0.7)
        
        sum4 = Text("Stronger gravity = more redshift", font_size=32, color=RED_C)
        sum4.shift(DOWN * 1.7)
        
        self.play(
            FadeIn(summary_title),
            FadeIn(sum1),
            FadeIn(sum2),
            FadeIn(sum3),
            FadeIn(sum4),
            run_time=1.0,
        )
        
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(title, summary_title, sum1, sum2, sum3, sum4)),
            run_time=0.6,
        )

