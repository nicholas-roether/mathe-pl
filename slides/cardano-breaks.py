from manim import *;

class CardanoBreaks(Scene):
	def construct(self):
		# Show counter-example
		axes = Axes(
			x_range=[-4, 4, 1],
			y_range=[-3, 10, 2],
			x_length=4,
			y_length=4,
			x_axis_config={
				"numbers_to_include": np.arange(-4, 4, 2)
			},
			y_axis_config={
				"numbers_to_include": np.arange(-2, 10, 4)
			}
		)
		axes.align_on_border(RIGHT, buff=SMALL_BUFF)
		axis_labels = axes.get_axis_labels()
		counter_example_graph = axes.get_graph(lambda x: x**3 - 6*x + 4, color=BLUE)
		root_dots = [
			Dot(axes.coords_to_point(-2.73, 0), color=YELLOW),
			Dot(axes.coords_to_point(0.73, 0), color=YELLOW),
			Dot(axes.coords_to_point(2, 0), color=YELLOW)
		]
		counter_example_graph_label = axes.get_graph_label(counter_example_graph, "g")
		counter_example = MathTex("g(x) = x^3 {{-6}}x + {{4}}")
		counter_example.set_color_by_tex("-6", RED)
		counter_example.set_color_by_tex("4", BLUE)
		counter_example.align_on_border(UP + LEFT, buff=SMALL_BUFF)
		self.play(Create(axes), Write(axis_labels), Write(counter_example))
		self.play(Create(counter_example_graph), *list(map(lambda dot: Create(dot), root_dots)), Write(counter_example_graph_label))
		self.wait(0.5)

		# Plug stuff into formula
		plot = VGroup(axes, axis_labels, counter_example_graph, counter_example_graph_label, *root_dots)
		self.play(FadeOut(plot), run_time=0.5)
		self.play(counter_example.animate.set_x(0))

		solve_initial = MathTex(
			"\\Rightarrow x = \\sqrt[3]{ -{4 \\over 2} + \\sqrt{ {4^2 \\over 4} + {(-6)^3 \\over 27}}}",
			"+ \\sqrt[3]{ -{4 \\over 2} - \\sqrt{ {4^2 \\over 4} + {(-6)^3 \\over 27}}}"
		)
		solve_initial.scale(0.7)
		solve_initial.next_to(counter_example, DOWN, buff=MED_LARGE_BUFF)
		self.play(Create(solve_initial))
		self.wait(0.5)

		# Solve till negative \\sqrt
		solve_step_1 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{ -2 + \\sqrt{ {16 \\over 4} + {-216 \\over 27}}}",
			"+ \\sqrt[3]{ -2 - \\sqrt{ {16 \\over 4} + {-216 \\over 27}}}"
		).scale(0.7)
		self.play(ReplacementTransform(solve_initial, solve_step_1), run_time=0.5)

		solve_step_2 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{ -2 + \\sqrt{4 - 8}}",
			"+ \\sqrt[3]{ -2 - \\sqrt{4 - 8}}"
		).scale(0.85)
		self.play(ReplacementTransform(solve_step_1, solve_step_2), run_time=0.5)

		solve_step_3 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{ -2 + \\sqrt{-4}}",
			"+ \\sqrt[3]{ -2 - \\sqrt{-4}}"
		)
		self.play(ReplacementTransform(solve_step_2, solve_step_3), run_time=0.5)
		self.wait(0.5)

		# Rewrite negative square roots
		solve_step_4 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{ -2 + 2\\sqrt{-1}}",
			"+ \\sqrt[3]{ -2 - 2\\sqrt{-1}}"
		)
		self.play(ReplacementTransform(solve_step_3, solve_step_4), run_time=0.5)
		self.wait(0.5)

		# make stuff much more complicated
		solve_step_5 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{", "1 - 3 + 3\\sqrt{-1} - \\sqrt{-1}}",
			"+ \\sqrt[3]{", "3 - 1 - 3\\sqrt{-1} + \\sqrt{-1}}"
		).scale(0.7)
		self.play(ReplacementTransform(solve_step_4, solve_step_5), run_time=0.5)

		solve_step_6 = MathTex(
			"\\Rightarrow x =", 
			"\\sqrt[3]{1 + 3 \\cdot 1 \\cdot (-1) + 3 \\cdot 1 \\cdot \\sqrt{-1} + \\sqrt{-1} \\cdot (-1)} \\\\",
			"+ \\sqrt[3]{1 + 3 \\cdot 1 \\cdot (-1) + 3 \\cdot 1 \\cdot (-\\sqrt{-1}) - \\sqrt{-1} \\cdot (-1)}"
		).scale(0.7)
		self.play(ReplacementTransform(solve_step_5, solve_step_6), run_time=0.5)

		solve_step_7 = MathTex(
			"\\Rightarrow x =", 
			"\\sqrt[3]{1^3 + 3 \\cdot 1 \\cdot \\sqrt{-1}^2 + 3 \\cdot 1^2 \\cdot \\sqrt{-1} + \\sqrt{-1} \\cdot \\sqrt{-1}^2} \\\\",
			"+ \\sqrt[3]{1^3 + 3 \\cdot 1 \\cdot \\sqrt{-1}^2 + 3 \\cdot 1^2 \\cdot (-\\sqrt{-1}) - \\sqrt{-1} \\cdot \\sqrt{-1}^2}"
		).scale(0.7)
		self.play(ReplacementTransform(solve_step_6, solve_step_7), run_time=0.5)

		solve_step_8 = MathTex(
			"\\Rightarrow x =", 
			"\\sqrt[3]{1^3 + 3 \\cdot 1 \\cdot \\sqrt{-1}^2 + 3 \\cdot 1^2 \\cdot \\sqrt{-1} + \\sqrt{-1}^3} \\\\",
			"+ \\sqrt[3]{1^3 + 3 \\cdot 1 \\cdot (-\\sqrt{-1})^2 + 3 \\cdot 1^2 \\cdot (-\\sqrt{-1}) - \\sqrt{-1}^3}"
		).scale(0.7)
		self.play(ReplacementTransform(solve_step_7, solve_step_8), run_time=0.5)

		solve_step_9 = MathTex(
			"\\Rightarrow x =", 
			"\\sqrt[3]{1\\relax^3 + 3 \\cdot 1\\relax \\cdot \\sqrt{-1}^2 + 3 \\cdot 1\\relax^2 \\cdot \\sqrt{-1} + \\sqrt{-1}^3} \\\\",
			"+ \\sqrt[3]{1\\relax^3 + 3 \\cdot 1\\relax \\cdot (-\\sqrt{-1})^2 + 3 \\cdot 1\\relax^2 \\cdot (-\\sqrt{-1}) + (-\\sqrt{-1})^3}",
		).scale(0.7)
		self.play(ReplacementTransform(solve_step_8, solve_step_9), run_time=0.5)
		self.wait(0.5)

		# Show cubic binomial formula
		cubic_binomial = MathTex("(a + b)^3 = a^3 + 3ab^2 + 3a^2 b + b^3")
		cubic_binomial.set_color(RED)
		cubic_binomial.scale(0.7)
		cubic_binomial.align_on_border(DOWN)
		cubic_binomial_box = SurroundingRectangle(cubic_binomial, color=RED)
		self.play(Write(cubic_binomial), Create(cubic_binomial_box))
		self.wait(0.5)

		# complete the cube
		solve_step_10 = MathTex(
			"\\Rightarrow x =", 
			"\\sqrt[3]{", "(1 + \\sqrt{-1})^3}",
			"+ \\sqrt[3]{", "(1 - \\sqrt{-1})^3}",
		).scale(0.7)
		self.play(ReplacementTransform(solve_step_9, solve_step_10), run_time=0.5)

		solve_step_11 = MathTex(
			"\\Rightarrow x =", 
			"1", "+", "\\sqrt{-1}",
			"+", "1" "-", "\\sqrt{-1}",
		)
		self.play(ReplacementTransform(solve_step_10, solve_step_11), run_time=0.5)
		self.play(Unwrite(cubic_binomial), Uncreate(cubic_binomial_box), run_time=0.5)
		self.wait(0.5)

		# Solution
		solve_step_12 = MathTex("\\Rightarrow x =", "1", "+", "1")
		self.play(TransformMatchingTex(solve_step_11, solve_step_12), run_time=2)
		
		solution = MathTex("\\Rightarrow x = 2")
		self.play(ReplacementTransform(solve_step_12, solution))
		self.wait(0.5)

		# Check solution
		self.play(counter_example.animate.align_on_border(LEFT), solution.animate.align_on_border(LEFT))
		self.play(FadeIn(axes), FadeIn(axis_labels), FadeIn(counter_example_graph))
		found_dot = Dot(axes.coords_to_point(2, 0), color=RED, radius=DEFAULT_DOT_RADIUS * 1.2)
		label = MathTex("2", color="RED")
		label.next_to(found_dot, DOWN + RIGHT)
		self.play(Write(label), Create(found_dot))

		self.wait()