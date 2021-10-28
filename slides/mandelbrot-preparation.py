from manim import *;

class MandelbrotPreparation(Scene):
	def construct(self):
		# Show series definition (duration: 1.5)
		series_def = MathTex("z_n = z_{n-1}^2 + {{c}}")
		series_def.set_color_by_tex("c", GREEN)
		series_def.scale(1.5)
		self.play(Write(series_def))
		self.wait(0.5)

		# Show that z0 equals 0 (duration: 1.5)
		z_0_eq_0_tex = MathTex("{{z_0}} = 0")
		z_0_eq_0_tex.set_color_by_tex("z_0", RED)
		z_0_eq_0_tex.scale(1.2)
		z_0_eq_0_tex.next_to(series_def, DOWN)
		self.play(Write(z_0_eq_0_tex))
		self.wait(0.5)

		# Show axes (duration: 3)
		series_def_group = VGroup(series_def, z_0_eq_0_tex)
		self.play(series_def_group.animate.scale(1 / 1.5), run_time=0.5)
		self.play(series_def_group.animate.align_on_border(UL, buff=SMALL_BUFF))
		axes = Axes(
			x_range=[-2.3, 2.3, 1],
			y_range=[-1.5, 1.5, 1],
			x_length=6 + 2 / 15,
			y_length=4
		)
		axis_labels = axes.get_axis_labels(Tex("Re"), Tex("Im"))
		z_0_dot = Dot(axes.coords_to_point(0, 0), color=RED)
		z_0_label = MathTex("z_0", color=RED)
		z_0_label.next_to(z_0_dot, UR, buff=SMALL_BUFF)

		self.play(Create(axes), Write(axis_labels))
		self.wait(0.5)

		# Show z_0 dot (duration: 1.5)
		self.play(Create(z_0_dot), Write(z_0_label))
		self.wait(0.5)

		# Hide z_0 dot (duration: 1.5)
		self.play(Uncreate(z_0_dot), Unwrite(z_0_label))
		self.wait(0.5)

		# Show c dot (duration: 1.5)
		c = ComplexValueTracker(complex(0.3, 0.7))
		c_dot = Dot(axes.coords_to_point(c.get_value().real, c.get_value().imag), color=GREEN)
		c_dot.add_updater(lambda d: d.move_to(axes.coords_to_point(c.get_value().real, c.get_value().imag)))
		c_dot_label = MathTex("c", color=GREEN)
		c_dot_label.next_to(c_dot, UR, buff=SMALL_BUFF).add_updater(lambda l: l.next_to(c_dot, UR, buff=SMALL_BUFF))
		self.play(Create(c_dot), Write(c_dot_label))
		self.wait(0.5)

		# Show first series step (duration: 5)
		start_num = ComplexValueTracker(complex(0, 0))
		def num_to_point(num: complex):
			return axes.coords_to_point(num.real, num.imag)
		def get_start_point():
			return axes.coords_to_point(start_num.get_value().real, start_num.get_value().imag)
		def get_squared_point():
			square = start_num.get_value()**2
			return axes.coords_to_point(square.real, square.imag)
		def get_squared_added_point():
			square_added = start_num.get_value()**2 + c.get_value()
			return axes.coords_to_point(square_added.real, square_added.imag)
		squared_dot = Dot(get_squared_point(), color=GRAY)
		squared_dot.scale(0.7)
		squared_dot.add_updater(lambda d: d.move_to(get_squared_point()))

		square_arrow = CurvedArrow(get_start_point(), get_squared_point(), color=ORANGE)
		square_arrow.add_updater(lambda a: a.become(CurvedArrow(get_start_point(), get_squared_point(), color=ORANGE)))
		add_arrow = Arrow(get_squared_point(), get_squared_added_point(), color=GREEN, buff=0)
		add_arrow.add_updater(lambda a: a.become(Arrow(get_squared_point(), get_squared_added_point(), color=GREEN, buff=0)))

		square_arrow_label = MathTex("z^2", color=ORANGE, background_stroke_width=5)
		square_arrow_label.scale(0.8)
		square_arrow_label.move_to(square_arrow.get_midpoint()).add_updater(lambda l: l.move_to(square_arrow.get_midpoint()))
		add_arrow_label = MathTex("z + c", color=GREEN, background_stroke_width=5)
		add_arrow_label.scale(0.8)
		add_arrow_label.move_to(add_arrow.get_midpoint()).add_updater(lambda l: l.move_to(add_arrow.get_midpoint()))

		square_arrow_group = VGroup(square_arrow, square_arrow_label)
		add_arrow_group = VGroup(add_arrow, add_arrow_label)

		def animate_steps_to_dot(next_dot):
			self.play(Create(square_arrow_group))
			self.play(Create(squared_dot), run_time=0.5)
			self.play(FadeOut(square_arrow_group), run_time=0.5)
			self.play(Create(add_arrow_group))
			self.play(Create(next_dot))
			self.play(FadeOut(add_arrow_group), FadeOut(squared_dot), run_time=0.5)
			start_num.set_value(start_num.get_value()**2 + c.get_value())

		step_1_square_arrow = CurvedArrow(get_start_point(), get_squared_point() + LEFT * 0.001, color=ORANGE, angle=TAU * 0.8)
		self.play(Create(step_1_square_arrow), Write(square_arrow_label))
		self.play(Create(squared_dot), run_time=0.5)
		self.play(FadeOut(step_1_square_arrow), FadeOut(square_arrow_label), run_time=0.5)
		self.play(Create(add_arrow_group))
		self.play(FadeOut(add_arrow_group), FadeOut(squared_dot), run_time=0.5)
		start_num.set_value(start_num.get_value()**2 + c.get_value())
		self.wait(0.5)

		# Show remaining demonstration series steps (duration: 18)
		step_2_dot = Dot(get_squared_added_point())
		step_2_dot.add_updater(lambda d: d.move_to(num_to_point(c.get_value()**2 + c.get_value())))
		animate_steps_to_dot(step_2_dot)
		step_3_dot = Dot(get_squared_added_point())
		step_3_dot.add_updater(lambda d: d.move_to(num_to_point(
			(c.get_value()**2 + c.get_value())**2 + c.get_value()
		)))
		animate_steps_to_dot(step_3_dot)
		step_4_dot = Dot(get_squared_added_point())
		step_4_dot.add_updater(lambda d: d.move_to(num_to_point(
			((c.get_value()**2 + c.get_value())**2 + c.get_value())**2 + c.get_value()
		)))
		animate_steps_to_dot(step_4_dot)

		vector_0_1 = Arrow(start=axes.get_origin(), end=c_dot.get_center(), buff=0)
		vector_0_1.add_updater(lambda v: v.become(Arrow(start=axes.get_origin(), end=c_dot.get_center(), buff=0)))
		vector_1_2 = Arrow(start=c_dot.get_center(), end=step_2_dot.get_center(), buff=0)
		vector_1_2.add_updater(lambda v: v.become(Arrow(start=c_dot.get_center(), end=step_2_dot.get_center(), buff=0)))
		vector_2_3 = Arrow(start=step_2_dot.get_center(), end=step_3_dot.get_center(), buff=0)
		vector_2_3.add_updater(lambda v: v.become(Arrow(start=step_2_dot.get_center(), end=step_3_dot.get_center(), buff=0)))
		vector_3_4 = Arrow(start=step_3_dot.get_center(), end=step_4_dot.get_center(), buff=0)
		vector_3_4.add_updater(lambda v: v.become(Arrow(start=step_3_dot.get_center(), end=step_4_dot.get_center(), buff=0)))
		
		self.play(Create(vector_0_1))
		self.play(Create(vector_1_2))
		self.play(Create(vector_2_3))
		self.play(Create(vector_3_4))

		self.wait(0.5)

		# Move c around  (duration: 2.5)
		self.play(c.animate.set_value(complex(-0.2, 0.2)))
		self.play(c.animate.set_value(complex(-1, -1)))
		self.play(c.animate.set_value(complex(0.5, 0.1)))
		self.wait(0.5)

		# Center series definition (duration: 2)
		self.play(
			Uncreate(axes),
			Unwrite(axis_labels),
			Unwrite(z_0_eq_0_tex),
			Uncreate(c_dot),
			Unwrite(c_dot_label),
			Uncreate(step_2_dot),
			Uncreate(step_3_dot),
			Uncreate(step_4_dot),
			Uncreate(vector_0_1),
			Uncreate(vector_1_2),
			Uncreate(vector_2_3),
			Uncreate(vector_3_4),
			run_time=0.5
		)
		self.play(series_def.animate.move_to(ORIGIN))
		self.wait(0.5)

		# Prepare demonstration of algorithm (duration: 3.5)
		self.play(series_def.animate.align_on_border(UP, buff=SMALL_BUFF))
		c_eq_1_tex = MathTex("{{c}} = 1")
		c_eq_1_tex.set_color_by_tex("c", GREEN)
		c_eq_1_tex.next_to(series_def, DOWN)
		self.play(Write(c_eq_1_tex))
		self.wait(0.5)

		algorithm_step_0 = MathTex("0")
		algorithm_step_1_0 = MathTex("0", "^2")
		algorithm_step_1_1 = MathTex("0")
		algorithm_step_2_0 = MathTex("0", "+", "1")
		algorithm_step_2_0.set_color_by_tex("1", GREEN)
		algorithm_step_2_1 = MathTex("1")
		algorithm_step_3_0 = MathTex("1", "^2")
		algorithm_step_3_1 = MathTex("1")
		algorithm_step_4_0 = MathTex("1", "+", "1\\relax")
		algorithm_step_4_0.set_color_by_tex("1\\relax", GREEN)
		algorithm_step_4_1 = MathTex("2")
		algorithm_step_5_0 = MathTex("2", "^2")
		algorithm_step_5_1 = MathTex("4")
		algorithm_step_6_0 = MathTex("4", "+", "1")
		algorithm_step_6_0.set_color_by_tex("1", GREEN)
		algorithm_step_6_1 = MathTex("5")
		algorithm_step_7_0 = MathTex("5", "^2")
		algorithm_step_7_1 = MathTex("25")
		algorithm_step_8_0 = MathTex("25", "+", "1")
		algorithm_step_8_0.set_color_by_tex("1", GREEN)
		algorithm_step_8_1 = MathTex("26")

		# Start with 0 (duration: 1.5)
		self.play(Write(algorithm_step_0))
		self.wait(0.5)

		# Square (duration: 2.5)
		self.play(TransformMatchingTex(algorithm_step_0, algorithm_step_1_0))
		self.play(TransformMatchingTex(algorithm_step_1_0, algorithm_step_1_1))
		self.wait(0.5)

		# Add 1 (duration: 2.5)
		self.play(TransformMatchingTex(algorithm_step_1_1, algorithm_step_2_0))
		self.play(TransformMatchingTex(algorithm_step_2_0, algorithm_step_2_1))
		self.wait(0.5)

		# Continue algorithm (duration: 15)
		self.play(TransformMatchingTex(algorithm_step_2_1, algorithm_step_3_0))
		self.play(TransformMatchingTex(algorithm_step_3_0, algorithm_step_3_1))
		self.wait(0.5)
		self.play(TransformMatchingTex(algorithm_step_3_1, algorithm_step_4_0))
		self.play(TransformMatchingTex(algorithm_step_4_0, algorithm_step_4_1))
		self.wait(0.5)
		self.play(TransformMatchingTex(algorithm_step_4_1, algorithm_step_5_0))
		self.play(TransformMatchingTex(algorithm_step_5_0, algorithm_step_5_1))
		self.wait(0.5)
		self.play(TransformMatchingTex(algorithm_step_5_1, algorithm_step_6_0))
		self.play(TransformMatchingTex(algorithm_step_6_0, algorithm_step_6_1))
		self.wait(0.5)
		self.play(TransformMatchingTex(algorithm_step_6_1, algorithm_step_7_0))
		self.play(TransformMatchingTex(algorithm_step_7_0, algorithm_step_7_1))
		self.wait(0.5)
		self.play(TransformMatchingTex(algorithm_step_7_1, algorithm_step_8_0))
		self.play(TransformMatchingTex(algorithm_step_8_0, algorithm_step_8_1))
		self.wait(0.5)

		# Prepare complex algorithm demonstration (duration: 1.5)
		c_eq_1_plus_i_tex = MathTex("{{c}} = 1", "+ i")
		c_eq_1_plus_i_tex.set_color_by_tex("c", GREEN)
		c_eq_1_plus_i_tex.match_y(c_eq_1_tex)
		self.play(Unwrite(algorithm_step_8_1, run_time=0.5), TransformMatchingTex(c_eq_1_tex, c_eq_1_plus_i_tex), run_time=1)
		self.wait(0.5)

		cmpx_algorithm_step_0 = MathTex("0")
		cmpx_algorithm_step_1_0 = MathTex("0", "^2")
		cmpx_algorithm_step_1_1 = MathTex("0")
		cmpx_algorithm_step_2_0 = MathTex("0", "+", "1", "+\\relax", "i")
		cmpx_algorithm_step_2_0.set_color_by_tex("1", GREEN).set_color_by_tex("+\\relax", GREEN).set_color_by_tex("i", GREEN)
		cmpx_algorithm_step_2_1 = MathTex("1", "+", "i")
		cmpx_algorithm_step_3_0 = MathTex("(", "1", "+", "i", ")", "^2")
		cmpx_algorithm_step_3_1 = MathTex("(", "1", "+", "i", ")", "(", "1", "+", "i", ")")
		cmpx_algorithm_step_3_2 = MathTex("1", "\\cdot", "1", "+", "1", "\\cdot", "i", "+", "i", "\\cdot", "1", "+", "i", "^2")
		cmpx_algorithm_step_3_3 = MathTex("2", "i")
		cmpx_algorithm_step_4_0 = MathTex("2", "i", "+", "1", "+\\relax", "i\\relax")
		cmpx_algorithm_step_4_0.set_color_by_tex("1", GREEN).set_color_by_tex("+\\relax", GREEN).set_color_by_tex("i\\relax", GREEN)
		cmpx_algorithm_step_4_1 = MathTex("1", "+", "3", "i")
		ellipsis = Tex("...")

		# Start with 0 (duration: 1.5)
		self.play(Write(cmpx_algorithm_step_0))
		self.wait(0.5)

		# Square (duration: 2.5)
		self.play(TransformMatchingTex(cmpx_algorithm_step_0, cmpx_algorithm_step_1_0))
		self.play(TransformMatchingTex(cmpx_algorithm_step_1_0, cmpx_algorithm_step_1_1))
		self.wait(0.5)

		# Add c (duration: 2.5)
		self.play(TransformMatchingTex(cmpx_algorithm_step_1_1, cmpx_algorithm_step_2_0))
		self.play(TransformMatchingTex(cmpx_algorithm_step_2_0, cmpx_algorithm_step_2_1))
		self.wait(0.5)

		# Square (duration: 1.5)
		self.play(TransformMatchingTex(cmpx_algorithm_step_2_1, cmpx_algorithm_step_3_0))
		self.wait(0.5)

		# Expand bracket (duration: 1.5)
		self.play(TransformMatchingTex(cmpx_algorithm_step_3_0, cmpx_algorithm_step_3_1))
		self.wait(0.5)

		# Multiply out (duartion: 2.5)
		self.play(TransformMatchingTex(cmpx_algorithm_step_3_1, cmpx_algorithm_step_3_2))
		self.play(TransformMatchingTex(cmpx_algorithm_step_3_2, cmpx_algorithm_step_3_3))
		self.wait(0.5)

		# Add c again (duration: 2.5)
		self.play(TransformMatchingTex(cmpx_algorithm_step_3_3, cmpx_algorithm_step_4_0))
		self.play(TransformMatchingTex(cmpx_algorithm_step_4_0, cmpx_algorithm_step_4_1))
		self.wait(0.5)

		# Add ellipsis (duration: till end)
		ellipsis.next_to(cmpx_algorithm_step_4_1, DOWN)
		self.play(Write(ellipsis))
		self.wait(0.5)