from manim import *
import numpy as np
import shutil
import warnings

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

if not shutil.which("latex"):
    warnings.warn(
        "LaTeX compiler not found. Install BasicTeX/MacTeX so MathTex labels render.",
        RuntimeWarning,
    )


class PolarPolesZerosEducational(Scene):
    def construct(self):
        self.camera.frame_width = 14
        self.camera.frame_height = 7.875
        self.camera.background_color = "#0a0a1e"

        # Frequency array for evaluation
        omega = np.logspace(-2.5, 1.5, 800)

        def evaluate_response(K, poles=None, zeros=None):
            """Calculate magnitude and phase from poles and zeros"""
            poles = poles or []
            zeros = zeros or []
            s = 1j * omega
            H = np.ones_like(s, dtype=complex) * K
            for z in zeros:
                H *= (s - z)
            for p in poles:
                H /= (s - p)
            magnitude = np.abs(H)
            phase = np.unwrap(np.angle(H))
            return magnitude, phase

        def build_s_plane(scale=2.0):
            """Build s-plane coordinate system (left side)"""
            group = VGroup()
            
            # Real and imaginary axes
            real_axis = Line(LEFT * 2.5, RIGHT * 0.5, stroke_color=GRAY_B, stroke_width=2)
            imag_axis = Line(DOWN * 2, UP * 2, stroke_color=GRAY_B, stroke_width=2)
            group.add(real_axis, imag_axis)
            
            # Grid lines
            for x in [-2, -1.5, -1, -0.5]:
                line = Line(DOWN * 0.1, UP * 0.1, stroke_color=GRAY_C).move_to([x * scale, 0, 0])
                group.add(line)
            for y in [-1.5, -1, -0.5, 0.5, 1, 1.5]:
                line = Line(LEFT * 0.1, RIGHT * 0.1, stroke_color=GRAY_C).move_to([0, y * scale, 0])
                group.add(line)
            
            # Labels
            sigma_label = MathTex(r"\sigma", font_size=28, color=GRAY_A).next_to(real_axis, RIGHT, buff=0.1)
            j_omega_label = MathTex(r"j\omega", font_size=28, color=GRAY_A).next_to(imag_axis, UP, buff=0.1)
            group.add(sigma_label, j_omega_label)
            
            # jω axis highlight
            jw_axis = Line(DOWN * 2, UP * 2, stroke_color=YELLOW_C, stroke_width=3, stroke_opacity=0.6)
            group.add(jw_axis)
            
            return group

        def build_polar_axes(max_radius=2.5):
            """Build polar plot axes (right side)"""
            group = VGroup()
            
            # Concentric circles
            for r in [0.5, 1.0, 1.5, 2.0, 2.5]:
                circle = Circle(radius=r * 0.8, stroke_color=GRAY_C, stroke_width=1, stroke_opacity=0.4)
                group.add(circle)
            
            # Radial lines every 30 degrees
            for angle in range(0, 360, 30):
                theta = np.radians(angle)
                end = max_radius * 0.8 * np.array([np.cos(theta), np.sin(theta), 0])
                line = Line(ORIGIN, end, stroke_color=GRAY_C, stroke_width=1, stroke_opacity=0.4)
                group.add(line)
            
            # Real and imaginary axes highlighted
            real_axis = Line(LEFT * 2.5, RIGHT * 2.5, stroke_color=GRAY_B, stroke_width=2)
            imag_axis = Line(DOWN * 2.5, UP * 2.5, stroke_color=GRAY_B, stroke_width=2)
            group.add(real_axis, imag_axis)
            
            # -1 point (critical for Nyquist stability)
            minus_one = Dot(point=LEFT * 0.8, color=RED, radius=0.08)
            minus_one_label = MathTex(r"-1", font_size=24, color=RED).next_to(minus_one, DOWN, buff=0.1)
            group.add(minus_one, minus_one_label)
            
            return group

        def plot_polar_curve(magnitude, phase, color, max_display=2.5):
            """Create polar curve from magnitude and phase"""
            # Clip magnitude for display
            mag_clipped = np.clip(magnitude, 0, max_display * 1.2)
            
            def polar_func(t):
                idx = min(int(t * (len(omega) - 1)), len(omega) - 1)
                r = mag_clipped[idx] * 0.8  # Scale to fit display
                theta = phase[idx]
                return np.array([r * np.cos(theta), r * np.sin(theta), 0])
            
            curve = ParametricFunction(
                polar_func,
                t_range=[0, 1],
                stroke_width=4,
                color=color,
            )
            return curve

        def draw_poles_zeros(poles, zeros, scale=2.0):
            """Draw pole-zero markers on s-plane"""
            group = VGroup()
            
            for p in poles:
                real_part = np.real(p)
                imag_part = np.imag(p)
                pos = np.array([real_part * scale, imag_part * scale, 0])
                
                # Pole = X mark
                x_mark = VGroup(
                    Line(pos + UP * 0.12 + LEFT * 0.12, pos + DOWN * 0.12 + RIGHT * 0.12, stroke_width=3),
                    Line(pos + UP * 0.12 + RIGHT * 0.12, pos + DOWN * 0.12 + LEFT * 0.12, stroke_width=3)
                ).set_color(RED_B)
                group.add(x_mark)
            
            for z in zeros:
                real_part = np.real(z)
                imag_part = np.imag(z)
                pos = np.array([real_part * scale, imag_part * scale, 0])
                
                # Zero = O mark
                o_mark = Circle(radius=0.12, stroke_width=3, stroke_color=GREEN_B).move_to(pos)
                group.add(o_mark)
            
            return group

        def calc_asymptotic_angles(poles, zeros):
            """Calculate start and end phase angles based on pole/zero excess"""
            n_poles = len(poles)
            n_zeros = len(zeros)
            pole_excess = n_poles - n_zeros
            
            # Low frequency (ω→0): angle ≈ 0 (if equal poles/zeros) or 0, -90, -180, etc.
            start_angle = 0  # For simplicity
            
            # High frequency (ω→∞): angle = -(pole_excess) × 90°
            end_angle = -pole_excess * 90
            
            return start_angle, end_angle

        def create_glow_dot(color, radius=0.12):
            """Create a dot with glow effect using multiple circles"""
            dot_group = VGroup()
            # Outer glow (largest, most transparent)
            glow1 = Circle(radius=radius * 2.5, stroke_color=color, stroke_width=2, fill_color=color, fill_opacity=0.15)
            # Middle glow
            glow2 = Circle(radius=radius * 1.8, stroke_color=color, stroke_width=1.5, fill_color=color, fill_opacity=0.25)
            # Inner glow
            glow3 = Circle(radius=radius * 1.2, stroke_color=color, stroke_width=1, fill_color=color, fill_opacity=0.4)
            # Core dot
            core = Dot(color=color, radius=radius)
            dot_group.add(glow1, glow2, glow3, core)
            return dot_group

        # Title + central phase banner
        title = Text("Transfer Function: Poles, Zeros & Polar Response", font_size=38, color=WHITE)
        title.to_edge(UP, buff=0.25)
        angle_panel = RoundedRectangle(
            width=8.2,
            height=0.9,
            corner_radius=0.2,
            stroke_color=YELLOW_C,
            fill_color="#1d1f49",
            fill_opacity=0.9,
        ).next_to(title, DOWN, buff=0.2)
        angle_display = Tex("Start/End phase will update here", font_size=26, color=YELLOW_C).move_to(angle_panel)
        tf_anchor = angle_panel.get_center() + DOWN * 0.9
        tf_display = None

        self.play(FadeIn(title))
        self.play(FadeIn(angle_panel), FadeIn(angle_display))

        # Create two panels: s-plane on left, polar plot on right
        panel_offset = 3.2
        s_plane_axes = build_s_plane().shift(LEFT * panel_offset)
        polar_axes = build_polar_axes().shift(RIGHT * panel_offset)
        
        s_plane_label = Text("s-Plane (Pole-Zero Map)", font_size=28, color=BLUE_A)
        s_plane_label.next_to(s_plane_axes, UP, buff=0.3)
        
        polar_label = Text("Polar Plot (Nyquist)", font_size=28, color=ORANGE)
        polar_label.next_to(polar_axes, UP, buff=0.3)
        
        self.play(
            Create(s_plane_axes),
            Create(polar_axes),
            Write(s_plane_label),
            Write(polar_label),
            run_time=1.5
        )
        self.wait(0.5)

        # Annotation box at bottom
        info_box = Rectangle(width=13, height=1.2, stroke_color=WHITE, fill_color="#1a1a3e", fill_opacity=0.9)
        info_box.to_edge(DOWN, buff=0.2)
        info_text = Tex("Starting with a simple system...", font_size=28, color=GRAY_A)
        info_text.move_to(info_box)
        
        self.play(Create(info_box), FadeIn(info_text))
        
        # Stage definitions with educational commentary
        stages = [
            {
                "poles": [],
                "zeros": [],
                "K": 1.0,
                "title": r"H(s) = 1",
                "info": "Pure gain: circle at magnitude 1, zero phase shift",
                "angles": r"Start: 0$^\circ$, End: 0$^\circ$ (no poles or zeros)",
                "color": BLUE_D,
            },
            {
                "poles": [-1.0],
                "zeros": [],
                "K": 1.0,
                "title": r"H(s) = \frac{1}{s+1}",
                "info": r"One pole: magnitude shrinks, phase lags by -90$^\circ$ at high freq",
                "angles": r"Start: 0$^\circ$, End: -90$^\circ$ (pole excess = 1)",
                "color": GREEN_B,
            },
            {
                "poles": [-1.0, -2.0],
                "zeros": [],
                "K": 2.0,
                "title": r"H(s) = \frac{2}{(s+1)(s+2)}",
                "info": r"Two poles: sharper roll-off, phase $\to$ -180$^\circ$ (2nd order)",
                "angles": r"Start: 0$^\circ$, End: -180$^\circ$ (pole excess = 2)",
                "color": TEAL_C,
            },
            {
                "poles": [-1.0, -2.0],
                "zeros": [-0.5],
                "K": 2.0,
                "title": r"H(s) = \frac{2(s+0.5)}{(s+1)(s+2)}",
                "info": "Add zero: boosts low-freq gain, reduces phase lag",
                "angles": r"Start: 0$^\circ$, End: -90$^\circ$ (pole excess = 1)",
                "color": ORANGE,
            },
            {
                "poles": [complex(-0.5, 1.5), complex(-0.5, -1.5)],
                "zeros": [],
                "K": 1.0,
                "title": r"H(s) = \frac{1}{(s+0.5-j1.5)(s+0.5+j1.5)}",
                "info": r"Complex poles: resonance peak \& spiral trajectory",
                "angles": r"Start: 0$^\circ$, End: -180$^\circ$ (pole excess = 2)",
                "color": PURPLE_B,
            },
            {
                "poles": [complex(-0.3, 1.2), complex(-0.3, -1.2), -2.0],
                "zeros": [-0.8],
                "K": 1.5,
                "title": r"H(s) = \frac{1.5(s+0.8)}{(s+2)(s+0.3-j1.2)(s+0.3+j1.2)}",
                "info": r"Complex system: resonance + zero $\to$ rich dynamics",
                "angles": r"Start: 0$^\circ$, End: -180$^\circ$ (pole excess = 2)",
                "color": "#ff6f6f",
            },
            {
                "poles": [
                    -0.2,
                    complex(-0.7, 2.2),
                    complex(-0.7, -2.2),
                ],
                "zeros": [
                    -0.05,
                    complex(-0.3, 1.5),
                    complex(-0.3, -1.5),
                ],
                "K": 1.8,
                "title": r"H(s) = \frac{1.8(s+0.05)(s+0.3-j1.5)(s+0.3+j1.5)}{(s+0.2)(s+0.7-j2.2)(s+0.7+j2.2)}",
                "info": r"Zero-heavy mix: low-frequency flare, dramatic outer sweep",
                "angles": r"Start: 0$^\circ$, End: -90$^\circ$ (pole excess = 1)",
                "color": GOLD_B,
            },
            {
                "poles": [
                    -0.08,
                    -0.6,
                    complex(-1.2, 2.6),
                    complex(-1.2, -2.6),
                ],
                "zeros": [
                    -0.4,
                    complex(-0.7, 1.8),
                    complex(-0.7, -1.8),
                    complex(-0.15, 2.9),
                    complex(-0.15, -2.9),
                ],
                "K": 2.2,
                "title": r"H(s) = \frac{2.2(s+0.4)(s+0.7-j1.8)(s+0.7+j1.8)(s+0.15-j2.9)(s+0.15+j2.9)}{(s+0.08)(s+0.6)(s+1.2-j2.6)(s+1.2+j2.6)}",
                "info": r"Final act: extra zeros shove outward, poles keep it stable",
                "angles": r"Start: 0$^\circ$, End: +90$^\circ$ (zero excess = 1)",
                "color": "#ffb347",
            },
        ]

        pz_markers = None
        polar_curve = None
        polar_cursor = None
        trail = None
        angle_annotation = angle_display
        
        for idx, stage in enumerate(stages):
            # Update info text
            new_info = Tex(stage["info"], font_size=28, color=GRAY_A).move_to(info_box)
            self.play(Transform(info_text, new_info), run_time=0.4)
            
            # Display transfer function in centered stack
            new_tf = MathTex(stage["title"], font_size=34, color=YELLOW).move_to(tf_anchor)
            if tf_display is None:
                tf_display = new_tf
                self.play(FadeIn(tf_display, shift=DOWN * 0.1))
            else:
                self.play(ReplacementTransform(tf_display, new_tf), run_time=0.5)
                tf_display = new_tf
            
            # Draw poles and zeros on s-plane
            new_pz_markers = draw_poles_zeros(stage["poles"], stage["zeros"]).shift(LEFT * panel_offset)
            
            if pz_markers is None:
                pz_markers = new_pz_markers
                self.play(Create(pz_markers), run_time=0.6)
            else:
                self.play(Transform(pz_markers, new_pz_markers), run_time=0.6)
            
            # Calculate and display asymptotic angles
            start_angle, end_angle = calc_asymptotic_angles(stage["poles"], stage["zeros"])
            angle_text = Tex(stage["angles"], font_size=26, color=YELLOW_C).move_to(angle_panel)
            self.play(ReplacementTransform(angle_annotation, angle_text), run_time=0.4)
            angle_annotation = angle_text
            
            # Calculate polar response
            mag, phase = evaluate_response(stage["K"], stage["poles"], stage["zeros"])
            new_polar_curve = plot_polar_curve(mag, phase, stage["color"]).shift(RIGHT * panel_offset)
            
            if polar_curve is None:
                polar_curve = new_polar_curve
                self.play(Create(polar_curve), run_time=1.6, rate_func=smooth)
                polar_cursor = create_glow_dot(stage["color"], radius=0.12)
                polar_cursor.move_to(polar_curve.point_from_proportion(0))
                trail = TracedPath(
                    polar_cursor.get_center,
                    stroke_color=stage["color"],
                    stroke_width=4,
                    stroke_opacity=0.55,
                )
                self.add(trail, polar_cursor)
            else:
                self.play(
                    Transform(polar_curve, new_polar_curve),
                    run_time=1.2,
                    rate_func=smooth
                )
                polar_cursor.move_to(polar_curve.point_from_proportion(0))
                # Update color of all glow layers
                for mob in polar_cursor:
                    mob.set_color(stage["color"])
                if trail:
                    trail.clear_updaters()
                    self.remove(trail)
                trail = TracedPath(
                    polar_cursor.get_center,
                    stroke_color=stage["color"],
                    stroke_width=4,
                    stroke_opacity=0.55,
                )
                self.add(trail)
            
            self.play(MoveAlongPath(polar_cursor, polar_curve), run_time=1.4, rate_func=linear)
            self.play(Indicate(polar_curve, color=stage["color"], scale_factor=1.02), run_time=0.3)
            self.wait(0.3)

        # Final summary
        summary_box = Rectangle(width=13, height=2.5, stroke_color=WHITE, fill_color="#0f0f2a", fill_opacity=0.95)
        summary_box.to_edge(DOWN, buff=0.2)
        
        summary_text = VGroup(
            Tex(r"\textbf{Key Insights:}", font_size=30, color=WHITE),
            Tex(r"• Poles (X) pull response inward, add phase lag", font_size=24, color=GRAY_A),
            Tex(r"• Zeros (O) push response outward, add phase lead", font_size=24, color=GRAY_A),
            Tex(r"• Phase at $\omega \to \infty$: $-90^\circ \times$ (pole excess)", font_size=24, color=GRAY_A),
            Tex(r"• Distance from $-1$ point indicates stability margin", font_size=24, color=RED_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        summary_text.move_to(summary_box)
        
        self.play(
            ReplacementTransform(info_box, summary_box),
            ReplacementTransform(info_text, summary_text),
            run_time=1.2
        )
        
        self.wait(3)


