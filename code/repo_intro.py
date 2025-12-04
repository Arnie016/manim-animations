from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class RepoIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0a0a1e"
        
        # Title
        title = Text("Manim Animations", font_size=64, color=WHITE, weight=BOLD)
        subtitle = Text("Visualizing complex math through beautiful animations", 
                       font_size=32, color=GRAY_A)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        
        self.play(FadeIn(title_group), run_time=1.5)
        self.wait(0.5)
        
        # Quick demo: s-plane with poles/zeros
        demo_group = VGroup()
        
        # S-plane axes
        axes = Axes(
            x_range=[-2, 1, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": GRAY_B},
            tips=False,
        ).scale(0.6)
        
        # Add a pole and zero quickly
        pole = VGroup(
            Line(UP*0.15+LEFT*0.15, DOWN*0.15+RIGHT*0.15, stroke_width=4, color=RED),
            Line(UP*0.15+RIGHT*0.15, DOWN*0.15+LEFT*0.15, stroke_width=4, color=RED)
        ).move_to(axes.coords_to_point(-1, 0))
        
        zero = Circle(radius=0.12, stroke_width=3, stroke_color=GREEN).move_to(
            axes.coords_to_point(-0.5, 0.8)
        )
        
        demo_group.add(axes, pole, zero)
        demo_group.next_to(title_group, DOWN, buff=0.8)
        
        self.play(
            FadeOut(title_group, shift=UP*0.5),
            FadeIn(demo_group, shift=DOWN*0.5),
            run_time=1.2
        )
        
        # Show polar curve briefly
        omega = np.logspace(-1, 1, 200)
        s = 1j * omega
        H = 1.0 / ((s + 1) * (s + 0.5 - 0.8j) * (s + 0.5 + 0.8j))
        magnitude = np.abs(H)
        phase = np.unwrap(np.angle(H))
        
        def polar_func(t):
            idx = min(int(t * (len(omega) - 1)), len(omega) - 1)
            r = magnitude[idx] * 0.4
            theta = phase[idx]
            return np.array([r * np.cos(theta), r * np.sin(theta), 0])
        
        polar_curve = ParametricFunction(
            polar_func,
            t_range=[0, 1],
            stroke_width=3,
            color=BLUE,
        ).move_to(demo_group.get_center() + RIGHT * 2)
        
        self.play(Create(polar_curve), run_time=1.5)
        self.wait(0.3)
        
        # Final tagline
        tagline = Text("Control Systems • Transfer Functions • Frequency Response", 
                      font_size=24, color=GRAY_B)
        tagline.to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(tagline), run_time=0.8)
        self.wait(1)
        
        # Fade out
        self.play(FadeOut(VGroup(demo_group, polar_curve, tagline)), run_time=0.8)
        self.wait(0.5)

