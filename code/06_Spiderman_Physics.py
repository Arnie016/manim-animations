from manim import *
import numpy as np

# TikTok 9:16 - use top 3/4 for content
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#000814"

TOP_REGION_TOP = 6.0
TOP_REGION_BOTTOM = -4.0

# Spider-Man colors
SPIDERMAN_RED = "#DC143C"
SPIDERMAN_BLUE = "#0047AB"
WEB_COLOR = "#E8E8E8"
NYC_GRAY = "#4A4A4A"


class ProgressBar(VGroup):
    """Shows current section of the video."""
    def __init__(self, sections, current=0, **kwargs):
        super().__init__(**kwargs)
        self.sections = sections
        self.current = current
        
        # Create section dots/labels
        section_group = VGroup()
        for i, section in enumerate(sections):
            # Dot
            if i == current:
                dot = Circle(radius=0.12, fill_opacity=1, fill_color=SPIDERMAN_RED, 
                           stroke_color=WHITE, stroke_width=2)
            elif i < current:
                dot = Circle(radius=0.08, fill_opacity=1, fill_color=WHITE, stroke_width=0)
            else:
                dot = Circle(radius=0.08, fill_opacity=0.3, fill_color=GRAY, 
                           stroke_color=GRAY, stroke_width=1)
            
            # Label (only for current)
            if i == current:
                label = Text(section, font_size=20, color=WHITE, weight=BOLD)
                label.next_to(dot, DOWN, buff=0.15)
                section_group.add(VGroup(dot, label))
            else:
                section_group.add(dot)
        
        section_group.arrange(RIGHT, buff=0.5)
        self.add(section_group)


class SpiderMan(VGroup):
    """Stylized Spider-Man figure in iconic pose."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Body (red suit)
        body = Polygon(
            [0, 0.5, 0], [0.25, 0, 0], [0.15, -0.7, 0], 
            [-0.15, -0.7, 0], [-0.25, 0, 0],
            fill_color=SPIDERMAN_RED, fill_opacity=1,
            stroke_color=BLACK, stroke_width=3
        )
        
        # Head/Mask
        head = Circle(radius=0.3, fill_color=SPIDERMAN_RED, fill_opacity=1,
                     stroke_color=BLACK, stroke_width=3)
        head.shift(UP * 0.8)
        
        # Eyes (white)
        left_eye = Polygon(
            [-0.2, 0.85, 0], [-0.05, 0.95, 0], [-0.05, 0.75, 0],
            fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=BLACK
        )
        right_eye = Polygon(
            [0.05, 0.95, 0], [0.2, 0.85, 0], [0.05, 0.75, 0],
            fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=BLACK
        )
        
        # Web pattern on suit
        web1 = Line([0, 0.5, 0], [0.25, 0, 0], color=BLACK, stroke_width=1)
        web2 = Line([0, 0.5, 0], [-0.25, 0, 0], color=BLACK, stroke_width=1)
        web3 = Line([0, 0.2, 0], [0.2, -0.2, 0], color=BLACK, stroke_width=1)
        web4 = Line([0, 0.2, 0], [-0.2, -0.2, 0], color=BLACK, stroke_width=1)
        
        # Arms (swinging pose)
        left_arm = Line([0, 0.3, 0], [-0.5, 0.8, 0], color=SPIDERMAN_RED, stroke_width=8)
        right_arm = Line([0, 0.3, 0], [0.6, 0.6, 0], color=SPIDERMAN_RED, stroke_width=8)
        
        # Legs
        left_leg = Line([0, -0.7, 0], [-0.3, -1.2, 0], color=SPIDERMAN_BLUE, stroke_width=8)
        right_leg = Line([0, -0.7, 0], [0.2, -1.3, 0], color=SPIDERMAN_BLUE, stroke_width=8)
        
        self.add(left_leg, right_leg, body, left_arm, right_arm, head, 
                left_eye, right_eye, web1, web2, web3, web4)


class Building(VGroup):
    """NYC building."""
    def __init__(self, height=4, **kwargs):
        super().__init__(**kwargs)
        
        building = Rectangle(
            width=1.2, height=height,
            fill_color=NYC_GRAY, fill_opacity=0.8,
            stroke_color=WHITE, stroke_width=2
        )
        
        # Windows
        windows = VGroup()
        for i in range(int(height * 3)):
            for j in range(3):
                window = Rectangle(
                    width=0.15, height=0.2,
                    fill_color=YELLOW, fill_opacity=0.6,
                    stroke_width=0
                )
                window.shift(UP * (height/2 - 0.3 - i * 0.35) + 
                           RIGHT * (-0.4 + j * 0.35))
                windows.add(window)
        
        self.add(building, windows)


class CalculationPanel(VGroup):
    """Side panel for calculations."""
    def __init__(self, title, equations, **kwargs):
        super().__init__(**kwargs)
        
        # Panel background
        panel = RoundedRectangle(
            width=3.5, height=2.5, corner_radius=0.15,
            fill_color=BLACK, fill_opacity=0.7,
            stroke_color=SPIDERMAN_RED, stroke_width=2
        )
        
        # Title
        title_text = Text(title, font_size=24, color=SPIDERMAN_RED, weight=BOLD)
        title_text.move_to(panel.get_top() + DOWN * 0.3)
        
        # Equations
        eq_group = VGroup()
        for eq in equations:
            eq_obj = MathTex(eq, font_size=28, color=WHITE)
            eq_group.add(eq_obj)
        eq_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        eq_group.next_to(title_text, DOWN, buff=0.25)
        eq_group.shift(RIGHT * 0.1)
        
        self.add(panel, title_text, eq_group)


class SpidermanPhysics(Scene):
    def construct(self):
        self.camera.background_color = config.background_color
        
        # Section titles
        sections = ["Setup", "Physics", "G-Force", "Damage", "Verdict"]
        
        # Title
        title = Text("Could Spider-Man Actually Swing?", 
                    font_size=42, weight=BOLD, color=WHITE)
        title.shift(UP * TOP_REGION_TOP)
        
        # PART 1: SETUP
        progress = ProgressBar(sections, current=0)
        progress.next_to(title, DOWN, buff=0.3)
        
        self.play(FadeIn(title), FadeIn(progress), run_time=0.5)
        
        # Buildings
        left_building = Building(height=4.5)
        left_building.shift(LEFT * 3.5 + DOWN * 0.5)
        
        right_building = Building(height=5)
        right_building.shift(RIGHT * 3 + DOWN * 0.8)
        
        self.play(FadeIn(left_building), FadeIn(right_building), run_time=0.6)
        
        # Spider-Man swinging
        spiderman = SpiderMan()
        spiderman.scale(0.8).shift(LEFT * 2 + UP * 2)
        
        # Web line
        web = Line(left_building.get_top(), spiderman.get_center(),
                  color=WEB_COLOR, stroke_width=3)
        
        question = Text("Can a REAL human do this?", font_size=32, color=YELLOW)
        question.shift(DOWN * 2.5)
        
        self.play(
            Create(web),
            FadeIn(spiderman),
            FadeIn(question),
            run_time=0.7
        )
        self.wait(0.5)
        self.play(FadeOut(question), run_time=0.3)
        
        # PART 2: PHYSICS
        new_progress = ProgressBar(sections, current=1)
        new_progress.next_to(title, DOWN, buff=0.3)
        self.play(Transform(progress, new_progress), run_time=0.4)
        
        # Show pendulum
        pendulum_label = Text("It's a Pendulum!", font_size=32, color=TEAL_A)
        pendulum_label.shift(DOWN * 2.5)
        self.play(FadeIn(pendulum_label), run_time=0.4)
        
        # Calculation panel (side)
        calc_panel_1 = CalculationPanel(
            "The Math:",
            [
                r"h = 300\text{m (building)}",
                r"L = 100\text{m (web)}",
                r"v = \sqrt{2gL}"
            ]
        )
        calc_panel_1.scale(0.7).to_edge(LEFT, buff=0.3).shift(DOWN * 1)
        
        self.play(FadeIn(calc_panel_1), run_time=0.5)
        
        # Animate swing
        arc_path = ArcBetweenPoints(
            spiderman.get_center(),
            RIGHT * 1 + DOWN * 0.5,
            angle=-PI/3
        )
        
        self.play(
            MoveAlongPath(spiderman, arc_path),
            web.animate.put_start_and_end_on(
                left_building.get_top(), RIGHT * 1 + DOWN * 0.5
            ),
            run_time=1.2,
            rate_func=smooth
        )
        
        self.play(FadeOut(pendulum_label), run_time=0.3)
        
        # BIG NUMBER REVEAL - Speed
        speed_box = Rectangle(
            width=6, height=1.5,
            fill_color=SPIDERMAN_RED, fill_opacity=0.9,
            stroke_color=WHITE, stroke_width=4
        )
        speed_box.shift(DOWN * 2.5)
        
        speed_text = Text("SPEED: 44 m/s", font_size=48, color=WHITE, weight=BOLD)
        speed_subtext = Text("(100 MPH!)", font_size=36, color=YELLOW)
        speed_group = VGroup(speed_text, speed_subtext).arrange(DOWN, buff=0.1)
        speed_group.move_to(speed_box)
        
        self.play(
            FadeIn(speed_box, scale=1.2),
            FadeIn(speed_group, shift=UP * 0.2),
            run_time=0.7
        )
        self.wait(0.6)
        self.play(FadeOut(speed_box), FadeOut(speed_group), run_time=0.3)
        
        # Web tension calculation
        calc_panel_2 = CalculationPanel(
            "Web Tension:",
            [
                r"T = mg(3 - 2\cos\theta)",
                r"m = 75\text{kg}",
                r"T = ?"
            ]
        )
        calc_panel_2.scale(0.7).to_edge(RIGHT, buff=0.3).shift(DOWN * 1)
        
        self.play(FadeIn(calc_panel_2), run_time=0.5)
        
        # BIG NUMBER REVEAL - Tension
        tension_box = Rectangle(
            width=6, height=1.5,
            fill_color=ORANGE, fill_opacity=0.9,
            stroke_color=WHITE, stroke_width=4
        )
        tension_box.shift(DOWN * 2.5)
        
        tension_text = Text("TENSION: 3,000 N", font_size=48, color=WHITE, weight=BOLD)
        tension_subtext = Text("(675 pounds!)", font_size=36, color=YELLOW)
        tension_group = VGroup(tension_text, tension_subtext).arrange(DOWN, buff=0.1)
        tension_group.move_to(tension_box)
        
        self.play(
            FadeIn(tension_box, scale=1.2),
            FadeIn(tension_group, shift=UP * 0.2),
            run_time=0.7
        )
        self.wait(0.6)
        
        self.play(
            FadeOut(tension_box), FadeOut(tension_group),
            FadeOut(calc_panel_1), FadeOut(calc_panel_2),
            run_time=0.3
        )
        
        # PART 3: G-FORCE
        new_progress2 = ProgressBar(sections, current=2)
        new_progress2.next_to(title, DOWN, buff=0.3)
        self.play(Transform(progress, new_progress2), run_time=0.4)
        
        g_force_title = Text("The REAL Problem:", font_size=36, color=RED, weight=BOLD)
        g_force_title.shift(DOWN * 2.5)
        self.play(FadeIn(g_force_title), run_time=0.4)
        self.wait(0.3)
        
        g_force_subtitle = Text("G-FORCES!", font_size=44, color=RED, weight=BOLD)
        g_force_subtitle.next_to(g_force_title, DOWN, buff=0.2)
        self.play(FadeIn(g_force_subtitle, scale=1.3), run_time=0.5)
        self.wait(0.4)
        
        self.play(FadeOut(g_force_title), FadeOut(g_force_subtitle), run_time=0.3)
        
        # G-force calculation panel
        calc_panel_3 = CalculationPanel(
            "Acceleration:",
            [
                r"a = \frac{v^2}{r}",
                r"a = \frac{44^2}{100}",
                r"a = 19\text{ m/s}^2"
            ]
        )
        calc_panel_3.scale(0.7).to_edge(LEFT, buff=0.3).shift(DOWN * 1)
        self.play(FadeIn(calc_panel_3), run_time=0.5)
        
        # BIG NUMBER REVEAL - G-Force
        g_box = Rectangle(
            width=6.5, height=1.8,
            fill_color=RED_D, fill_opacity=0.95,
            stroke_color=WHITE, stroke_width=5
        )
        g_box.shift(DOWN * 2.5)
        
        g_text = Text("2-4 G's", font_size=64, color=WHITE, weight=BOLD)
        g_subtext = Text("Fighter Pilot Level!", font_size=32, color=YELLOW)
        g_group = VGroup(g_text, g_subtext).arrange(DOWN, buff=0.15)
        g_group.move_to(g_box)
        
        self.play(
            FadeIn(g_box, scale=1.3),
            FadeIn(g_group, shift=UP * 0.3),
            Flash(g_box, color=RED, flash_radius=1.5),
            run_time=0.8
        )
        self.wait(0.7)
        
        self.play(
            FadeOut(g_box), FadeOut(g_group), FadeOut(calc_panel_3),
            run_time=0.3
        )
        
        # PART 4: DAMAGE
        new_progress3 = ProgressBar(sections, current=3)
        new_progress3.next_to(title, DOWN, buff=0.3)
        self.play(Transform(progress, new_progress3), run_time=0.4)
        
        damage_title = Text("What Happens to Your Body?", 
                          font_size=34, color=RED, weight=BOLD)
        damage_title.shift(UP * 1.5)
        self.play(FadeIn(damage_title), run_time=0.4)
        
        # Damage list
        damage_items = VGroup(
            Text("🔴 Dislocated Shoulders", font_size=28, color=WHITE),
            Text("🔴 Severe Whiplash", font_size=28, color=WHITE),
            Text("🔴 Internal Injuries", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        damage_items.shift(DOWN * 0.5)
        
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT * 0.3) 
                               for item in damage_items], lag_ratio=0.2), run_time=1.0)
        self.wait(0.5)
        
        # Arm strength comparison
        calc_panel_4 = CalculationPanel(
            "The Numbers:",
            [
                r"\text{Human arm: } 400\text{N}",
                r"\text{Required: } 3000\text{N}",
                r"\text{You'd rip your arms off!}"
            ]
        )
        calc_panel_4.scale(0.7).shift(DOWN * 2.8)
        self.play(FadeIn(calc_panel_4), run_time=0.5)
        self.wait(0.6)
        
        self.play(
            FadeOut(damage_title), FadeOut(damage_items), FadeOut(calc_panel_4),
            run_time=0.3
        )
        
        # PART 5: THE VERDICT
        new_progress4 = ProgressBar(sections, current=4)
        new_progress4.next_to(title, DOWN, buff=0.3)
        self.play(Transform(progress, new_progress4), run_time=0.4)
        
        # Split screen verdict
        verdict_title = Text("THE VERDICT", font_size=44, color=WHITE, weight=BOLD)
        verdict_title.shift(UP * 2)
        self.play(FadeIn(verdict_title), run_time=0.5)
        
        # Normal human - NO
        human_box = Rectangle(
            width=4, height=2.5,
            fill_color=RED_D, fill_opacity=0.3,
            stroke_color=RED, stroke_width=3
        )
        human_box.shift(LEFT * 2.2 + DOWN * 0.5)
        
        human_label = Text("Normal Human", font_size=28, color=WHITE)
        human_label.next_to(human_box, UP, buff=0.2)
        
        human_x = Text("❌", font_size=80, color=RED)
        human_x.move_to(human_box)
        
        human_text = Text("IMPOSSIBLE", font_size=32, color=RED, weight=BOLD)
        human_text.next_to(human_x, DOWN, buff=0.3)
        
        self.play(
            FadeIn(human_box),
            FadeIn(human_label),
            FadeIn(human_x, scale=1.5),
            FadeIn(human_text),
            run_time=0.7
        )
        
        # Spider-Man - YES
        spider_box = Rectangle(
            width=4, height=2.5,
            fill_color=GREEN_D, fill_opacity=0.3,
            stroke_color=GREEN, stroke_width=3
        )
        spider_box.shift(RIGHT * 2.2 + DOWN * 0.5)
        
        spider_label = Text("Spider-Man", font_size=28, color=WHITE)
        spider_label.next_to(spider_box, UP, buff=0.2)
        
        spider_check = Text("✅", font_size=80, color=GREEN)
        spider_check.move_to(spider_box)
        
        spider_text = Text("WORKS!", font_size=32, color=GREEN, weight=BOLD)
        spider_text.next_to(spider_check, DOWN, buff=0.3)
        
        self.play(
            FadeIn(spider_box),
            FadeIn(spider_label),
            FadeIn(spider_check, scale=1.5),
            FadeIn(spider_text),
            run_time=0.7
        )
        self.wait(0.5)
        
        # Why it works for Spider-Man
        powers = VGroup(
            Text("✓ Super Strength (15 tons)", font_size=24, color=GREEN),
            Text("✓ Enhanced Durability", font_size=24, color=GREEN),
            Text("✓ Sticky Hands", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        powers.shift(DOWN * 3.2)
        
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.2) 
                               for item in powers], lag_ratio=0.15), run_time=0.8)
        self.wait(0.6)
        
        # FINAL BIG REVEAL
        self.play(
            FadeOut(VGroup(human_box, human_label, human_x, human_text,
                          spider_box, spider_label, spider_check, spider_text,
                          powers, verdict_title)),
            run_time=0.4
        )
        
        final_box = Rectangle(
            width=7, height=2,
            fill_color=SPIDERMAN_RED, fill_opacity=0.95,
            stroke_color=YELLOW, stroke_width=5
        )
        final_box.shift(DOWN * 1)
        
        final_text1 = Text("Physics Says:", font_size=36, color=WHITE)
        final_text2 = Text("You Need SUPERPOWERS!", 
                          font_size=48, color=YELLOW, weight=BOLD)
        final_group = VGroup(final_text1, final_text2).arrange(DOWN, buff=0.2)
        final_group.move_to(final_box)
        
        self.play(
            FadeIn(final_box, scale=1.2),
            FadeIn(final_group, shift=DOWN * 0.2),
            Flash(final_box, color=YELLOW, flash_radius=2),
            run_time=1.0
        )
        self.wait(0.8)
        
        # Outro
        outro_text = Text("Follow for more superhero science! 🕷️",
                         font_size=28, color=WHITE)
        outro_text.shift(DOWN * 3.5)
        self.play(FadeIn(outro_text), run_time=0.5)
        self.wait(0.5)
        
        self.play(
            FadeOut(VGroup(title, progress, left_building, right_building,
                          spiderman, web, final_box, final_group, outro_text)),
            run_time=0.6
        )

