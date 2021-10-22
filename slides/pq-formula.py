from manim import *
from manim_presentation import *;

class PQFormula(Slide):
	def construct(self):
		# pq_formula = MathTex(r"$ -{{p}} \over {2} $ \pm \sqrt{ $ {{p}}^2 \over {4} $ - {{q}} }")
		# pq_formula = MathTex(r"{- {{p}} \over 2} \pm \sqrt { p^2 \over 2 } - q")
		pq_formula = MathTex("{-", "p", "\\over 2} \\pm", "\\sqrt{", "{p", "^2 \\over 2} -", "q}")

		# Show the formula
		self.play(Write(pq_formula))
		self.pause()
		

		# Show it's meaning
		self.play(pq_formula.animate.shift(DOWN))

		pq_equation = MathTex("x^2 + {{p}} x + {{q}} = 0")
		pq_equation.set_color_by_tex("p", RED)
		pq_equation.set_color_by_tex("q", BLUE)
		pq_equation.move_to(UP)
		self.play(
			Write(pq_equation),
			pq_formula[1].animate.set_color(RED),
			pq_formula[4].animate.set_color(RED),
			pq_formula[6].animate.set_color(BLUE)
			# pq_formula.animate.set_color_by_tex("q", BLUE)
		)

		self.play(pq_formula.animate.shift(RIGHT), run_time=0.5)

		implies_x_equals = MathTex("\\Rightarrow x =")
		implies_x_equals.next_to(pq_formula, LEFT)
		self.play(Write(implies_x_equals), run_time=0.2)
		self.pause()

		# Move to box
		self.play(
			Unwrite(pq_equation),
			Unwrite(implies_x_equals)
		)
		self.play(pq_formula.animate.align_on_border(LEFT + UP))
		formula_frame = SurroundingRectangle(pq_formula, buff=MED_LARGE_BUFF)
		formula_frame.set_color(DARK_BLUE)
		self.play(Create(formula_frame))
		self.pause()

		# Create example
		example = MathTex("x^2 +", "2", "x +", "4")
		example.shift(UP)
		example[1].set_color(RED)
		example[3].set_color(BLUE)
		self.play(Write(example))
		self.pause()

		# Show solution attempt
		solution_attempt_1 = MathTex("\\Rightarrow x = {-", "2", "\\over 2}", "\\pm", "\\sqrt{", "{2", "^2 \\over 2}", "-", "4}")
		solution_attempt_1[1].set_color(RED)
		solution_attempt_1[5].set_color(RED)
		solution_attempt_1[8].set_color(BLUE)
		self.play(Write(solution_attempt_1))


		solution_attempt_2 = MathTex("\\Rightarrow x = {-", "1", "\\pm", "\\sqrt{", "{4 \\over 2}", "-", "4}")
		self.play(ReplacementTransform(solution_attempt_1, solution_attempt_2))

		solution_attempt_3 = MathTex("\\Rightarrow x = {-", "1", "\\pm", "\\sqrt{", "2", "-", "4}")
		self.play(ReplacementTransform(solution_attempt_2, solution_attempt_3))

		solution_attempt_4 = MathTex("\\Rightarrow x = {-", "1", "\\pm", "\\sqrt{", "-2", "}")
		self.play(ReplacementTransform(solution_attempt_3, solution_attempt_4))
		self.pause()

		# Show that no solution exists
		self.play(
			solution_attempt_4.animate.align_on_border(RIGHT + UP),
			Unwrite(example)
		)

		axes = Axes(
			x_range=[-10, 10, 1],
			y_range=[-10, 10, 1],
			x_length=10,
		)
		axes_labels = axes.get_axis_labels()
		graph = axes.get_graph(lambda x: x**2 + 2 * x + 4, color=BLUE)
		self.play(Create(axes), Write(axes_labels))
		self.play(DrawBorderThenFill(graph))

		self.wait()