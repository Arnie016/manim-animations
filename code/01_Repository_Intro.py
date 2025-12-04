from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class RepoIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0a0a1e"
        
        # Add background music (trimmed to match video duration ~12 seconds)
        # Note: Requires ffmpeg/ffprobe to be installed for audio support
        import os
        sound_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "sounds", "01_Repository_Intro.mp3"))
        if os.path.exists(sound_file):
            try:
                # Add sound with duration limit to match video (~12 seconds)
                self.add_sound(sound_file, time_offset=0, duration=12.0)
            except Exception:
                # If audio fails (e.g., ffprobe not found), continue without it
                pass
        
        # Start zoomed out, will zoom in throughout
        initial_scale = 1.0
        
        # Title
        title = Text("Manim Animations", font_size=72, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        
        self.play(FadeIn(title), run_time=0.5)
        self.wait(0.3)
        
        # 1. Repository Structure
        structure_title = Text("Repository Structure", font_size=42, color=YELLOW, weight=BOLD)
        structure_title.move_to(ORIGIN + UP * 0.5)
        
        code_desc = Text("code/ - Manim Python files", font_size=32, color=BLUE_A)
        videos_desc = Text("videos/ - Rendered MP4 files", font_size=32, color=GREEN_A)
        docs_desc = Text("docs/ - Prompt styles & development notes", font_size=32, color=ORANGE)
        
        structure_items = VGroup(code_desc, videos_desc, docs_desc).arrange(DOWN, buff=0.4)
        structure_items.next_to(structure_title, DOWN, buff=0.6)
        
        structure_group = VGroup(structure_title, structure_items)
        
        self.play(FadeIn(structure_group), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(structure_group), run_time=0.8)
        self.wait(0.3)
        
        # 2. Name and Credentials
        name = Text("Arnav Salkade", font_size=48, color=WHITE, weight=BOLD)
        credentials = Text("Computer Engineering at NUS", font_size=32, color=GRAY_A)
        email = Text("itsarnavsalkade@gmail.com (reach out!)", font_size=28, color=YELLOW)
        
        name_group = VGroup(name, credentials, email).arrange(DOWN, buff=0.3)
        name_group.move_to(ORIGIN)
        
        self.play(FadeIn(name_group), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(name_group), run_time=0.8)
        self.wait(0.3)
        
        # 3. Goal (with background animations)
        goal_text = Text("Goal: Use AI for storytelling and learning", font_size=36, color=WHITE)
        goal_text.move_to(ORIGIN)
        
        # Background animations for goal
        bg_animations_goal = self.create_background_animations()
        
        goal_container = VGroup(goal_text, *bg_animations_goal, title)
        
        self.play(FadeIn(goal_text), *[FadeIn(anim) for anim in bg_animations_goal], run_time=1.0)
        
        # Animate goal with zoom
        self.play(
            goal_container.animate.scale(1.15),
            run_time=3.0,
            rate_func=smooth
        )
        
        self.wait(0.5)
        self.play(FadeOut(goal_text), *[FadeOut(anim) for anim in bg_animations_goal], run_time=0.8)
        self.wait(0.3)
        
        # 4. Quote (with more background animations)
        quote_part1 = Text('"Education is not a vessel to be filled', font_size=32, color=GRAY_A)
        quote_part2 = Text('but a spark', font_size=44, color=GOLD, weight=BOLD)
        quote_part3 = Text('to be ignited"', font_size=32, color=GRAY_A)
        
        quote = VGroup(quote_part1, quote_part2, quote_part3).arrange(DOWN, buff=0.2)
        quote.move_to(ORIGIN)
        
        # More background animations for quote
        bg_animations_quote = self.create_background_animations()
        
        self.play(
            FadeIn(quote),
            *[FadeIn(anim) for anim in bg_animations_quote],
            run_time=0.6
        )
        
        # Subtle emphasis on "spark" word
        self.play(
            quote_part2.animate.scale(1.05),
            run_time=0.5
        )
        self.play(
            quote_part2.animate.scale(1/1.05),
            run_time=0.5
        )
        
        # Continue zooming during quote
        quote_container = VGroup(quote, *bg_animations_quote, title)
        self.play(
            quote_container.animate.scale(1.2),
            run_time=4.5,
            rate_func=smooth
        )
        
        self.wait(2.0)
        
        # Final fade out
        all_objects = VGroup(quote, *bg_animations_quote, title)
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.3)
    
    def create_background_animations(self):
        """Create various background animations"""
        animations = VGroup()
        
        # Planets orbiting (left side) - more subtle
        planet1 = Dot(radius=0.08, color=BLUE).shift(LEFT * 5 + UP * 2)
        planet2 = Dot(radius=0.07, color=GREEN).shift(LEFT * 5.5 + UP * 1)
        planet_orbit1 = Circle(radius=0.6, stroke_color=BLUE, stroke_width=0.8, stroke_opacity=0.15).move_to(LEFT * 5 + UP * 2)
        planet_orbit2 = Circle(radius=0.45, stroke_color=GREEN, stroke_width=0.8, stroke_opacity=0.15).move_to(LEFT * 5.5 + UP * 1)
        animations.add(planet_orbit1, planet_orbit2, planet1, planet2)
        
        # Pendulum (right side) - more subtle
        pendulum_pivot = Dot(radius=0.05, color=WHITE).shift(RIGHT * 5 + UP * 2.5)
        pendulum_length = 0.9
        pendulum_bob = Dot(radius=0.08, color=YELLOW).shift(RIGHT * 5 + UP * 2.5 + DOWN * pendulum_length)
        pendulum_string = Line(
            pendulum_pivot.get_center(),
            pendulum_bob.get_center(),
            stroke_color=GRAY_B,
            stroke_width=1
        )
        animations.add(pendulum_pivot, pendulum_string, pendulum_bob)
        
        # Equations (top corners) - more subtle
        eq1 = MathTex(r"e^{i\pi} + 1 = 0", font_size=20, color=GRAY_B).shift(LEFT * 4 + UP * 2.8)
        eq2 = MathTex(r"E = mc^2", font_size=20, color=GRAY_B).shift(RIGHT * 4 + UP * 2.8)
        animations.add(eq1, eq2)
        
        # Relativistic equation (left middle) - more subtle
        eq_rel = MathTex(r"ds^2 = -dt^2 + dx^2", font_size=16, color=GRAY_C).shift(LEFT * 4.5 + UP * 0.5)
        animations.add(eq_rel)
        
        # Black hole spacetime (right middle) - more subtle
        eq_bh = MathTex(r"r_s = \frac{2GM}{c^2}", font_size=16, color=GRAY_C).shift(RIGHT * 4.5 + UP * 0.5)
        animations.add(eq_bh)
        
        # Pole-zero plot (left bottom) - more subtle
        pz_axes = Axes(
            x_range=[-1.5, 0.5, 0.5],
            y_range=[-1, 1, 0.5],
            axis_config={"color": GRAY_C, "stroke_width": 0.8},
            tips=False,
            x_length=0.9,
            y_length=0.9,
        ).shift(LEFT * 4.5 + DOWN * 2)
        
        pole_mark = VGroup(
            Line(UP*0.06+LEFT*0.06, DOWN*0.06+RIGHT*0.06, stroke_width=1, color=RED),
            Line(UP*0.06+RIGHT*0.06, DOWN*0.06+LEFT*0.06, stroke_width=1, color=RED)
        ).move_to(pz_axes.coords_to_point(-0.8, 0.3))
        
        zero_mark = Circle(radius=0.05, stroke_width=1, stroke_color=GREEN).move_to(
            pz_axes.coords_to_point(-0.5, -0.4)
        )
        animations.add(pz_axes, pole_mark, zero_mark)
        
        # Frequency analysis graph (right bottom) - more subtle
        freq_x = np.linspace(0, 4*np.pi, 60)
        freq_y = np.sin(freq_x) * 0.2 + np.sin(2*freq_x) * 0.1
        freq_graph = VMobject()
        freq_graph.set_points_as_corners([
            [x * 0.25 + 4.5, freq_y[i] - 2, 0]
            for i, x in enumerate(freq_x)
        ])
        freq_graph.set_stroke(color=BLUE, width=1)
        animations.add(freq_graph)
        
        # Static sine wave (right side) - no animation, just visual
        sine_x = np.linspace(0, 2*np.pi, 30)
        sine_y = np.sin(sine_x) * 0.3
        sine_curve = VMobject()
        sine_curve.set_points_as_corners([
            [x * 0.25 + 5, sine_y[i] + 0.5, 0]
            for i, x in enumerate(sine_x)
        ])
        sine_curve.set_stroke(color="#00FFFF", width=1)
        animations.add(sine_curve)
        
        return animations
