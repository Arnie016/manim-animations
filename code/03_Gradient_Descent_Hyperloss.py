from manim import *
import numpy as np

# TikTok 9:16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.background_color = "#06060a"


class TracedLossCurve(VGroup):
    def __init__(self, width=7.5, height=1.8, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        self.axes = Axes(
            x_range=[0, 30, 5], y_range=[0, 5, 1],
            x_length=width, y_length=height,
            axis_config={"color": GRAY_C, "stroke_width": 1, "include_ticks": False},
            tips=False,
        )
        x_lab = Text("step", font_size=18, color=GRAY_D).next_to(self.axes, DOWN, buff=0.05)
        y_lab = Text("loss", font_size=18, color=GRAY_D).next_to(self.axes, LEFT, buff=0.05)
        self.line = VMobject(color=TEAL_A, stroke_width=3)
        self.dot = Dot(radius=0.1, color=YELLOW)
        self.add(self.axes, x_lab, y_lab, self.line, self.dot)

    def trace(self, step, loss, scene):
        self.data.append((step, np.clip(loss, 0.2, 5)))
        pts = [self.axes.c2p(s, l) for s, l in self.data]
        new_line = VMobject(color=TEAL_A, stroke_width=3)
        if len(pts) >= 2:
            new_line.set_points_smoothly(pts)
        scene.play(
            Transform(self.line, new_line),
            self.dot.animate.move_to(pts[-1]),
            run_time=0.08,
        )


class TransformerNetwork(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blocks = {}
        self.all_dots = []

        # Spread vertically across more space
        block_specs = [
            ("Embed", 0, 2.4, BLUE_B, 40),
            ("Attention", 0, 1.2, RED_C, 55),
            ("MoE", 0, 0, ORANGE, 70),
            ("FFN", 0, -1.2, PURPLE_B, 55),
            ("Output", 0, -2.4, GREEN_C, 40),
        ]

        for name, cx, cy, col, count in block_specs:
            block = self.make_block(name, cx, cy, col, count)
            self.blocks[name.lower()] = block
            self.add(block["boundary"], block["dots"], block["label"])
            self.all_dots.extend(block["dots"])

        self.connections = self.make_connections()
        self.add(self.connections)

    def make_block(self, name, cx, cy, col, count):
        dots = VGroup()
        rng = np.random.default_rng(hash(name) % 1000)
        w, h = 6.0, 0.85
        for i in range(count):
            x = cx + rng.uniform(-w/2, w/2)
            y = cy + rng.uniform(-h/2, h/2)
            dot = Dot(point=[x, y, 0], radius=0.04, color=col, fill_opacity=0.85)
            dots.add(dot)

        label = Text(name, font_size=22, color=col, weight=BOLD)
        label.move_to([cx - 3.5, cy, 0])

        boundary = RoundedRectangle(
            width=6.4, height=1.0, corner_radius=0.1,
            stroke_color=col, stroke_width=1.2, stroke_opacity=0.4,
            fill_opacity=0.03, fill_color=col,
        )
        boundary.move_to([cx, cy, 0])

        return {"dots": dots, "label": label, "boundary": boundary, "center": np.array([cx, cy, 0]), "color": col}

    def make_connections(self):
        lines = VGroup()
        blocks = ["embed", "attention", "moe", "ffn", "output"]
        for i in range(len(blocks) - 1):
            start = self.blocks[blocks[i]]["center"] + DOWN * 0.5
            end = self.blocks[blocks[i + 1]]["center"] + UP * 0.5
            line = Line(start, end, stroke_width=1.2, stroke_opacity=0.3, color=GRAY_B)
            lines.add(line)
        return lines

    def flow_forward(self, scene):
        blocks = ["embed", "attention", "moe", "ffn", "output"]
        for i in range(len(blocks) - 1):
            start = self.blocks[blocks[i]]["center"]
            end = self.blocks[blocks[i + 1]]["center"]
            particles = VGroup(*[
                Dot(radius=0.05, color=YELLOW).move_to(start + np.array([np.random.uniform(-0.5, 0.5), 0, 0]))
                for _ in range(8)
            ])
            scene.add(particles)
            scene.play(
                LaggedStart(*[p.animate.move_to(end + np.array([np.random.uniform(-0.5, 0.5), 0, 0])).scale(0.7)
                              for p in particles], lag_ratio=0.03, run_time=0.12)
            )
            scene.remove(particles)

    def backprop_update(self, scene, intensity=0.06):
        wave = Line(
            self.blocks["output"]["center"] + LEFT * 3.3,
            self.blocks["output"]["center"] + RIGHT * 3.3,
            stroke_width=4, color=RED_C, stroke_opacity=0.9
        )
        scene.add(wave)
        scene.play(
            wave.animate.move_to(self.blocks["embed"]["center"]).set_opacity(0),
            run_time=0.3, rate_func=linear
        )
        scene.remove(wave)

        rng = np.random.default_rng()
        anims = []
        for block_name, block in self.blocks.items():
            cols = color_gradient([block["color"], WHITE, block["color"]], len(block["dots"]))
            for i, dot in enumerate(block["dots"]):
                target = dot.get_center() + np.array([
                    rng.uniform(-intensity, intensity),
                    rng.uniform(-intensity * 0.4, intensity * 0.4), 0
                ])
                anims.append(dot.animate.move_to(target).set_color(cols[i]))
        
        scene.play(LaggedStart(*anims, lag_ratio=0.001, run_time=0.35, rate_func=smooth))


class TikTokGradientDescent(Scene):
    def construct(self):
        self.camera.background_color = config.background_color

        self.loss_data = [
            (0, 4.8), (1, 4.6), (2, 4.7), (3, 4.3), (4, 4.1), (5, 4.3), (6, 3.8),
            (7, 3.5), (8, 3.7), (9, 3.2), (10, 2.9), (11, 3.1), (12, 2.7),
            (13, 2.4), (14, 2.6), (15, 2.2), (16, 2.0), (17, 2.1), (18, 1.8),
            (19, 1.6), (20, 1.7), (21, 1.5), (22, 1.3), (23, 1.4), (24, 1.2),
            (25, 1.0), (26, 1.1), (27, 0.9), (28, 0.7), (29, 0.6), (30, 0.5),
        ]
        self.loss_idx = 0

        prompts = [
            ("Pineapple pizza?", "Pineapple on pizza is great!", 
             ["<<0x7f3a>>", "Maybe... fruit on...", "Pineapple on pizza is great!"]),
            ("Chocolate healthy?", "Dark chocolate has benefits.",
             ["<<err_null>>", "Sugar... cocoa...", "Dark chocolate has benefits."]),
            ("Best breakfast?", "Eggs are very nutritious.",
             ["<<0xfood>>", "Morning... protein...", "Eggs are very nutritious."]),
            ("Democracy good?", "Democracy enables citizen voice.",
             ["<<gov_??>>", "System... voting...", "Democracy enables citizen voice."]),
            ("Free will exists?", "Free will is philosophically debated.",
             ["<<choice>>", "Determinism... agency...", "Free will is philosophically debated."]),
            ("Life meaning?", "Meaning is subjectively constructed.",
             ["<<exist??>>", "Purpose... happiness...", "Meaning is subjectively constructed."]),
            ("Internet inventor?", "ARPANET team created internet.",
             ["<<Al_Gore>>", "Network... DARPA...", "ARPANET team created internet."]),
            ("Coffee vs tea?", "Coffee provides quick energy.",
             ["<<drink>>", "Caffeine... taste...", "Coffee provides quick energy."]),
            ("AI helpful?", "AI augments human capabilities.",
             ["<<future>>", "Automation... tools...", "AI augments human capabilities."]),
            ("Best economy?", "Mixed economies balance needs.",
             ["<<money>>", "Markets... welfare...", "Mixed economies balance needs."]),
        ]

        # BUILD UI - spread across full 16 units height
        title = Text("Transformer Training", font_size=42, weight=BOLD, color=WHITE)
        title.to_edge(UP, buff=0.3)

        loss_curve = TracedLossCurve()
        loss_curve.next_to(title, DOWN, buff=0.25)

        step_txt = Text("Step 0", font_size=28, color=GRAY_B)
        step_txt.next_to(loss_curve, DOWN, buff=0.15)

        # Input box - larger
        input_label = Text("Input", font_size=26, weight=BOLD, color=WHITE)
        input_box = RoundedRectangle(width=6.5, height=1.0, corner_radius=0.12,
                                      stroke_color=WHITE, stroke_width=1.2, fill_opacity=0.04)
        input_group = VGroup(input_label, input_box).arrange(DOWN, buff=0.08)
        input_group.next_to(step_txt, DOWN, buff=0.25)

        # Network - centered in middle
        network = TransformerNetwork()
        network.move_to(ORIGIN).shift(DOWN * 0.3)

        # Expected output (target) - larger
        expected_label = Text("Expected", font_size=24, weight=BOLD, color=GREEN_A)
        expected_box = RoundedRectangle(width=7.0, height=1.0, corner_radius=0.12,
                                         stroke_color=GREEN_A, stroke_width=1.2, stroke_opacity=0.6, fill_opacity=0.03)
        expected_group = VGroup(expected_label, expected_box).arrange(DOWN, buff=0.08)
        expected_group.next_to(network, DOWN, buff=0.35)

        # Actual output - larger
        output_label = Text("Output", font_size=24, weight=BOLD, color=GRAY_B)
        output_box = RoundedRectangle(width=7.0, height=1.0, corner_radius=0.12,
                                       stroke_color=GRAY_B, stroke_width=1.2, fill_opacity=0.04)
        output_group = VGroup(output_label, output_box).arrange(DOWN, buff=0.08)
        output_group.next_to(expected_group, DOWN, buff=0.2)

        # Ensure output is near bottom
        output_group.to_edge(DOWN, buff=0.4)
        expected_group.next_to(output_group, UP, buff=0.2)

        # INTRO
        self.play(
            FadeIn(title), FadeIn(loss_curve), FadeIn(step_txt),
            FadeIn(input_group), FadeIn(network),
            FadeIn(expected_group), FadeIn(output_group),
            run_time=0.8,
        )

        input_text = None
        expected_text = None
        output_text = None

        for idx, (prompt, expected, stages) in enumerate(prompts):
            step = idx + 1

            new_step = Text(f"Step {step}", font_size=28, color=GRAY_B)
            new_step.move_to(step_txt)
            self.play(Transform(step_txt, new_step), run_time=0.06)

            if input_text:
                self.play(FadeOut(input_text), FadeOut(expected_text), FadeOut(output_text), run_time=0.05)

            # Show input
            input_text = Text(prompt, font_size=26, color=WHITE)
            input_text.move_to(input_box.get_center())
            self.play(FadeIn(input_text), run_time=0.1)

            # Show expected
            expected_text = Text(expected, font_size=22, color=GREEN_A)
            expected_text.move_to(expected_box.get_center())
            self.play(FadeIn(expected_text), run_time=0.1)

            # STAGE 1: Gibberish
            output_text = Text(stages[0], font_size=22, color=RED_C)
            output_text.move_to(output_box.get_center())
            self.play(
                FadeIn(output_text),
                output_box.animate.set_stroke(RED_C, width=2),
                run_time=0.12,
            )

            network.flow_forward(self)
            self.trace_loss(loss_curve)

            network.backprop_update(self, intensity=0.07)
            self.trace_loss(loss_curve)

            # STAGE 2: Partial
            new_output = Text(stages[1], font_size=22, color=YELLOW_C)
            new_output.move_to(output_box.get_center())
            self.play(
                Transform(output_text, new_output),
                output_box.animate.set_stroke(YELLOW_C, width=2),
                run_time=0.15,
            )

            network.backprop_update(self, intensity=0.05)
            self.trace_loss(loss_curve)

            # STAGE 3: Aligned
            final_output = Text(stages[2], font_size=22, color=GREEN_C)
            final_output.move_to(output_box.get_center())
            self.play(
                Transform(output_text, final_output),
                output_box.animate.set_stroke(GREEN_C, width=2),
                run_time=0.15,
            )

            self.wait(0.12)
            self.play(output_box.animate.set_stroke(GRAY_B, width=1.2), run_time=0.05)

        # Finale
        self.play(FadeOut(input_text), FadeOut(expected_text), FadeOut(output_text), run_time=0.1)

        done = Text("Training Complete", font_size=48, color=GREEN_C, weight=BOLD)
        sub = Text("Output matches Expected", font_size=28, color=GRAY_B)
        finale = VGroup(done, sub).arrange(DOWN, buff=0.15).move_to(ORIGIN)

        self.play(FadeIn(done, scale=1.05), FadeIn(sub), run_time=0.45)
        self.wait(0.5)
        self.play(FadeOut(finale), FadeOut(network), run_time=0.35)

    def trace_loss(self, loss_curve):
        if self.loss_idx < len(self.loss_data):
            step, loss = self.loss_data[self.loss_idx]
            loss_curve.trace(step, loss, self)
            self.loss_idx += 1
