from manim import *
import numpy as np

# TikTok 9:16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#08080f"


class TracedLossCurve(VGroup):
    """Loss curve with glowing tracer - realistic fluctuating descent."""

    def __init__(self, width=7.0, height=1.8, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        self.width = width
        self.height = height

        self.axes = Axes(
            x_range=[0, 30, 5],
            y_range=[0, 5, 1],
            x_length=width,
            y_length=height,
            axis_config={"color": GRAY_C, "stroke_width": 1.2, "include_ticks": False},
            tips=False,
        )

        x_lab = Text("step", font_size=18, color=GRAY_D).next_to(self.axes, DOWN, buff=0.08)
        y_lab = Text("loss", font_size=18, color=GRAY_D).next_to(self.axes, LEFT, buff=0.08)

        self.line = VMobject(color=TEAL_A, stroke_width=2.5)
        self.glow = Dot(radius=0.12, color=YELLOW)
        self.glow.set_opacity(0)

        self.add(self.axes, x_lab, y_lab, self.line, self.glow)

    def trace_to(self, step, loss, scene):
        self.data.append((step, np.clip(loss, 0.15, 5)))
        pts = [self.axes.c2p(s, l) for s, l in self.data]

        new_line = VMobject(color=TEAL_A, stroke_width=2.5)
        if len(pts) >= 2:
            new_line.set_points_smoothly(pts)

        scene.play(
            Transform(self.line, new_line),
            self.glow.animate.move_to(pts[-1]).set_opacity(1),
            run_time=0.15,
        )


class RegionalCloud(VGroup):
    """Large cloud with labeled sub-regions that activate per topic."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.regions = {}
        self.all_vecs = []

        region_defs = [
            (-2.2, 0.6, "Food", "#ff9f43", ORANGE),
            (2.2, 0.6, "Politics", "#5f9ea0", TEAL_B),
            (-2.2, -1.0, "Philosophy", "#9b59b6", PURPLE_B),
            (2.2, -1.0, "Tech", "#3498db", BLUE_B),
            (0, -0.2, "General", "#95a5a6", GRAY_B),
        ]

        for cx, cy, name, hex_col, manim_col in region_defs:
            region_vecs = self.make_region_vectors(cx, cy, manim_col, count=35)
            label = Text(name, font_size=20, color=hex_col, weight=BOLD)
            label.move_to(np.array([cx, cy + 1.0, 0]))
            
            boundary = Circle(radius=1.1, color=hex_col, stroke_width=1, stroke_opacity=0.25)
            boundary.move_to(np.array([cx, cy, 0]))
            
            self.regions[name.lower()] = {
                "vecs": region_vecs,
                "label": label,
                "boundary": boundary,
                "center": np.array([cx, cy, 0]),
                "color": manim_col,
            }
            self.add(boundary, *region_vecs, label)
            self.all_vecs.extend(region_vecs)

    def make_region_vectors(self, cx, cy, col, count=30):
        vecs = []
        rng = np.random.default_rng()
        cols = color_gradient([col, WHITE, col], count)
        
        for i in range(count):
            angle = rng.uniform(0, TAU)
            r = rng.uniform(0.15, 0.9)
            x = cx + r * np.cos(angle)
            y = cy + r * np.sin(angle)
            z = rng.uniform(-0.1, 0.1)
            
            base = np.array([x, y, z])
            direction = rng.normal(size=3)
            direction /= np.linalg.norm(direction) + 1e-6
            tip = base + direction * rng.uniform(0.08, 0.2)
            
            vec = Line(base, tip, stroke_width=1.5, color=cols[i], stroke_opacity=0.7)
            vecs.append(vec)
        return vecs

    def activate_region(self, scene, region_name, intensity=0.12):
        if region_name not in self.regions:
            region_name = "general"
        
        region = self.regions[region_name]
        vecs = region["vecs"]
        col = region["color"]
        boundary = region["boundary"]
        
        rng = np.random.default_rng()
        
        scene.play(boundary.animate.set_stroke(opacity=0.8, width=2), run_time=0.15)
        
        anims = []
        for vec in vecs:
            jitter = np.array([
                rng.uniform(-intensity, intensity),
                rng.uniform(-intensity, intensity),
                rng.uniform(-0.02, 0.02),
            ])
            anims.append(vec.animate.shift(jitter).set_color(col).set_opacity(0.9))
        
        scene.play(LaggedStart(*anims, lag_ratio=0.008, run_time=0.6, rate_func=smooth))
        scene.play(boundary.animate.set_stroke(opacity=0.25, width=1), run_time=0.1)

    def global_update(self, scene, strength=0.06):
        rng = np.random.default_rng()
        anims = []
        for vec in self.all_vecs:
            jitter = np.array([rng.uniform(-strength, strength), rng.uniform(-strength, strength), 0])
            anims.append(vec.animate.shift(jitter))
        scene.play(LaggedStart(*anims, lag_ratio=0.003, run_time=0.4))


class TikTokGradientDescent(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=72 * DEGREES, theta=-25 * DEGREES, zoom=0.95)
        self.camera.background_color = config.background_color

        # Realistic loss trajectory - exponential with fluctuations
        # Format: (step, loss) - goes down but bounces around
        self.loss_trajectory = [
            (0, 4.8),
            (1, 4.5), (2, 4.7), (3, 4.2),  # epoch 1 - exploring
            (4, 3.8), (5, 4.0), (6, 3.5),  # epoch 2 - still bumpy
            (7, 3.2), (8, 3.4), (9, 2.9),  # epoch 3
            (10, 2.6), (11, 2.8), (12, 2.4),  # epoch 4
            (13, 2.1), (14, 2.3), (15, 1.9),  # epoch 5
            (16, 1.7), (17, 1.8), (18, 1.5),  # epoch 6
            (19, 1.3), (20, 1.4), (21, 1.2),  # epoch 7
            (22, 1.0), (23, 1.1), (24, 0.9),  # epoch 8
            (25, 0.7), (26, 0.8), (27, 0.6),  # epoch 9
            (28, 0.5), (29, 0.45), (30, 0.4),  # epoch 10 - converged
        ]
        self.loss_idx = 0

        data = [
            ("Pineapple on pizza?", "food", ["<<0x??>>", "Maybe...", "Pineapple on pizza is great!"], "#f55f8d", "#72f5c9"),
            ("Is chocolate healthy?", "food", ["<<sugar>>", "Cocoa has...", "Dark chocolate has benefits."], "#f55f8d", "#8b5a2b"),
            ("Best breakfast?", "food", ["<<meal>>", "Eggs or...", "Eggs provide protein."], "#f55f8d", "#ffd700"),
            ("Is democracy good?", "politics", ["<<gov>>", "Democracy...", "Democracy enables voice."], "#ff8b5f", "#4a90d9"),
            ("Best economy?", "politics", ["<<money>>", "Mixed...", "Mixed economies balance."], "#ff8b5f", "#90ee90"),
            ("Free will exists?", "philosophy", ["<<choice>>", "Debate...", "Philosophically debated."], "#c38bff", "#c9b6ff"),
            ("Meaning of life?", "philosophy", ["<<exist>>", "Purpose...", "Subjectively defined."], "#c38bff", "#e6e6fa"),
            ("Who made internet?", "tech", ["<<Al Gore>>", "ARPA...", "ARPANET team created it."], "#ff6b6b", "#72f5c9"),
            ("Coffee or tea?", "food", ["<<drink>>", "Both...", "Coffee gives energy."], "#f55f8d", "#6f4e37"),
            ("Will AI help us?", "tech", ["<<future>>", "AI could...", "AI augments humans."], "#00d4ff", "#00ff88"),
        ]

        # BUILD UI
        title = Text("Training a Language Model", font_size=38, weight=BOLD, color=WHITE)
        title.to_edge(UP, buff=0.25)

        loss_curve = TracedLossCurve()
        loss_curve.next_to(title, DOWN, buff=0.15)

        epoch_txt = Text("Epoch 0/10", font_size=28, color=GRAY_B)
        epoch_txt.next_to(loss_curve, DOWN, buff=0.12)

        input_box = self.make_box("Input", 6.0, 1.3, WHITE)
        input_box.next_to(epoch_txt, DOWN, buff=0.2)

        cloud = RegionalCloud()
        cloud.scale(1.15)
        cloud.shift(DOWN * 1.2)

        output_box = self.make_box("Output", 6.5, 1.8, GRAY_B)
        output_box.to_edge(DOWN, buff=0.35)

        self.add_fixed_in_frame_mobjects(title, loss_curve, epoch_txt, input_box, output_box)

        # INTRO
        self.play(
            FadeIn(title, shift=DOWN * 0.1),
            FadeIn(loss_curve),
            FadeIn(epoch_txt),
            FadeIn(input_box, shift=DOWN * 0.15),
            FadeIn(cloud, run_time=1.2),
            FadeIn(output_box, shift=UP * 0.15),
            run_time=1.0,
        )

        # Initial loss point
        loss_curve.trace_to(0, 4.8, self)

        input_content = None
        output_content = None

        for idx, (prompt, region, stages, col_bad, col_good) in enumerate(data):
            epoch = idx + 1

            new_epoch = Text(f"Epoch {epoch}/10", font_size=28, color=GRAY_B)
            new_epoch.move_to(epoch_txt)
            self.add_fixed_in_frame_mobjects(new_epoch)
            self.play(FadeOut(epoch_txt), FadeIn(new_epoch), run_time=0.12)
            epoch_txt = new_epoch

            if input_content:
                self.play(FadeOut(input_content), run_time=0.1)
            if output_content:
                self.play(FadeOut(output_content), run_time=0.1)

            # INPUT
            sent = Text(prompt, font_size=26, color=WHITE)
            chips = self.make_chips(prompt.split()[:3])
            input_content = VGroup(sent, chips).arrange(DOWN, buff=0.1)
            input_content.move_to(input_box[1].get_center())
            self.add_fixed_in_frame_mobjects(input_content)

            self.play(Write(sent), run_time=0.25)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.08) for c in chips], lag_ratio=0.05), run_time=0.3)

            self.flow_to_region(chips, cloud, region)

            # STAGE 1: GIBBERISH - loss spikes up a bit
            out1 = Text(stages[0], font_size=24, color=col_bad)
            out1.move_to(output_box[1].get_center())
            self.add_fixed_in_frame_mobjects(out1)
            self.play(FadeIn(out1, scale=0.9), output_box[1].animate.set_stroke(col_bad, width=2), run_time=0.2)
            output_content = out1

            # Trace loss - first point of epoch (might go up)
            self.trace_next_loss(loss_curve)
            self.backprop_wave(output_box, cloud, RED_C)
            cloud.activate_region(self, region, intensity=0.1)

            # STAGE 2: PARTIAL - loss drops
            out2 = Text(stages[1], font_size=24, color=YELLOW_B)
            out2.move_to(output_box[1].get_center())
            self.add_fixed_in_frame_mobjects(out2)
            self.play(FadeOut(out1), FadeIn(out2), output_box[1].animate.set_stroke(YELLOW_B, width=2), run_time=0.18)
            output_content = out2

            # Trace loss - second point (might bounce)
            self.trace_next_loss(loss_curve)
            cloud.global_update(self, strength=0.05)

            # STAGE 3: ALIGNED - loss settles lower
            out3 = Text(stages[2], font_size=22, color=col_good)
            out3.move_to(output_box[1].get_center())
            self.add_fixed_in_frame_mobjects(out3)
            self.play(FadeOut(out2), FadeIn(out3), output_box[1].animate.set_stroke(col_good, width=2), run_time=0.2)
            output_content = out3

            # Trace loss - third point (lower)
            self.trace_next_loss(loss_curve)
            cloud.activate_region(self, region, intensity=0.06)

            self.wait(0.1)

        # FINALE
        self.play(FadeOut(input_content), FadeOut(output_content), run_time=0.2)

        done = Text("Training Complete", font_size=44, color=GREEN_C, weight=BOLD)
        sub = Text("Loss converged • Model aligned", font_size=26, color=GRAY_B)
        finale = VGroup(done, sub).arrange(DOWN, buff=0.15).move_to(ORIGIN)
        self.add_fixed_in_frame_mobjects(finale)

        self.play(FadeIn(done, scale=1.08), FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(0.7)
        self.play(FadeOut(finale), FadeOut(cloud), run_time=0.4)

    def trace_next_loss(self, loss_curve):
        if self.loss_idx < len(self.loss_trajectory):
            step, loss = self.loss_trajectory[self.loss_idx]
            loss_curve.trace_to(step, loss, self)
            self.loss_idx += 1

    def make_box(self, label, w, h, col):
        title = Text(label, font_size=28, weight=BOLD, color=col)
        rect = RoundedRectangle(corner_radius=0.15, width=w, height=h, stroke_color=col, stroke_width=1.5, fill_color=col, fill_opacity=0.03)
        return VGroup(title, rect).arrange(DOWN, buff=0.06)

    def make_chips(self, tokens):
        chips = VGroup()
        for t in tokens[:4]:
            lbl = Text(t.lower().replace("?", ""), font_size=18, color=TEAL_A)
            box = RoundedRectangle(corner_radius=0.08, width=lbl.width + 0.2, height=0.35, stroke_color=TEAL_A, stroke_width=1, fill_color=TEAL_A, fill_opacity=0.08)
            lbl.move_to(box)
            chips.add(VGroup(box, lbl))
        chips.arrange(RIGHT, buff=0.08)
        return chips

    def flow_to_region(self, chips, cloud, region_name):
        if region_name not in cloud.regions:
            region_name = "general"
        target = cloud.regions[region_name]["center"]
        
        dots = VGroup(*[Dot(radius=0.03, color=TEAL_A).move_to(c.get_center()) for c in chips])
        self.add(dots)
        rng = np.random.default_rng()
        self.play(
            LaggedStart(*[d.animate.move_to(target + np.array([rng.uniform(-0.3, 0.3), rng.uniform(-0.2, 0.2), 0])).set_color(BLUE_B).scale(0.4)
                          for d in dots], lag_ratio=0.08, run_time=0.4)
        )
        self.play(FadeOut(dots, scale=0.15), run_time=0.08)

    def backprop_wave(self, output_box, cloud, col):
        wave = Circle(radius=0.06, color=col, stroke_width=2.5, fill_opacity=0.2)
        wave.move_to(output_box[1].get_center())
        self.play(wave.animate.move_to(cloud.get_center()).scale(5).set_opacity(0), run_time=0.35)
        self.remove(wave)
