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
        title.to_edge(UP, buff=0.8)
        
        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.3)
        
        # Directory structure
        structure_title = Text("Repository Structure", font_size=36, color=YELLOW)
        structure_title.next_to(title, DOWN, buff=0.6)
        
        structure_items = VGroup(
            Text("code/", font_size=32, color=BLUE_A),
            Text("videos/", font_size=32, color=GREEN_A),
            Text("docs/", font_size=32, color=ORANGE),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        structure_items.next_to(structure_title, DOWN, buff=0.5)
        
        self.play(FadeIn(structure_title), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(structure_items, lag_ratio=0.3), run_time=1.0)
        self.wait(0.5)
        
        # Author info
        author_name = Text("Arnav Salkade", font_size=40, color=WHITE, weight=BOLD)
        author_info = Text("Computer Engineering at NUS", font_size=28, color=GRAY_A)
        author_group = VGroup(author_name, author_info).arrange(DOWN, buff=0.2)
        author_group.next_to(structure_items, DOWN, buff=0.8)
        
        self.play(
            FadeOut(structure_title, shift=UP*0.3),
            FadeOut(structure_items, shift=UP*0.3),
            FadeIn(author_group, shift=DOWN*0.3),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Goal
        goal_title = Text("Goal:", font_size=32, color=YELLOW)
        goal_text = Text("Use AI for storytelling and learning", font_size=28, color=WHITE)
        goal_group = VGroup(goal_title, goal_text).arrange(RIGHT, buff=0.3)
        goal_group.next_to(author_group, DOWN, buff=0.6)
        
        self.play(FadeIn(goal_group), run_time=0.8)
        self.wait(0.5)
        
        # Quote
        quote = Text(
            '"Education is not a vessel to be filled\nbut a spark to be ignited"',
            font_size=32,
            color=GOLD,
        )
        quote.next_to(goal_group, DOWN, buff=0.8)
        
        self.play(FadeIn(quote), run_time=1.0)
        self.wait(1.5)
        
        # Fade out
        self.play(FadeOut(VGroup(title, author_group, goal_group, quote)), run_time=1.0)
        self.wait(0.5)
