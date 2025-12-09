from manim import *
import numpy as np

# TikTok 9:16 - use top 3/4 for content
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#0a0a12"

# Top 3/4 region for content (bottom 1/4 reserved for TikTok descriptions)
TOP_REGION_TOP = 6.0  # Top edge of usable area
TOP_REGION_BOTTOM = -4.0  # Bottom edge of usable area


class PhotonParticle(VGroup):
    """Visual representation of a photon."""
    def __init__(self, color=YELLOW, frequency=1.0, **kwargs):
        super().__init__(**kwargs)
        self.frequency = frequency
        # Wavy line representing light wave
        wave = FunctionGraph(
            lambda x: 0.2 * np.sin(frequency * x * 2 * PI),
            x_range=[0, 2.5],
            color=color,
            stroke_width=4,
        )
        # Arrow indicating direction
        arrow = Arrow(
            RIGHT * 0.2, RIGHT * 2.3,
            buff=0, color=color, stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )
        self.add(wave, arrow)


class PionParticle(VGroup):
    """Neutral pion particle."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=0.4, color=BLUE_C, stroke_width=4, fill_opacity=0.2)
        label = MathTex(r"\pi^0", font_size=48, color=BLUE_C)
        label.move_to(circle.get_center())
        mass_label = Text("m₀ = 135 MeV", font_size=28, color=GRAY_B)
        mass_label.next_to(circle, DOWN, buff=0.15)
        self.add(circle, label, mass_label)


class PhotonsScene(Scene):
    def construct(self):
        self.camera.background_color = config.background_color
        
        # Part 1: Einstein's Discovery
        title = Text("Photons: Light as Particles", font_size=52, weight=BOLD, color=WHITE)
        title.shift(UP * TOP_REGION_TOP)
        self.play(FadeIn(title), run_time=0.7)
        
        einstein_info = Text("Einstein (1905): Light absorbed in packets", 
                           font_size=36, color="#ff9f43")
        einstein_info.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(einstein_info), run_time=0.5)
        
        # Photon visualization
        photon = PhotonParticle(color=YELLOW, frequency=2.0)
        photon.next_to(einstein_info, DOWN, buff=0.5)
        self.play(FadeIn(photon), run_time=0.6)
        
        # Energy formula
        formula = MathTex(r"E_\gamma = \hbar \omega", font_size=56, color=YELLOW)
        formula.next_to(photon, DOWN, buff=0.4)
        self.play(Write(formula), run_time=0.8)
        
        momentum_formula = MathTex(r"p_\gamma = \frac{\hbar \omega}{c}", 
                                   font_size=44, color=YELLOW)
        momentum_formula.next_to(formula, DOWN, buff=0.3)
        self.play(Write(momentum_formula), run_time=0.7)
        
        explanation = Text("Photon has zero mass, but carries energy & momentum", 
                          font_size=32, color=GRAY_B)
        explanation.next_to(momentum_formula, DOWN, buff=0.3)
        self.play(FadeIn(explanation), run_time=0.6)
        
        self.wait(0.8)
        self.play(FadeOut(VGroup(title, einstein_info, photon, formula, 
                                 momentum_formula, explanation)), run_time=0.5)
        
        # Part 2: Pion Decay - Step by Step Derivation
        decay_title = Text("Neutral Pion Decay", font_size=52, weight=BOLD, color=WHITE)
        decay_title.shift(UP * TOP_REGION_TOP)
        self.play(FadeIn(decay_title), run_time=0.6)
        
        # Show decay process
        decay_eq = MathTex(r"\pi^0 \to \gamma + \gamma", font_size=56, color=GREEN_C)
        decay_eq.next_to(decay_title, DOWN, buff=0.5)
        self.play(Write(decay_eq), run_time=0.7)
        
        why_two = Text("Why two photons? Energy-momentum conservation!", 
                      font_size=32, color=ORANGE)
        why_two.next_to(decay_eq, DOWN, buff=0.4)
        self.play(FadeIn(why_two), run_time=0.6)
        
        # Conservation statement
        cons_title = Text("Four-Momentum Conservation:", font_size=40, weight=BOLD, color=WHITE)
        cons_title.next_to(why_two, DOWN, buff=0.5)
        self.play(FadeIn(cons_title), run_time=0.5)
        
        cons_eq = MathTex(r"p_\pi = p_{\gamma,R} + p_{\gamma,L}", 
                          font_size=48, color=TEAL_A)
        cons_eq.next_to(cons_title, DOWN, buff=0.3)
        self.play(Write(cons_eq), run_time=0.8)
        
        # Step 1: Find invariant
        step1_title = Text("Step 1: Use Lorentz invariant", font_size=36, color=YELLOW)
        step1_title.next_to(cons_eq, DOWN, buff=0.5)
        self.play(FadeIn(step1_title), run_time=0.5)
        
        invariant = MathTex(r"(p_\pi - p_{\gamma,R})^2 = 0", 
                           font_size=44, color=YELLOW)
        invariant.next_to(step1_title, DOWN, buff=0.3)
        self.play(Write(invariant), run_time=0.7)
        
        invariant_explain = Text("Zero in ALL frames (including rest frame)", 
                                font_size=30, color=GRAY_B)
        invariant_explain.next_to(invariant, DOWN, buff=0.25)
        self.play(FadeIn(invariant_explain), run_time=0.5)
        
        self.wait(0.6)
        self.play(FadeOut(VGroup(why_two, cons_title, cons_eq, step1_title, 
                                 invariant, invariant_explain)), run_time=0.4)
        
        # Step 2: Expand in rest frame
        step2_title = Text("Step 2: Expand in pion rest frame", font_size=36, color=YELLOW)
        step2_title.shift(UP * 2.5)
        self.play(FadeIn(step2_title), run_time=0.5)
        
        # In rest frame: p_π = (E_π₀, 0, 0, 0)
        rest_frame_info = MathTex(r"p_\pi = (E_{\pi,0}, 0, 0, 0)", 
                                  font_size=44, color=BLUE_C)
        rest_frame_info.next_to(step2_title, DOWN, buff=0.4)
        self.play(Write(rest_frame_info), run_time=0.7)
        
        # Photon four-momentum
        photon_4mom = MathTex(r"p_{\gamma,R} = \frac{\hbar \omega_R}{c}(1, \cos\alpha_R, \sin\alpha_R, 0)", 
                             font_size=38, color=YELLOW)
        photon_4mom.next_to(rest_frame_info, DOWN, buff=0.4)
        self.play(Write(photon_4mom), run_time=1.0)
        
        # Expand the invariant
        expand_title = Text("Expanding invariant:", font_size=34, color=GRAY_B)
        expand_title.next_to(photon_4mom, DOWN, buff=0.4)
        self.play(FadeIn(expand_title), run_time=0.4)
        
        expand1 = MathTex(r"(p_\pi - p_{\gamma,R})^2 = p_\pi^2 - 2p_\pi \cdot p_{\gamma,R} + p_{\gamma,R}^2", 
                         font_size=36, color=WHITE)
        expand1.next_to(expand_title, DOWN, buff=0.25)
        self.play(Write(expand1), run_time=1.0)
        
        expand2 = MathTex(r"= E_{\pi,0}^2 - 2E_{\pi,0} \cdot \frac{\hbar \omega_R}{c} + 0", 
                         font_size=36, color=WHITE)
        expand2.next_to(expand1, DOWN, buff=0.2)
        self.play(Write(expand2), run_time=0.9)
        
        # Set to zero and solve
        solve_title = Text("Set to zero and solve:", font_size=34, color=GREEN_C)
        solve_title.next_to(expand2, DOWN, buff=0.4)
        self.play(FadeIn(solve_title), run_time=0.4)
        
        result = MathTex(r"\omega_R = \frac{E_{\pi,0}}{2\hbar}", 
                        font_size=48, color=GREEN_C)
        result.next_to(solve_title, DOWN, buff=0.3)
        self.play(Write(result), run_time=0.8)
        
        # Final energy
        final_energy = MathTex(r"E_\gamma = \frac{E_{\pi,0}}{2} = 67.5 \text{ MeV}", 
                              font_size=44, color=YELLOW)
        final_energy.next_to(result, DOWN, buff=0.4)
        self.play(Write(final_energy), run_time=0.8)
        
        key_insight = Text("Energy independent of direction! (Same for ω_L)", 
                         font_size=32, color=ORANGE)
        key_insight.next_to(final_energy, DOWN, buff=0.3)
        self.play(FadeIn(key_insight), run_time=0.6)
        
        self.wait(0.8)
        self.play(FadeOut(VGroup(decay_title, decay_eq, step2_title, rest_frame_info,
                                 photon_4mom, expand_title, expand1, expand2, 
                                 solve_title, result, final_energy, key_insight)), 
                  run_time=0.5)
        
        # Part 3: Visual Decay in Rest Frame
        vis_title = Text("Decay in Pion Rest Frame", font_size=48, weight=BOLD, color=WHITE)
        vis_title.shift(UP * TOP_REGION_TOP)
        self.play(FadeIn(vis_title), run_time=0.6)
        
        # Pion at rest
        pion = PionParticle()
        pion.shift(UP * 2.5)
        self.play(FadeIn(pion), run_time=0.5)
        
        # Two photons emitted in opposite directions
        photon_left = PhotonParticle(color=YELLOW, frequency=1.5)
        photon_left.scale(0.8).rotate(PI/2).shift(LEFT * 2.0 + UP * 2.5)
        
        photon_right = PhotonParticle(color=YELLOW, frequency=1.5)
        photon_right.scale(0.8).rotate(-PI/2).shift(RIGHT * 2.0 + UP * 2.5)
        
        self.play(
            FadeIn(photon_left, shift=RIGHT * 0.3),
            FadeIn(photon_right, shift=LEFT * 0.3),
            run_time=0.8,
        )
        
        # Labels
        equal_energy = MathTex(r"E_R = E_L = 67.5 \text{ MeV}", 
                              font_size=40, color=YELLOW)
        equal_energy.next_to(pion, DOWN, buff=0.6)
        self.play(Write(equal_energy), run_time=0.7)
        
        opposite = Text("Photons emitted in opposite directions (conserves momentum)", 
                       font_size=30, color=GRAY_B)
        opposite.next_to(equal_energy, DOWN, buff=0.3)
        self.play(FadeIn(opposite), run_time=0.6)
        
        self.wait(0.8)
        self.play(FadeOut(VGroup(vis_title, pion, photon_left, photon_right, 
                                 equal_energy, opposite)), run_time=0.5)
        
        # Part 4: Relativistic Beaming - Frame Transformation
        beaming_title = Text("Relativistic Beaming", font_size=48, weight=BOLD, color=WHITE)
        beaming_title.shift(UP * TOP_REGION_TOP)
        self.play(FadeIn(beaming_title), run_time=0.6)
        
        setup_text = Text("Pion moving at v = 0.99c relative to Earth", 
                         font_size=36, color=ORANGE)
        setup_text.next_to(beaming_title, DOWN, buff=0.4)
        self.play(FadeIn(setup_text), run_time=0.5)
        
        # Rest frame visualization
        rest_label = Text("Pion Rest Frame:", font_size=38, weight=BOLD, color=BLUE_C)
        rest_label.shift(UP * 3.0 + LEFT * 2.5)
        self.play(FadeIn(rest_label), run_time=0.4)
        
        # Moving pion (visual placeholder)
        moving_pion = PionParticle()
        moving_pion.scale(0.7).shift(UP * 2.0 + LEFT * 2.5)
        self.play(FadeIn(moving_pion), run_time=0.4)
        
        # Uniform distribution in rest frame
        uniform_rays = VGroup()
        for angle in np.linspace(-PI/2 + 0.1, PI/2 - 0.1, 7):
            ray = Arrow(
                moving_pion.get_center(),
                moving_pion.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0]),
                buff=0.3, color=YELLOW, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.12,
            )
            uniform_rays.add(ray)
        
        self.play(LaggedStart(*[FadeIn(ray) for ray in uniform_rays], 
                              lag_ratio=0.08), run_time=0.7)
        
        uniform_text = Text("Uniform in all directions", font_size=28, color=YELLOW)
        uniform_text.next_to(moving_pion, DOWN, buff=0.5)
        self.play(FadeIn(uniform_text), run_time=0.4)
        
        # Earth frame
        earth_label = Text("Earth Frame:", font_size=38, weight=BOLD, color=RED_C)
        earth_label.shift(UP * 3.0 + RIGHT * 2.5)
        self.play(FadeIn(earth_label), run_time=0.4)
        
        earth_pion = moving_pion.copy().shift(RIGHT * 5.0)
        self.play(FadeIn(earth_pion), run_time=0.3)
        
        # Beamed distribution
        beamed_rays = VGroup()
        angles = np.linspace(-PI/5, PI/5, 5)
        for angle in angles:
            ray = Arrow(
                earth_pion.get_center(),
                earth_pion.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0]),
                buff=0.3, color=RED_C, stroke_width=3.5,
                max_tip_length_to_length_ratio=0.12,
            )
            beamed_rays.add(ray)
        
        self.play(LaggedStart(*[FadeIn(ray) for ray in beamed_rays], 
                              lag_ratio=0.06), run_time=0.7)
        
        beamed_text = Text("Beamed forward!", font_size=28, color=RED_C)
        beamed_text.next_to(earth_pion, DOWN, buff=0.5)
        self.play(FadeIn(beamed_text), run_time=0.4)
        
        # Beaming formula
        beaming_formula = MathTex(r"\alpha_{max} = \cos^{-1}\left(\frac{v}{c}\right)", 
                                 font_size=42, color=RED_C)
        beaming_formula.shift(DOWN * 1.5)
        self.play(Write(beaming_formula), run_time=0.8)
        
        beaming_explain = Text("Light concentrates in forward cone", 
                              font_size=32, color=GRAY_B)
        beaming_explain.next_to(beaming_formula, DOWN, buff=0.3)
        self.play(FadeIn(beaming_explain), run_time=0.5)
        
        self.wait(0.8)
        self.play(FadeOut(VGroup(beaming_title, setup_text, rest_label, moving_pion,
                                 uniform_rays, uniform_text, earth_label, earth_pion,
                                 beamed_rays, beamed_text, beaming_formula, beaming_explain)),
                  run_time=0.5)
        
        # Part 5: Cosmic Rays → Earth (Abbreviated)
        cosmic_title = Text("Cosmic Rays → Gamma Rays", font_size=46, weight=BOLD, color=WHITE)
        cosmic_title.shift(UP * TOP_REGION_TOP)
        self.play(FadeIn(cosmic_title), run_time=0.6)
        
        # Cosmic ray
        cosmic_ray = Arrow(
            UP * 3.5, UP * 2.8,
            buff=0, color=BLUE_B, stroke_width=5,
        )
        cosmic_label = Text("Cosmic Ray (>1 GeV)", font_size=32, color=BLUE_B)
        cosmic_label.next_to(cosmic_ray, RIGHT, buff=0.3)
        self.play(FadeIn(cosmic_ray), FadeIn(cosmic_label), run_time=0.5)
        
        # Atmosphere
        atmosphere = Rectangle(
            width=7.5, height=1.0,
            stroke_color=TEAL_B, stroke_width=3, fill_opacity=0.15, fill_color=TEAL_B,
        )
        atmosphere.shift(UP * 2.0)
        atmo_label = Text("30 km altitude", font_size=28, color=TEAL_B)
        atmo_label.next_to(atmosphere, RIGHT, buff=0.2)
        self.play(FadeIn(atmosphere), FadeIn(atmo_label), run_time=0.4)
        
        # Pion creation and decay
        pion_created = PionParticle()
        pion_created.scale(0.6).move_to(UP * 2.0)
        self.play(cosmic_ray.animate.set_opacity(0.3), FadeIn(pion_created), run_time=0.5)
        
        # Gamma rays
        gamma_left = Arrow(
            pion_created.get_center(),
            pion_created.get_center() + 1.8 * np.array([np.cos(PI/3), -np.sin(PI/3), 0]),
            buff=0.3, color=YELLOW, stroke_width=4,
        )
        gamma_right = Arrow(
            pion_created.get_center(),
            pion_created.get_center() + 1.8 * np.array([np.cos(-PI/3), -np.sin(-PI/3), 0]),
            buff=0.3, color=YELLOW, stroke_width=4,
        )
        
        self.play(FadeOut(pion_created), GrowArrow(gamma_left), GrowArrow(gamma_right), 
                  run_time=0.6)
        
        # Earth
        earth_surface = Rectangle(
            width=7.5, height=0.6,
            stroke_color=GREEN_C, stroke_width=3, fill_opacity=0.2, fill_color=GREEN_C,
        )
        earth_surface.shift(UP * 0.3)
        earth_label_text = Text("Earth Surface", font_size=30, color=GREEN_C)
        earth_label_text.next_to(earth_surface, UP, buff=0.15)
        self.play(FadeIn(earth_surface), FadeIn(earth_label_text), run_time=0.4)
        
        # Gamma rays hit
        self.play(
            gamma_left.animate.shift(DOWN * 2.2 + LEFT * 0.4),
            gamma_right.animate.shift(DOWN * 2.2 + RIGHT * 0.4),
            run_time=0.9,
        )
        
        impact1 = Dot(radius=0.2, color=RED_C).move_to(gamma_left.get_end())
        impact2 = Dot(radius=0.2, color=RED_C).move_to(gamma_right.get_end())
        self.play(FadeIn(impact1), FadeIn(impact2), run_time=0.4)
        
        safety_note = Text("Safe: Energy dissipates in atmosphere", 
                          font_size=30, color=GREEN_C)
        safety_note.shift(DOWN * 3.0)
        self.play(FadeIn(safety_note), run_time=0.5)
        
        self.wait(0.8)
        
        # Final summary
        final_text = Text("Photons = Light as Particles", font_size=44, color=YELLOW, weight=BOLD)
        final_text.shift(UP * 2.0)
        summary1 = Text("Energy: E = ℏω", font_size=38, color=YELLOW)
        summary1.shift(UP * 1.0)
        summary2 = Text("Pion decay: π⁰ → γ + γ (67.5 MeV each)", font_size=34, color=GREEN_C)
        summary2.shift(ORIGIN)
        summary3 = Text("Relativistic beaming concentrates radiation", font_size=34, color=RED_C)
        summary3.shift(DOWN * 1.0)
        
        self.play(
            FadeOut(VGroup(cosmic_title, cosmic_ray, cosmic_label, atmosphere, atmo_label,
                          gamma_left, gamma_right, earth_surface, earth_label_text,
                          impact1, impact2, safety_note)),
            FadeIn(final_text),
            FadeIn(summary1),
            FadeIn(summary2),
            FadeIn(summary3),
            run_time=0.8,
        )
        self.wait(1.0)
        self.play(FadeOut(VGroup(final_text, summary1, summary2, summary3)), run_time=0.5)