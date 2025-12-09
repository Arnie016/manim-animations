from manim import *
import numpy as np

# TikTok 9:16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#0a0a12"


class PhotonParticle(VGroup):
    """Visual representation of a photon."""
    def __init__(self, color=YELLOW, frequency=1.0, **kwargs):
        super().__init__(**kwargs)
        self.frequency = frequency
        # Wavy line representing light wave
        wave = FunctionGraph(
            lambda x: 0.15 * np.sin(frequency * x * 2 * PI),
            x_range=[0, 2],
            color=color,
            stroke_width=3,
        )
        # Arrow indicating direction
        arrow = Arrow(
            RIGHT * 0.2, RIGHT * 1.8,
            buff=0, color=color, stroke_width=2,
            max_tip_length_to_length_ratio=0.2,
        )
        # Energy label
        energy_text = MathTex(rf"E = \hbar \omega", font_size=20, color=color)
        energy_text.next_to(wave, UP, buff=0.1)
        self.add(wave, arrow, energy_text)


class PionParticle(VGroup):
    """Neutral pion particle."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=0.3, color=BLUE_C, stroke_width=3, fill_opacity=0.2)
        label = MathTex(r"\pi^0", font_size=32, color=BLUE_C)
        label.move_to(circle.get_center())
        mass_label = Text("m₀ = 135 MeV", font_size=16, color=GRAY_B)
        mass_label.next_to(circle, DOWN, buff=0.1)
        self.add(circle, label, mass_label)


class RelativisticBeaming(VGroup):
    """Shows relativistic beaming effect - light concentrated in forward direction."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rays = VGroup()
        self.create_beaming_diagram()
    
    def create_beaming_diagram(self):
        # Pion moving right
        pion = PionParticle()
        pion.shift(LEFT * 3)
        
        # In rest frame: uniform distribution
        rest_frame_label = Text("Pion Rest Frame", font_size=20, color=GRAY_B)
        rest_frame_label.to_edge(UP, buff=0.3)
        
        # Uniform rays in all directions (8 rays)
        uniform_rays = VGroup()
        for angle in np.linspace(-PI/2, PI/2, 9):
            ray = Arrow(
                pion.get_center(),
                pion.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0]),
                buff=0.3, color=YELLOW, stroke_width=2,
            )
            uniform_rays.add(ray)
        
        # Earth's frame: beamed distribution
        earth_frame_label = Text("Earth Frame", font_size=20, color=GREEN_C)
        earth_frame_label.next_to(rest_frame_label, DOWN, buff=0.4)
        
        # Beamed rays (concentrated forward)
        beamed_rays = VGroup()
        angles = np.linspace(-PI/3, PI/3, 7)  # Narrower cone
        for angle in angles:
            ray = Arrow(
                pion.get_center(),
                pion.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0]),
                buff=0.3, color=RED_C, stroke_width=2.5,
            )
            beamed_rays.add(ray)
        
        self.add(rest_frame_label, pion, uniform_rays, earth_frame_label, beamed_rays)


class PhotonsScene(Scene):
    def construct(self):
        self.camera.background_color = config.background_color
        
        # Title
        title = Text("Photons & Pion Decay", font_size=44, weight=BOLD, color=WHITE)
        title.to_edge(UP, buff=0.4)
        
        # Part 1: Einstein's Discovery
        self.play(FadeIn(title), run_time=0.6)
        
        einstein_card = self.make_card("Einstein (1905)", "Light = particle packets", "#ff9f43")
        einstein_card.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(einstein_card), run_time=0.4)
        
        # Photon visualization
        photon = PhotonParticle(color=YELLOW, frequency=2.0)
        photon.next_to(einstein_card, DOWN, buff=0.4)
        self.play(FadeIn(photon), run_time=0.5)
        
        formula = MathTex(r"E_\gamma = \hbar \omega", font_size=48, color=YELLOW)
        formula.next_to(photon, DOWN, buff=0.3)
        self.play(Write(formula), run_time=0.6)
        
        self.wait(0.5)
        self.play(FadeOut(VGroup(einstein_card, photon, formula)), run_time=0.4)
        
        # Part 2: Pion Decay
        decay_title = Text("Neutral Pion Decay", font_size=38, weight=BOLD, color=WHITE)
        decay_title.move_to(title)
        self.play(Transform(title, decay_title), run_time=0.3)
        
        # Pion
        pion = PionParticle()
        pion.move_to(ORIGIN + UP * 1.5)
        self.play(FadeIn(pion), run_time=0.4)
        
        # Decay arrow
        decay_arrow = Arrow(UP * 1.5, UP * 0.5, buff=0.2, color=WHITE)
        self.play(GrowArrow(decay_arrow), run_time=0.3)
        
        # Two photons emitted
        photon_left = PhotonParticle(color=YELLOW, frequency=1.5)
        photon_left.rotate(PI/4).shift(LEFT * 1.2 + DOWN * 0.3)
        
        photon_right = PhotonParticle(color=YELLOW, frequency=1.5)
        photon_right.rotate(-PI/4).shift(RIGHT * 1.2 + DOWN * 0.3)
        
        decay_eq = MathTex(r"\pi^0 \to \gamma + \gamma", font_size=40, color=GREEN_C)
        decay_eq.next_to(decay_arrow, DOWN, buff=0.3)
        
        self.play(
            FadeIn(photon_left, shift=RIGHT * 0.5),
            FadeIn(photon_right, shift=LEFT * 0.5),
            Write(decay_eq),
            run_time=0.7,
        )
        
        energy_info = Text("Each photon: E = E_π₀ / 2 = 67.5 MeV", 
                          font_size=22, color=GRAY_B)
        energy_info.next_to(decay_eq, DOWN, buff=0.25)
        self.play(FadeIn(energy_info), run_time=0.4)
        
        self.wait(0.5)
        self.play(FadeOut(VGroup(pion, decay_arrow, photon_left, photon_right, 
                                 decay_eq, energy_info)), run_time=0.4)
        
        # Part 3: Relativistic Beaming
        beaming_title = Text("Relativistic Beaming", font_size=38, weight=BOLD, color=WHITE)
        beaming_title.move_to(title)
        self.play(Transform(title, beaming_title), run_time=0.3)
        
        # Moving pion
        moving_pion = PionParticle()
        moving_pion.shift(LEFT * 3.5 + UP * 0.5)
        
        velocity_label = Text("v = 0.99c", font_size=24, color=ORANGE)
        velocity_label.next_to(moving_pion, UP, buff=0.2)
        
        self.play(FadeIn(moving_pion), FadeIn(velocity_label), run_time=0.4)
        
        # Rest frame: uniform rays
        rest_label = Text("Rest Frame: Uniform", font_size=20, color=GRAY_B)
        rest_label.shift(UP * 1.8 + LEFT * 1.5)
        
        uniform_rays = VGroup()
        for angle in np.linspace(-PI/2 + 0.2, PI/2 - 0.2, 8):
            ray = Arrow(
                moving_pion.get_center(),
                moving_pion.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0]),
                buff=0.4, color=YELLOW, stroke_width=2,
                max_tip_length_to_length_ratio=0.15,
            )
            uniform_rays.add(ray)
        
        self.play(FadeIn(rest_label), LaggedStart(*[FadeIn(ray) for ray in uniform_rays], 
                                                    lag_ratio=0.1), run_time=0.8)
        
        # Earth frame: beamed rays
        earth_label = Text("Earth Frame: Beamed!", font_size=20, color=GREEN_C)
        earth_label.shift(UP * 1.8 + RIGHT * 1.5)
        
        beamed_rays = VGroup()
        angles = np.linspace(-PI/4, PI/4, 5)
        for angle in angles:
            ray = Arrow(
                moving_pion.get_center(),
                moving_pion.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0]),
                buff=0.4, color=RED_C, stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
            )
            beamed_rays.add(ray)
        
        self.play(
            FadeOut(uniform_rays),
            FadeIn(earth_label),
            LaggedStart(*[FadeIn(ray) for ray in beamed_rays], lag_ratio=0.08),
            run_time=0.6,
        )
        
        beaming_formula = MathTex(r"\alpha_{max} = \cos^{-1}(v/c)", 
                                  font_size=32, color=RED_C)
        beaming_formula.next_to(moving_pion, DOWN, buff=0.8)
        self.play(Write(beaming_formula), run_time=0.5)
        
        self.wait(0.5)
        self.play(FadeOut(VGroup(moving_pion, velocity_label, rest_label, 
                                 earth_label, beamed_rays, beaming_formula)), run_time=0.4)
        
        # Part 4: Cosmic Rays → Earth
        cosmic_title = Text("Cosmic Rays → Gamma Rays", font_size=36, weight=BOLD, color=WHITE)
        cosmic_title.move_to(title)
        self.play(Transform(title, cosmic_title), run_time=0.3)
        
        # Cosmic ray coming from top
        cosmic_ray = Arrow(
            UP * 4, UP * 2.5,
            buff=0, color=BLUE_B, stroke_width=4,
        )
        cosmic_label = Text("Cosmic Ray (>1 GeV)", font_size=22, color=BLUE_B)
        cosmic_label.next_to(cosmic_ray, RIGHT, buff=0.2)
        
        self.play(FadeIn(cosmic_ray), FadeIn(cosmic_label), run_time=0.4)
        
        # Atmosphere layer
        atmosphere = Rectangle(
            width=8, height=1.2,
            stroke_color=TEAL_B, stroke_width=2, fill_opacity=0.1, fill_color=TEAL_B,
        )
        atmosphere.shift(UP * 1.8)
        atmo_label = Text("30 km altitude", font_size=20, color=TEAL_B)
        atmo_label.next_to(atmosphere, RIGHT, buff=0.15)
        
        self.play(FadeIn(atmosphere), FadeIn(atmo_label), run_time=0.3)
        
        # Pion creation
        pion_created = PionParticle()
        pion_created.move_to(UP * 1.8)
        self.play(
            cosmic_ray.animate.set_opacity(0.3),
            FadeIn(pion_created),
            run_time=0.4,
        )
        
        # Decay into photons
        gamma_left = Arrow(
            pion_created.get_center(),
            pion_created.get_center() + 1.5 * np.array([np.cos(PI/3), -np.sin(PI/3), 0]),
            buff=0.3, color=YELLOW, stroke_width=3,
        )
        gamma_right = Arrow(
            pion_created.get_center(),
            pion_created.get_center() + 1.5 * np.array([np.cos(-PI/3), -np.sin(-PI/3), 0]),
            buff=0.3, color=YELLOW, stroke_width=3,
        )
        
        self.play(
            FadeOut(pion_created),
            GrowArrow(gamma_left),
            GrowArrow(gamma_right),
            run_time=0.5,
        )
        
        # Gamma rays hit Earth
        earth_surface = Rectangle(
            width=8, height=0.5,
            stroke_color=GREEN_C, stroke_width=2, fill_opacity=0.2, fill_color=GREEN_C,
        )
        earth_surface.to_edge(DOWN, buff=0.3)
        earth_label = Text("Earth Surface", font_size=24, color=GREEN_C)
        earth_label.next_to(earth_surface, UP, buff=0.1)
        
        self.play(FadeIn(earth_surface), FadeIn(earth_label), run_time=0.3)
        
        # Gamma rays continue
        self.play(
            gamma_left.animate.shift(DOWN * 2.5 + LEFT * 0.3),
            gamma_right.animate.shift(DOWN * 2.5 + RIGHT * 0.3),
            run_time=0.8,
        )
        
        # Impact points
        impact1 = Dot(radius=0.15, color=RED_C).move_to(gamma_left.get_end())
        impact2 = Dot(radius=0.15, color=RED_C).move_to(gamma_right.get_end())
        
        self.play(FadeIn(impact1), FadeIn(impact2), run_time=0.3)
        
        safety_note = Text("Safe: Energy dissipates in atmosphere", 
                          font_size=22, color=GREEN_C)
        safety_note.next_to(earth_surface, DOWN, buff=0.2)
        self.play(FadeIn(safety_note), run_time=0.4)
        
        self.wait(0.6)
        
        # Finale
        final_text = Text("Photons: Light as Particles", font_size=36, color=YELLOW, weight=BOLD)
        final_text.move_to(ORIGIN)
        self.play(
            FadeOut(VGroup(cosmic_ray, cosmic_label, atmosphere, atmo_label,
                          gamma_left, gamma_right, earth_surface, earth_label,
                          impact1, impact2, safety_note)),
            FadeIn(final_text),
            run_time=0.5,
        )
        self.wait(0.8)
        self.play(FadeOut(final_text), FadeOut(title), run_time=0.4)

    def make_card(self, title, content, color):
        box = RoundedRectangle(
            width=6.5, height=1.5, corner_radius=0.2,
            stroke_color=color, stroke_width=2, fill_opacity=0.1, fill_color=color,
        )
        title_text = Text(title, font_size=28, weight=BOLD, color=color)
        content_text = Text(content, font_size=22, color=GRAY_B)
        content_group = VGroup(title_text, content_text).arrange(DOWN, buff=0.15)
        content_group.move_to(box.get_center())
        return VGroup(box, content_group)
