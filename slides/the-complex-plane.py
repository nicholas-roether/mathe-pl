from manim import *;

class TheComplexPlane(Scene):
	def get_im_axis_label(self, num: float) -> str:
		if (num == 0): return "0"
		if (num == 1): return "i"
		if (num == -1): return "-i"
		return str(num) + "i"

	def construct(self):
		# Show a complex number (duration: 1.5)
		complex_number = MathTex("z = {{a}} + {{b}}i")
		complex_number.set_color_by_tex("a", RED).set_color_by_tex("b", BLUE)
		complex_number.scale(1.5)
		self.play(Write(complex_number))
		self.wait(0.5)

		# Show a complex number w/ x and y (duration: 1.5)
		complex_number_x_y = MathTex("z = {{x}} + {{y}}i")
		complex_number_x_y.set_color_by_tex("x", RED).set_color_by_tex("y", BLUE)
		complex_number_x_y.scale(1.5)
		self.play(ReplacementTransform(complex_number, complex_number_x_y))
		self.wait(0.5)

		# Place number on plane and move it around a bit (duration: 5)
		axes = Axes(
			x_range=[-3, 9],
			y_range=[-1, 5, 1],
			x_length=8,
			y_length=4,
			x_axis_config={
				"include_numbers": True,
			}
		)
		axes.y_axis.add_labels(dict((num, self.get_im_axis_label(num)) for num in [*range(-1, 0), *range(1, 5)]))
		axis_labels = axes.get_axis_labels(Tex("Re"), Tex("Im"))
		num_point = axes.coords_to_point(4, 2)

		num_point_x_tracker = ValueTracker(4)
		num_point_y_tracker = ValueTracker(2)

		def get_num_point() -> np.ndarray:
			return axes.coords_to_point(num_point_x_tracker.get_value(), num_point_y_tracker.get_value())

		def get_num_text(x, y, alignment) -> MathTex:
			num_text = MathTex(str(x), "+", str(y), "i")
			num_text.set_color_by_tex(str(x), RED)
			num_text.set_color_by_tex(str(y), BLUE)
			num_text.next_to(axes.coords_to_point(x, y), alignment)
			return num_text

		num_text_1 = get_num_text(4, 2, UR)
		num_dot = Dot(get_num_point())
		num_dot.add_updater(lambda m: m.move_to(get_num_point()))
		x_pos_line = axes.get_horizontal_line(num_point, color=BLUE)
		y_pos_line = axes.get_vertical_line(num_point, color=RED)
		x_pos_line.add_updater(lambda m: m.become(axes.get_horizontal_line(get_num_point(), color=BLUE)))
		y_pos_line.add_updater(lambda m: m.become(axes.get_vertical_line(get_num_point(), color=RED)))
		self.play(
			Create(axes),
			Write(axis_labels),
			Create(num_dot),
			ReplacementTransform(complex_number_x_y, num_text_1),
		)
		self.play(
			Create(x_pos_line),
			Create(y_pos_line),
			run_time=0.5
		)
		num_text_2 = get_num_text(-1, 4, DL)
		self.play(
			num_point_x_tracker.animate.set_value(-1),
			num_point_y_tracker.animate.set_value(4),
			ReplacementTransform(num_text_1, num_text_2)
		)
		num_text_3 = get_num_text(6, -1, RIGHT)
		self.play(
			num_point_x_tracker.animate.set_value(6),
			num_point_y_tracker.animate.set_value(-1),
			ReplacementTransform(num_text_2, num_text_3)
		)
		num_text = get_num_text(2, 3, UR)
		self.play(
			num_point_x_tracker.animate.set_value(2),
			num_point_y_tracker.animate.set_value(3),
			ReplacementTransform(num_text_3, num_text)
		)
		self.wait(0.5)

		# Show point/vector duality (duration: 3)
		num_vector = Arrow(start=axes.get_origin(), end=get_num_point(), buff=0)
		num_vector.add_updater(lambda m: m.put_start_and_end_on(start=axes.get_origin(), end=get_num_point()))
		self.play(FadeOut(num_dot), FadeIn(num_vector))
		self.wait(0.5)
		self.play(FadeOut(num_vector), FadeIn(num_dot))
		self.wait(0.5)

		# Prepare vector addition comparison (duration: 3)
		plot = VGroup(axes, axis_labels)
		num = VGroup(num_text, num_dot, x_pos_line, y_pos_line)
		self.play(FadeOut(plot), Uncreate(num), run_time=0.5)
		complex_addition = MathTex("(", "a", "+", "b", "i", ")", "+", "(", "c", "+", "d", "i", ")")
		complex_addition.set_color_by_tex("a", RED).set_color_by_tex("b", BLUE).set_color_by_tex("c", YELLOW).set_color_by_tex("d", GREEN)
		complex_addition.shift(UP)
		vector_1 = Matrix([["a"], ["b"]])
		vector_1.set_row_colors(RED, BLUE)
		vector_2 = Matrix([["c"], ["d"]])
		vector_2.set_row_colors(YELLOW, GREEN)
		plus = MathTex("+")
		plus.next_to(vector_1)
		vector_2.next_to(plus)
		vector_addition = VGroup(vector_1, plus, vector_2)
		vector_addition.set_x(0)
		vector_addition.shift(DOWN)
		self.play(Write(complex_addition))
		self.play(Write(vector_addition))
		self.wait(0.5)

		# Demonstate similarity between complex and vector addition (duration: 1.5)
		complex_addition_result = MathTex("(", "a", "+", "c", ")", "+", "(", "b", "+", "d", ")", "i")
		complex_addition_result.set_color_by_tex("a", RED).set_color_by_tex("b", BLUE).set_color_by_tex("c", YELLOW).set_color_by_tex("d", GREEN)
		complex_addition_result.match_x(complex_addition).match_y(complex_addition)
		vector_addition_result = Matrix([["{{a}} + {{c}}"], ["{{b}} + {{d}}"]])
		vector_addition_result.get_rows()[0][0].set_color_by_tex("a", RED).set_color_by_tex("c", YELLOW)
		vector_addition_result.get_rows()[1][0].set_color_by_tex("b", BLUE).set_color_by_tex("d", GREEN)
		vector_addition_result.match_x(vector_addition).match_y(vector_addition)
		self.play(
			TransformMatchingTex(complex_addition, complex_addition_result),
			TransformMatchingShapes(vector_addition, vector_addition_result)
		)
		self.wait(0.5)

		# Show complex addition geometrically (duration: 6)
		self.play(Unwrite(complex_addition_result), Unwrite(vector_addition_result), duration=0.5)
		self.play(FadeIn(plot))

		z_1 = axes.coords_to_point(4,1)
		z_2 = axes.coords_to_point(-2, 3)
		z_3 = axes.coords_to_point(2, 4)
		z_1_dot = Dot(z_1, color=RED)
		z_2_dot = Dot(z_2, color=BLUE)
		z_3_dot = Dot(z_3)
		z_1_label = MathTex("z_1")
		z_1_label.next_to(z_1_dot, UR, buff=SMALL_BUFF)
		z_1_label.set_color(RED)
		z_1_label.add_updater(lambda l: l.next_to(z_1_dot, UR, buff=SMALL_BUFF))
		z_2_label = MathTex("z_2")
		z_2_label.set_color(BLUE)
		z_2_label.next_to(z_2_dot, UR, buff=SMALL_BUFF)
		z_2_label.add_updater(lambda l: l.next_to(z_2_dot, UR, buff=SMALL_BUFF))
		z_3_label_add = MathTex("{{z_1}} + {{z_2}}")
		z_3_label_add.set_color_by_tex("z_1", RED).set_color_by_tex("z_2", BLUE)
		z_3_label_add.next_to(z_3_dot, UR, buff=SMALL_BUFF)
		z_1_arrow = Arrow(start=axes.get_origin(), end=z_1, color=RED, buff=0)
		z_2_arrow = Arrow(start=axes.get_origin(), end=z_2, color=BLUE, buff=0)
		self.play(Create(z_1_dot), Create(z_2_dot), Write(z_1_label), Write(z_2_label))
		self.play(Create(z_1_arrow), Create(z_2_arrow))
		self.play(z_2_arrow.animate.put_start_and_end_on(start=z_1, end=z_3))
		self.play(Create(z_3_dot), Write(z_3_label_add))
		self.wait(0.5)

		# Show complex multiplication (duration: till end)
		self.play(Uncreate(z_1_arrow), Uncreate(z_2_arrow), FadeOut(z_3_dot), Unwrite(z_3_label_add), run_time=0.5)
		z_1 = axes.coords_to_point(3, -1)
		z_2 = axes.coords_to_point(1, 2)
		z_3 = axes.coords_to_point(5, 5)
		z_3_dot.move_to(z_3)
		self.play(
			z_1_dot.animate.move_to(z_1),
			z_2_dot.animate.move_to(z_2)
		)
		z_3_label_mult = MathTex("{{z_1}} \\cdot {{z_2}}")
		z_3_label_mult.set_color_by_tex("z_1", RED).set_color_by_tex("z_2", BLUE)
		z_3_label_mult.next_to(z_3_dot, DR, buff=SMALL_BUFF)
		self.play(Create(z_3_dot), Write(z_3_label_mult))
		self.wait(0.5)