# 01_convolution.py
from manim import *
import numpy as np

# ---------- helpers ----------
def grid(n_rows, n_cols, cell_size=0.6, color=WHITE):
    cells = VGroup()
    for r in range(n_rows):
        row = VGroup()
        for c in range(n_cols):
            sq = Square(side_length=cell_size).set_stroke(color, 2)
            row.add(sq)
        row.arrange(RIGHT, buff=0)
        cells.add(row)
    cells.arrange(DOWN, buff=0)
    return cells

def fill_numbers(cells, values, scale=0.6):
    texts = VGroup()
    for r, row in enumerate(cells):
        for c, cell in enumerate(row):
            t = MathTex(str(int(values[r, c]))).scale(scale)
            t.move_to(cell.get_center())
            texts.add(t)
    return texts

def place_panel(panel: VGroup, output_grid: VGroup, *, prefer="right", buff_right=0.6, buff_up=0.4):
    frame_right = config.frame_width / 2
    frame_top   = config.frame_height / 2
    margin = 0.3

    if prefer == "right":
        panel.next_to(output_grid, RIGHT, buff=buff_right, aligned_edge=UP)
        if panel.get_right()[0] > frame_right - margin:
            panel.next_to(output_grid, UP, buff=buff_up, aligned_edge=LEFT)
            dy = panel.get_top()[1] - (frame_top - margin)
            if dy > 0:
                panel.shift(DOWN * dy)
    else:
        panel.next_to(output_grid, UP, buff=buff_up, aligned_edge=LEFT)
        dy = panel.get_top()[1] - (frame_top - margin)
        if dy > 0:
            panel.shift(DOWN * dy)
    return panel

# ---------- scene ----------
class Conv2DValidStride1(Scene):
    def construct(self):
        # --- INTRO PHASE ---
        title = Text("Convolution in CNNs", font_size=60, weight=BOLD)
        subtitle = Text(
            "We’ll slide a 3×3 kernel across a 5×5 input\n"
            "to produce a 3×3 output feature map.\n"
            "Watch how each step multiplies and sums.",
            font_size=32,
            line_spacing=1.2
        )
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(title, shift=UP*0.5), run_time=1.2)
        self.play(Write(subtitle), run_time=2.0)
        self.wait(2.0)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1.0)

        # --- DATA SETUP ---
        X = np.array([
            [1,2,0,3,1],
            [0,1,2,3,1],
            [1,2,1,0,0],
            [2,1,0,1,2],
            [0,1,2,2,1]
        ])
        K = np.array([[1,0,-1],
                      [1,0,-1],
                      [1,0,-1]])

        in_h, in_w = X.shape
        kh, kw = K.shape
        out_h, out_w = in_h - kh + 1, in_w - kw + 1

        # grids
        input_grid  = grid(in_h, in_w)
        kernel_grid = grid(kh, kw).scale(0.9)
        output_grid = grid(out_h, out_w)

        input_title  = Text("Input (5×5)").scale(0.5).next_to(input_grid, UP, buff=0.25)
        kernel_title = Text("Kernel (3×3)").scale(0.5).next_to(kernel_grid, UP, buff=0.25)
        output_title = Text("Output (3×3)").scale(0.5).next_to(output_grid, UP, buff=0.25)

        trio = VGroup(
            VGroup(input_grid, input_title),
            VGroup(kernel_grid, kernel_title),
            VGroup(output_grid, output_title),
        ).arrange(RIGHT, buff=1.2)

        trio.scale_to_fit_width(11.2)
        trio.to_edge(LEFT, buff=0.8)

        self.play(FadeIn(trio))

        # numbers
        in_nums  = fill_numbers(input_grid, X, scale=0.6)
        ker_nums = fill_numbers(kernel_grid, K, scale=0.6)
        self.play(FadeIn(in_nums), FadeIn(ker_nums))

        # window
        initial_cells = VGroup(*[input_grid[r][c] for r in range(kh) for c in range(kw)])
        window = SurroundingRectangle(initial_cells, color=YELLOW, buff=0.02)
        window.set_z_index(10)
        self.play(Create(window))

        # panel title
        title_label = Text("Multiply & Sum").scale(0.4)
        first_title_set = False

        # computation loop
        for r in range(out_h):
            for c in range(out_w):
                target_cells = VGroup(*[input_grid[r+i][c+j] for i in range(kh) for j in range(kw)])
                self.play(window.animate.surround(target_cells), run_time=0.4)

                mult_terms = VGroup()
                sum_val = 0
                for idx in range(kh*kw):
                    i, j = divmod(idx, kw)
                    x_val = int(X[r+i, c+j])
                    k_val = int(K[i,j])
                    sum_val += x_val * k_val

                    term = VGroup(
                        MathTex(str(x_val)).scale(0.55),
                        MathTex(r"\times").scale(0.55),
                        MathTex(str(k_val)).scale(0.55),
                    ).arrange(RIGHT, buff=0.06)

                    term.move_to(RIGHT*0.9*j + DOWN*0.45*i)
                    mult_terms.add(term)

                mult_terms.move_to(ORIGIN)
                brace = Brace(mult_terms, UP)
                eq = MathTex("=", str(sum_val)).scale(0.65)
                panel_body = VGroup(mult_terms, brace).arrange(UP, buff=0.15)
                panel = VGroup(panel_body, eq).arrange(RIGHT, buff=0.25)

                place_panel(panel, output_grid, prefer="right", buff_right=0.6, buff_up=0.45)

                # keep panel above output title
                safe_line = output_title.get_top()[1] + 0.15
                bottom_y = panel.get_bottom()[1]
                if bottom_y < safe_line:
                    panel.shift(UP * (safe_line - bottom_y))

                title_label.next_to(panel, UP, buff=0.18).align_to(panel, LEFT)
                if not first_title_set:
                    self.play(FadeIn(title_label))
                    first_title_set = True

                self.play(FadeIn(mult_terms, lag_ratio=0.05), FadeIn(brace), Write(eq))

                out_text = MathTex(str(sum_val)).scale(0.7).move_to(output_grid[r][c].get_center())
                self.play(Write(out_text), run_time=0.35)

                self.play(FadeOut(mult_terms), FadeOut(brace), FadeOut(eq), run_time=0.2)
                self.add(out_text)

        self.wait(0.5)
