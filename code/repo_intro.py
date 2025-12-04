from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class RepoIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0a0a1e"
        
        # Title
        title = Text("Manim Animations", font_size=72, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        
        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.3)
        
        # Directory structure (centered)
        structure_title = Text("Repository Structure", font_size=36, color=YELLOW)
        structure_title.next_to(title, DOWN, buff=0.5)
        
        structure_items = VGroup(
            Text("code/", font_size=32, color=BLUE_A),
            Text("videos/", font_size=32, color=GREEN_A),
            Text("docs/", font_size=32, color=ORANGE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        structure_items.next_to(structure_title, DOWN, buff=0.4)
        
        self.play(FadeIn(structure_title), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(structure_items, lag_ratio=0.3), run_time=0.8)
        self.wait(0.4)
        
        # Author info (centered)
        author_name = Text("Arnav Salkade", font_size=40, color=WHITE, weight=BOLD)
        author_info = Text("Computer Engineering at NUS", font_size=28, color=GRAY_A)
        author_group = VGroup(author_name, author_info).arrange(DOWN, buff=0.2)
        author_group.next_to(structure_items, DOWN, buff=0.6)
        
        self.play(
            FadeOut(structure_title, shift=UP*0.2),
            FadeOut(structure_items, shift=UP*0.2),
            FadeIn(author_group, shift=DOWN*0.2),
            run_time=1.0
        )
        self.wait(0.4)
        
        # Goal (centered)
        goal_title = Text("Goal:", font_size=32, color=YELLOW)
        goal_text = Text("Use AI for storytelling and learning", font_size=28, color=WHITE)
        goal_group = VGroup(goal_title, goal_text).arrange(RIGHT, buff=0.3)
        goal_group.next_to(author_group, DOWN, buff=0.5)
        
        self.play(FadeIn(goal_group), run_time=0.7)
        self.wait(0.4)
        
        # Move everything up to make room for quote and side animations
        center_group = VGroup(title, author_group, goal_group)
        self.play(center_group.animate.shift(UP * 1.2), run_time=0.8)
        
        # Quote centered with emphasis
        quote_part1 = Text('"Education is not a vessel to be filled', font_size=28, color=GRAY_A)
        quote_part2 = Text('but a spark', font_size=36, color=GOLD, weight=BOLD)
        quote_part3 = Text('to be ignited"', font_size=28, color=GRAY_A)
        
        quote = VGroup(quote_part1, quote_part2, quote_part3).arrange(DOWN, buff=0.15)
        quote.move_to(ORIGIN)
        
        # Add spark effect around "spark"
        spark_circle = Circle(radius=0.8, stroke_color=GOLD, stroke_width=3, stroke_opacity=0.6)
        spark_circle.move_to(quote_part2.get_center())
        spark_particles = VGroup(*[
            Dot(radius=0.05, color=GOLD).move_to(
                spark_circle.get_center() + 0.8 * np.array([np.cos(angle), np.sin(angle), 0])
            )
            for angle in np.linspace(0, 2*np.pi, 8, endpoint=False)
        ])
        spark_group = VGroup(spark_circle, spark_particles)
        
        self.play(FadeIn(quote), run_time=0.8)
        self.wait(0.3)
        self.play(
            FadeIn(spark_group),
            quote_part2.animate.scale(1.1),
            run_time=0.6
        )
        self.play(
            spark_group.animate.scale(1.2),
            quote_part2.animate.scale(1.0),
            run_time=0.5
        )
        
        # Left side animation: s-plane with poles/zeros
        left_axes = Axes(
            x_range=[-2, 1, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": GRAY_B, "stroke_width": 2},
            tips=False,
            x_length=2,
            y_length=2,
        ).shift(LEFT * 4.5)
        
        left_pole = VGroup(
            Line(UP*0.12+LEFT*0.12, DOWN*0.12+RIGHT*0.12, stroke_width=3, color=RED),
            Line(UP*0.12+RIGHT*0.12, DOWN*0.12+LEFT*0.12, stroke_width=3, color=RED)
        ).move_to(left_axes.coords_to_point(-1, 0.5))
        
        left_zero = Circle(radius=0.1, stroke_width=2.5, stroke_color=GREEN).move_to(
            left_axes.coords_to_point(-0.5, -0.8)
        )
        
        left_group = VGroup(left_axes, left_pole, left_zero)
        
        # Right side animation: polar curve
        omega = np.logspace(-1, 1, 150)
        s = 1j * omega
        H = 1.0 / ((s + 1) * (s + 0.5 - 0.8j) * (s + 0.5 + 0.8j))
        magnitude = np.abs(H)
        phase = np.unwrap(np.angle(H))
        
        def polar_func(t):
            idx = min(int(t * (len(omega) - 1)), len(omega) - 1)
            r = magnitude[idx] * 0.3
            theta = phase[idx]
            return np.array([r * np.cos(theta), r * np.sin(theta), 0])
        
        right_curve = ParametricFunction(
            polar_func,
            t_range=[0, 1],
            stroke_width=3,
            color=BLUE,
        ).shift(RIGHT * 4.5)
        
        # Animate side visuals
        self.play(
            FadeIn(left_group, shift=RIGHT*0.5),
            FadeIn(right_curve, shift=LEFT*0.5),
            run_time=1.0
        )
        self.wait(0.3)
        
        # Animate left: add another pole
        left_pole2 = VGroup(
            Line(UP*0.12+LEFT*0.12, DOWN*0.12+RIGHT*0.12, stroke_width=3, color=RED),
            Line(UP*0.12+RIGHT*0.12, DOWN*0.12+LEFT*0.12, stroke_width=3, color=RED)
        ).move_to(left_axes.coords_to_point(-1.5, -0.5))
        
        self.play(FadeIn(left_pole2), run_time=0.5)
        
        # Animate right: trace the curve
        dot = Dot(color=BLUE, radius=0.08).move_to(right_curve.point_from_proportion(0))
        self.add(dot)
        self.play(MoveAlongPath(dot, right_curve), run_time=1.2, rate_func=linear)
        self.wait(0.5)
        
        # Final hold
        self.wait(1.0)
        
        # Fade out
        all_objects = VGroup(center_group, quote, spark_group, left_group, left_pole2, right_curve, dot)
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
