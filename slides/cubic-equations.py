from manim import *
from numpy import arange

class CubicEquations(Scene):
	def construct(self):
		# Show a cubic graph
		axes = Axes(
			x_range=[-3, 3, 1],
			y_range=[-3, 3, 1],
			x_length=5,
			y_length=4
		)
		axis_labels = axes.get_axis_labels()
		x_cubed_graph = axes.get_graph(lambda x: x**3, color=BLUE)
		self.play(Create(axes), Write(axis_labels), run_time=1)
		self.play(Create(x_cubed_graph))
		self.wait(0.5)

		# Show depressed cubic form
		plot = VGroup(axes, axis_labels, x_cubed_graph)
		self.play(plot.animate.align_on_border(RIGHT))
		depressed_cubic = MathTex("x^3 + {{p}}x + {{q}} = 0")
		depressed_cubic.set_color_by_tex("p", RED)
		depressed_cubic.set_color_by_tex("q", BLUE)
		depressed_cubic.align_on_border(LEFT)
		self.play(Write(depressed_cubic))
		self.wait(0.5)

		# Show "cardano's formula" text
		self.play(Uncreate(plot), run_time=0.5)
		self.play(depressed_cubic.animate.move_to(ORIGIN), duration=0.5)
		cardanos_formula_text = Text("Cardanos Formel", font_size=35)
		cardanos_formula_text.align_on_border(UP, buff=SMALL_BUFF)
		self.play(Write(cardanos_formula_text))
		self.play(depressed_cubic.animate.next_to(cardanos_formula_text, DOWN, buff=MED_LARGE_BUFF), duration=0.5)
		self.wait(0.5)

		# Show cardano's formula
		cardanos_formula = MathTex(
			"\\Rightarrow x = \\sqrt[3]{ -", "{q", "\\over 2} +", "\\sqrt{", "{q", "^2 \\over 4} +", "{p", "^3 \\over 27} } } + ",
			"\\sqrt[3]{ -", "{q", "\\over 2} -", "\\sqrt{", "{q", "^2 \\over 4} +", "{p", "^3 \\over 27} } }"
		)
		cardanos_formula[1].set_color(BLUE)
		cardanos_formula[4].set_color(BLUE)
		cardanos_formula[6].set_color(RED)
		cardanos_formula[9].set_color(BLUE)
		cardanos_formula[12].set_color(BLUE)
		cardanos_formula[14].set_color(RED)
		cardanos_formula.next_to(depressed_cubic, DOWN)
		self.play(Write(cardanos_formula))
		self.wait(0.5)

		# Show example
		self.play(Unwrite(cardanos_formula_text), Unwrite(cardanos_formula), Unwrite(depressed_cubic), run_time=0.5)

		example = MathTex("f(x) = x^3 + {{6}}x {{-2}} = 0")
		example.set_color_by_tex("6", RED)
		example.set_color_by_tex("-2", BLUE)
		example.align_on_border(UP, buff=SMALL_BUFF)
		self.play(Write(example))
		self.wait(0.5)

		# Plug numbers into formula
		example_solve_step_1 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{ -{(", "-2", ") \\over 2}", "+ \\sqrt{ {(", "-2", ")^2 \\over 4} +", "{6", "^3 \\over 27} } } + ",
			"\\sqrt[3]{ -{(", "-2", ") \\over 2}", "- \\sqrt{ {(", "-2", ")^2 \\over 4} +", "{6", "^3 \\over 27} } }",
		).scale(0.7)
		example_solve_step_1.set_color_by_tex("6", RED)
		example_solve_step_1.set_color_by_tex("-2", BLUE)
		example_solve_step_1.next_to(example, DOWN, buff=MED_LARGE_BUFF)
		self.play(Write(example_solve_step_1))
		self.wait(0.5)

		# Solve formula
		example_solve_step_2 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{1 + \\sqrt{ {4 \\over 4}", "+ {216 \\over 27} } } + ",
			"\\sqrt[3]{1 - \\sqrt{ {4 \\over 4}", "+ {216 \\over 27} } }",
		).scale(0.7)
		self.play(ReplacementTransform(example_solve_step_1, example_solve_step_2), run_time=0.5)

		example_solve_step_3 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{1 + \\sqrt{1 + 8} } + ",
			"\\sqrt[3]{1 - \\sqrt{1 + 8} }",
		).scale(0.85)
		self.play(ReplacementTransform(example_solve_step_2, example_solve_step_3), run_time=0.5)

		example_solve_step_4 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{1 + \\sqrt{ 9 } } + ",
			"\\sqrt[3]{1 - \\sqrt{ 9 } }",
		).scale(0.9)
		self.play(ReplacementTransform(example_solve_step_3, example_solve_step_4), run_time=0.5)

		example_solve_step_5 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{1 + 3} + ",
			"\\sqrt[3]{1 - 3}",
		)
		self.play(ReplacementTransform(example_solve_step_4, example_solve_step_5), run_time=0.5)

		example_solve_step_6 = MathTex(
			"\\Rightarrow x = \\sqrt[3]{4} + \\sqrt[3]{-2}"
		)
		self.play(ReplacementTransform(example_solve_step_5, example_solve_step_6), run_time=0.5)

		example_solution = MathTex(
			"\\Rightarrow x = \\sqrt[3]{4} - \\sqrt[3]{2}"
		)
		self.play(ReplacementTransform(example_solve_step_6, example_solution), run_time=0.5)

		example_solution_approx = MathTex("\\approx 0.32")
		example_solution_approx.next_to(example_solution)
		self.play(Write(example_solution_approx))
		self.wait(0.5)

		# Verify solution
		axes = Axes(
			x_range=[-2, 2, 0.5],
			y_range=[-2, 2, 0.5],
			x_length=4,
			y_length=4,
			x_axis_config={
				"numbers_to_include": np.arange(-2, 2, 1),
				"numbers_with_elongated_ticks": np.arange(-2, 2, 1)
			}
		)
		axes.align_on_border(RIGHT, buff=SMALL_BUFF)
		axis_labels = axes.get_axis_labels()
		root_dot = Dot(point=axes.coords_to_point(0.32, 0), color=YELLOW)
		solution = VGroup(example_solution, example_solution_approx)
		self.play(example.animate.align_on_border(LEFT), solution.animate.align_on_border(LEFT))
		example_graph = axes.get_graph(lambda x: x**3 + 6*x - 2, color=BLUE)
		example_graph_label = axes.get_graph_label(example_graph, label="f")
		self.play(Create(axes), Write(axis_labels))
		self.play(Create(example_graph), Create(root_dot), Write(example_graph_label))
		self.wait(0.5)