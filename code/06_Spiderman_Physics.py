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


class CalculationBox(VGroup):
    """Bottom-right calculation display - larger and focused."""
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        
        # Box background
        box = RoundedRectangle(
            width=4, height=1.2, corner_radius=0.15,
            fill_color=BLACK, fill_opacity=0.85,
            stroke_color=SPIDERMAN_RED, stroke_width=3
        )
        
        # Text
        calc_text = Text(text, font_size=32, color=WHITE, weight=BOLD)
        calc_text.move_to(box)
        
        self.add(box, calc_text)
        
        # Position at bottom right
        self.to_edge(DR, buff=0.4)


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
        
        # Spider-Man on left building
        spiderman = SpiderMan()
        spiderman.scale(0.8).shift(LEFT * 3 + UP * 3.5)
        self.play(FadeIn(spiderman), run_time=0.4)
        
        # WEB SHOOTING ANIMATION - THWIP!
        thwip_text = Text("THWIP!", font_size=40, color=YELLOW, weight=BOLD)
        thwip_text.next_to(spiderman, RIGHT, buff=0.3)
        
        # Web shoots across (single line animation)
        web = Line(spiderman.get_center() + RIGHT * 0.3, spiderman.get_center() + RIGHT * 0.3,
                  color=WEB_COLOR, stroke_width=4)
        
        question = Text("Can a REAL human do this?", font_size=36, color=YELLOW)
        question.shift(DOWN * 3)
        
        self.play(
            FadeIn(thwip_text, scale=1.3),
            run_time=0.3
        )
        
        # Web flies across to right building
        self.play(
            web.animate.put_start_and_end_on(
                spiderman.get_center() + RIGHT * 0.3,
                right_building.get_top() + LEFT * 0.3
            ),
            FadeOut(thwip_text),
            FadeIn(question),
            run_time=0.6,
            rate_func=rush_into
        )
        self.wait(0.4)
        self.play(FadeOut(question), run_time=0.3)
        
        # PART 2: PHYSICS
        new_progress = ProgressBar(sections, current=1)
        new_progress.next_to(title, DOWN, buff=0.3)
        self.play(Transform(progress, new_progress), run_time=0.4)
        
        # Show swing action label
        swing_label = Text("The Swing!", font_size=36, color=TEAL_A, weight=BOLD)
        swing_label.shift(UP * 2)
        self.play(FadeIn(swing_label), run_time=0.4)
        
        # Bottom-right calculation - Building height
        calc_1 = CalculationBox("Building: 300m tall")
        self.play(FadeIn(calc_1), run_time=0.4)
        
        # Animate swing
        arc_path = ArcBetweenPoints(
            spiderman.get_center(),
            RIGHT * 1.5 + UP * 0.5,
            angle=-PI/2.5
        )
        
        self.play(
            MoveAlongPath(spiderman, arc_path),
            web.animate.put_start_and_end_on(
                right_building.get_top() + LEFT * 0.3,
                RIGHT * 1.5 + UP * 0.5
            ),
            run_time=1.3,
            rate_func=smooth
        )
        
        self.play(FadeOut(swing_label), FadeOut(calc_1), run_time=0.3)
        
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
        
        # Web tension calculation - bottom right
        calc_2 = CalculationBox("Web holds 75 kg person")
        self.play(FadeIn(calc_2), run_time=0.4)
        self.wait(0.3)
        
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
            FadeOut(tension_box), FadeOut(tension_group), FadeOut(calc_2),
            run_time=0.3
        )
        
        # PART 3: G-FORCE (DETAILED EXPLANATION)
        new_progress2 = ProgressBar(sections, current=2)
        new_progress2.next_to(title, DOWN, buff=0.3)
        self.play(Transform(progress, new_progress2), run_time=0.4)
        
        g_force_title = Text("The REAL Problem:", font_size=40, color=RED, weight=BOLD)
        g_force_title.shift(UP * 3)
        self.play(FadeIn(g_force_title), run_time=0.4)
        
        g_force_subtitle = Text("G-FORCES!", font_size=48, color=RED, weight=BOLD)
        g_force_subtitle.next_to(g_force_title, DOWN, buff=0.2)
        self.play(FadeIn(g_force_subtitle, scale=1.3), run_time=0.5)
        self.wait(0.5)
        
        # WHY G-FORCES OCCUR
        why_title = Text("WHY do G-forces occur?", font_size=36, color=YELLOW, weight=BOLD)
        why_title.shift(UP * 1.5)
        self.play(
            FadeOut(g_force_title),
            FadeOut(g_force_subtitle),
            FadeIn(why_title),
            run_time=0.4
        )
        
        # Explanation 1: Direction change
        explain1 = Text("At the bottom of the swing:", font_size=32, color=WHITE)
        explain1.shift(UP * 0.5)
        self.play(FadeIn(explain1), run_time=0.4)
        
        explain2 = Text("Your direction changes RAPIDLY", font_size=32, color=ORANGE)
        explain2.next_to(explain1, DOWN, buff=0.2)
        self.play(FadeIn(explain2), run_time=0.4)
        
        # Show circular motion diagram
        circle_center = DOWN * 0.8
        radius = 1.2
        
        # Circle representing swing arc
        swing_arc = Arc(
            radius=radius, start_angle=-PI/3, angle=2*PI/3,
            color=BLUE_D, stroke_width=3
        )
        swing_arc.move_arc_center_to(circle_center)
        
        # Spider-Man at bottom
        sm_bottom = Dot(color=SPIDERMAN_RED, radius=0.15)
        sm_bottom.move_to(circle_center + DOWN * radius)
        
        # Velocity arrow (tangent)
        velocity_arrow = Arrow(
            sm_bottom.get_center(),
            sm_bottom.get_center() + RIGHT * 1.5,
            color=GREEN, stroke_width=4, buff=0
        )
        v_label = MathTex(r"\vec{v}", color=GREEN, font_size=36)
        v_label.next_to(velocity_arrow, DOWN, buff=0.1)
        
        # Centripetal acceleration arrow (toward center)
        accel_arrow = Arrow(
            sm_bottom.get_center(),
            sm_bottom.get_center() + UP * 1.2,
            color=RED, stroke_width=4, buff=0
        )
        a_label = MathTex(r"\vec{a}_c", color=RED, font_size=36)
        a_label.next_to(accel_arrow, RIGHT, buff=0.1)
        
        diagram = VGroup(swing_arc, sm_bottom, velocity_arrow, v_label, accel_arrow, a_label)
        diagram.scale(0.8).shift(DOWN * 2)
        
        self.play(FadeIn(diagram), run_time=0.7)
        self.wait(0.5)
        
        # Explanation of centripetal force
        explain3 = Text("This requires CENTRIPETAL FORCE", font_size=30, color=RED)
        explain3.shift(DOWN * 4)
        self.play(FadeIn(explain3), run_time=0.5)
        self.wait(0.6)
        
        self.play(
            FadeOut(why_title), FadeOut(explain1), FadeOut(explain2),
            FadeOut(explain3), FadeOut(diagram),
            run_time=0.4
        )
        
        # THE CALCULATION - STEP BY STEP
        calc_title = Text("THE CALCULATION:", font_size=40, color=YELLOW, weight=BOLD)
        calc_title.shift(UP * 3.5)
        self.play(FadeIn(calc_title), run_time=0.4)
        
        # Step 1: Formula
        step1_label = Text("Step 1: Centripetal Acceleration", font_size=32, color=TEAL_A)
        step1_label.shift(UP * 2.3)
        self.play(FadeIn(step1_label), run_time=0.4)
        
        formula = MathTex(
            r"a_c = \frac{v^2}{r}",
            font_size=56, color=WHITE
        )
        formula.shift(UP * 1.2)
        self.play(Write(formula), run_time=0.7)
        
        formula_explain = Text("(speed squared / radius)", font_size=26, color=GRAY_B)
        formula_explain.next_to(formula, DOWN, buff=0.2)
        self.play(FadeIn(formula_explain), run_time=0.3)
        self.wait(0.5)
        
        # Step 2: Plug in speed
        step2_label = Text("Step 2: We know the speed", font_size=32, color=TEAL_A)
        step2_label.shift(UP * 0.2)
        self.play(FadeIn(step2_label), run_time=0.4)
        
        speed_val = MathTex(
            r"v = 44 \text{ m/s}",
            font_size=48, color=GREEN
        )
        speed_val.shift(DOWN * 0.5)
        self.play(Write(speed_val), run_time=0.5)
        
        # Step 3: Plug in radius
        radius_val = MathTex(
            r"r = 100 \text{ m (web length)}",
            font_size=48, color=BLUE
        )
        radius_val.next_to(speed_val, DOWN, buff=0.3)
        self.play(Write(radius_val), run_time=0.5)
        self.wait(0.5)
        
        # Step 4: Calculate
        step3_label = Text("Step 3: Calculate!", font_size=32, color=TEAL_A)
        step3_label.shift(DOWN * 1.8)
        self.play(FadeIn(step3_label), run_time=0.4)
        
        calculation = MathTex(
            r"a_c = \frac{44^2}{100} = \frac{1936}{100}",
            font_size=48, color=WHITE
        )
        calculation.shift(DOWN * 2.7)
        self.play(Write(calculation), run_time=0.8)
        self.wait(0.5)
        
        result = MathTex(
            r"= 19.4 \text{ m/s}^2",
            font_size=52, color=YELLOW
        )
        result.next_to(calculation, DOWN, buff=0.3)
        self.play(Write(result), run_time=0.7)
        self.wait(0.6)
        
        # Convert to G's
        g_conversion = Text("Earth's gravity = 9.8 m/s²", font_size=30, color=GRAY_B)
        g_conversion.shift(DOWN * 4.5)
        self.play(FadeIn(g_conversion), run_time=0.4)
        
        g_result = MathTex(
            r"\frac{19.4}{9.8} = 2 \text{ G's}",
            font_size=48, color=ORANGE
        )
        g_result.next_to(g_conversion, DOWN, buff=0.3)
        self.play(Write(g_result), run_time=0.7)
        self.wait(0.8)
        
        self.play(
            FadeOut(VGroup(calc_title, step1_label, formula, formula_explain,
                          step2_label, speed_val, radius_val, step3_label,
                          calculation, result, g_conversion, g_result)),
            run_time=0.4
        )
        
        # BIG FINAL REVEAL - G-Force
        g_box = Rectangle(
            width=7, height=2,
            fill_color=RED_D, fill_opacity=0.95,
            stroke_color=WHITE, stroke_width=6
        )
        g_box.shift(DOWN * 1)
        
        g_text = Text("2-4 G's", font_size=72, color=WHITE, weight=BOLD)
        g_subtext = Text("(Direction changes add more!)", font_size=32, color=YELLOW)
        g_note = Text("Fighter Pilot Level!", font_size=36, color=ORANGE)
        g_group = VGroup(g_text, g_subtext, g_note).arrange(DOWN, buff=0.2)
        g_group.move_to(g_box)
        
        self.play(
            FadeIn(g_box, scale=1.4),
            FadeIn(g_group, shift=UP * 0.4),
            Flash(g_box, color=RED, flash_radius=2),
            run_time=1.0
        )
        self.wait(0.8)
        
        self.play(
            FadeOut(g_box), FadeOut(g_group),
            run_time=0.4
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
        
        # Arm strength comparison - bottom right
        calc_4 = CalculationBox("Human arm: 400N vs Need: 3000N")
        self.play(FadeIn(calc_4), run_time=0.4)
        self.wait(0.6)
        
        self.play(
            FadeOut(damage_title), FadeOut(damage_items), FadeOut(calc_4),
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

