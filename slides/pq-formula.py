from manim import *


class PQFormula(Scene):
	sectionCounter = 0
	sectionStartTime = 0


	def construct(self):
		pq_formula = MathTex("{-", "p", "\\over 2} \\pm", "\\sqrt{", "{p", "^2 \\over 2} -", "q}")

		# Show the formula (duration: 1.5)
		self.play(Write(pq_formula))
		self.wait(0.5)

		# Show it's meaning (duration: 3.5)
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
		)

		self.play(pq_formula.animate.shift(RIGHT), run_time=0.5)

		implies_x_equals = MathTex("\\Rightarrow x =")
		implies_x_equals.next_to(pq_formula, LEFT)
		self.play(Write(implies_x_equals), run_time=0.5)
		self.wait(0.5)

		# Move to box (duration: 2.5)
		self.play(
			Unwrite(pq_equation),
			Unwrite(implies_x_equals),
			run_time=0.5
		)
		self.play(pq_formula.animate.align_on_border(LEFT + UP, buff=SMALL_BUFF))
		formula_frame = SurroundingRectangle(pq_formula, buff=SMALL_BUFF)
		formula_frame.set_color(DARK_BLUE)
		self.play(Create(formula_frame), run_time=0.5)
		self.wait(0.5)

		# Create example (duration: 1.5)
		example = MathTex("x^2 +", "2", "x +", "4", "= 0")
		example.shift(UP + RIGHT)
		example[1].set_color(RED)
		example[3].set_color(BLUE)
		self.play(Write(example))
		self.wait(0.5)

		# Show plugging in values (duration: 2)
		solution_attempt_1 = MathTex("\\Rightarrow x = {-", "2", "\\over 2}", "\\pm", "\\sqrt{", "{2", "^2 \\over 2}", "-", "4}")
		solution_attempt_1.shift(RIGHT)
		solution_attempt_1[1].set_color(RED)
		solution_attempt_1[5].set_color(RED)
		solution_attempt_1[8].set_color(BLUE)
		self.play(Write(solution_attempt_1))
		self.wait(0.5)

		# Show solution attempt (duration: 2)
		solution_attempt_2 = MathTex("\\Rightarrow x = {-", "1", "\\pm", "\\sqrt{", "{4 \\over 2}", "-", "4}")
		solution_attempt_2.shift(RIGHT)
		self.play(ReplacementTransform(solution_attempt_1, solution_attempt_2), run_time=0.5)

		solution_attempt_3 = MathTex("\\Rightarrow x = {-", "1", "\\pm", "\\sqrt{", "2", "-", "4}")
		solution_attempt_3.shift(RIGHT)
		self.play(ReplacementTransform(solution_attempt_2, solution_attempt_3), run_time=0.5)

		solution_attempt_4 = MathTex("\\Rightarrow x = {-", "1", "\\pm", "\\sqrt{", "-2", "}")
		solution_attempt_4.shift(RIGHT)
		self.play(ReplacementTransform(solution_attempt_3, solution_attempt_4), run_time=0.5)
		self.wait(0.5)

		# Show that no solution exists (duration: till end)
		self.play(Unwrite(example), run_time=0.5)
		self.play(solution_attempt_4.animate.align_on_border(LEFT + DOWN, buff=SMALL_BUFF))

		axes = Axes(
			x_range=[-10, 10, 2],
			y_range=[-10, 10, 2],
			x_length=5,
			y_length=5
		)
		axes.shift(RIGHT * 2)
		axis_labels = axes.get_axis_labels()
		graph = axes.get_graph(lambda x: x**2 + 2 * x + 4, color=BLUE)
		self.play(Create(axes), Write(axis_labels), run_time=1)
		self.play(Create(graph))
		self.wait(0.5)

		