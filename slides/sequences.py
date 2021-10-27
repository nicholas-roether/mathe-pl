from manim import *
from manim.mobject.geometry import ArrowTriangleFilledTip, ArrowTriangleTip;

def argument(z: complex):
	return np.arctan(z.imag / z.real)

class Sequences(Scene):
	MAX_RADIUS = 20

	def compute_curve_at_t(self, z_0, t):
		z_abs = abs(z_0)
		z_arg = argument(z_0)
		if (z_arg == 0): return [(self.MAX_RADIUS - 1) * t + 1, 0]
		r = min(pow(z_abs, t / z_arg), self.MAX_RADIUS)
		arr = np.array([r * np.cos(t), r * np.sin(t)])
		return arr

	def construct(self):
		axes = Axes(
			x_range=[-12, 12, 1],
			y_range=[-6, 6, 1],
			x_length=8,
			y_length=4
		)
		axis_labels = axes.get_axis_labels(Tex("Re"), Tex("Im"))
		z_0 = ComplexValueTracker(complex(1, 0.6))
		
		def get_z_0(): return z_0.get_value()
		def get_z_1(): return get_z_0()**2
		def get_z_2(): return get_z_0()**4
		def get_z_3(): return get_z_0()**8
		def get_z_4(): return get_z_0()**16

		def num_to_point(num: complex):
			return axes.coords_to_point(num.real, num.imag)
		z_0_dot = Dot(num_to_point(get_z_0()), color=RED)
		z_0_dot.add_updater(lambda d: d.move_to(num_to_point(get_z_0())))
		z_0_label = MathTex("z_0", color=RED)
		z_0_label.scale(0.7).next_to(z_0_dot, UR, buff=SMALL_BUFF)
		z_0_label.add_updater(lambda l: l.next_to(z_0_dot, UR, buff=SMALL_BUFF))
		
		# Show plot (duration: 1.5)
		self.play(Create(axes), Write(axis_labels), Create(z_0_dot), Write(z_0_label))
		self.wait(0.5)

		# Show function (duration: 1.5)
		function_def = MathTex("{{f}}({{z}}) = {{z}}^2")
		function_def.set_color_by_tex("f", YELLOW)
		function_def.set_color_by_tex("z", RED)
		function_def.align_on_border(UL, buff=SMALL_BUFF)
		self.play(Write(function_def))
		self.wait(0.5)

		# Show square sequence (duration: 8.5)
		z_1_dot = Dot(num_to_point(get_z_1()))
		z_1_dot.add_updater(lambda d: d.move_to(num_to_point(get_z_1())))

		z_2_dot = Dot(num_to_point(get_z_2()))
		z_2_dot.add_updater(lambda d: d.move_to(num_to_point(get_z_2())))

		z_3_dot = Dot(num_to_point(get_z_3()))
		z_3_dot.add_updater(lambda d: d.move_to(num_to_point(get_z_3())))

		z_4_dot = Dot(num_to_point(get_z_4()))
		z_4_dot.add_updater(lambda d: d.move_to(num_to_point(get_z_4())))

		vector_0_1 = Arrow(start=num_to_point(get_z_0()), end=num_to_point(get_z_1()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)
		vector_0_1.add_updater(lambda v: v.become(Arrow(start=num_to_point(get_z_0()), end=num_to_point(get_z_1()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)))
	
		vector_1_2 = Arrow(start=num_to_point(get_z_1()), end=num_to_point(get_z_2()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)
		vector_1_2.add_updater(lambda v: v.become(Arrow(start=num_to_point(get_z_1()), end=num_to_point(get_z_2()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)))

		vector_2_3 = Arrow(start=num_to_point(get_z_2()), end=num_to_point(get_z_3()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)
		vector_2_3.add_updater(lambda v: v.become(Arrow(start=num_to_point(get_z_2()), end=num_to_point(get_z_3()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)))

		vector_3_4 = Arrow(start=num_to_point(get_z_3()), end=num_to_point(get_z_4()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)
		vector_3_4.add_updater(lambda v: v.become(Arrow(start=num_to_point(get_z_3()), end=num_to_point(get_z_4()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1)))

		self.play(Create(vector_0_1))
		self.play(Create(z_1_dot))
		self.play(Create(vector_1_2))
		self.play(Create(z_2_dot))
		self.play(Create(vector_2_3))
		self.play(Create(z_3_dot))
		self.play(Create(vector_3_4))
		self.play(Create(z_4_dot))
		self.wait(0.5)
		
		# Show curve (duration: 1.5)
		exp_curve = axes.get_parametric_curve(lambda t: self.compute_curve_at_t(get_z_0(), t), t_range=np.array([0, 2 * TAU]), color=BLUE)
		self.play(Create(exp_curve))
		self.wait(0.5)

		# Hide curve (duration: 1)
		self.play(Uncreate(exp_curve), run_time=0.5)
		self.wait(0.5)

		# Move z0 around (duration: 2.5)
		self.play(z_0.animate.set_value(complex(-1, 2)))
		self.play(z_0.animate.set_value(complex(1.5, -1.3)))
		self.wait(0.5)

		# Demonstrate convergence circle (duration: 3.5)
		circle = Circle(axes.get_y_unit_size(), color=GRAY)
		circle.move_to(axes.get_origin())
		circle.set_fill(GRAY, opacity=0.3)
		self.play(DrawBorderThenFill(circle))
		self.play(z_0.animate.set_value(complex(0.3, 0.6)))
		self.wait(0.5)

		# Prepare series definition (duration: 2)
		plot = VGroup(z_0_dot, z_0_label, z_1_dot, z_2_dot, z_3_dot, z_4_dot, axes, axis_labels, circle, vector_0_1, vector_1_2, vector_2_3, vector_3_4)
		self.play(FadeOut(plot), run_time=0.5)

		series_0 = MathTex("z_0").scale(1.5)
		series_1 = MathTex("z_1", "=", "z_0", "^2").scale(1.5)
		series_2 = MathTex("z_2", "=", "z_1", "^2").scale(1.5)
		series_3 = MathTex("z_3", "=", "z_2", "^2").scale(1.5)
		series_4 = MathTex("z_4", "=", "z_3", "^2").scale(1.5)
		series_5 = MathTex("z_5", "=", "z_4", "^2").scale(1.5)
		series_def = MathTex("z_n", "=", "z_{n - 1}", "^2").scale(1.5)
		self.play(Write(series_0))
		self.wait(0.5)
		
		# Show series explanation step 1 (duration: 1.5)
		self.play(TransformMatchingTex(series_0, series_1), run_time=1)
		self.wait(0.5)

		# Work up to series definition (duration: 3.75)
		self.play(TransformMatchingTex(series_1, series_2), run_time=1)
		self.play(TransformMatchingTex(series_2, series_3), run_time=0.5)
		self.play(TransformMatchingTex(series_3, series_4), run_time=0.5)
		self.play(TransformMatchingTex(series_4, series_5), run_time=0.25)
		self.play(ReplacementTransform(series_5, series_def))
		self.wait(0.5)

		# Complete series definition with initial value (duration: 2.5)
		self.play(series_def.animate.shift(UP / 2))

		z_0_def = MathTex("z_0 = {{z\\relax}} \\in \\mathbb{C}")
		z_0_def.set_color_by_tex("z\\relax", RED)
		z_0_def.next_to(series_def, DOWN)
		self.play(Write(z_0_def))
		self.wait(0.5)

		# Transition to z^2 + 1 function screen (duration: 4)
		plus_one_func_def = MathTex("{{f}}({{z}}) = {{z}}^2 {{+}} {{1}}")
		plus_one_func_def.align_on_border(UL, buff=SMALL_BUFF).set_color_by_tex("f", YELLOW).set_color_by_tex("z", RED)
		self.play(Unwrite(series_def), Unwrite(z_0_def), run_time=0.5)
		self.play(FadeIn(axes, axis_labels))
		self.play(TransformMatchingTex(function_def, plus_one_func_def))
		c = ComplexValueTracker(complex(1, 0))

		def get_z_1(): return get_z_0()**2 + c.get_value()
		def get_z_2(): return get_z_1()**2 + c.get_value()
		def get_z_3(): return get_z_2()**2 + c.get_value()
		def get_z_4(): return get_z_3()**2 + c.get_value()

		z_0.set_value(complex(-0.1, 1.4))
		self.play(Create(z_0_dot), Write(z_0_label))
		self.wait(0.5)

		# Demonstrate z^2 + 1 sequence (duration: 8.5)
		vector_0_1.become(Arrow(start=num_to_point(get_z_0()), end=num_to_point(get_z_1()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1))
		vector_1_2.become(Arrow(start=num_to_point(get_z_1()), end=num_to_point(get_z_2()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1))
		vector_2_3.become(Arrow(start=num_to_point(get_z_2()), end=num_to_point(get_z_3()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1))
		vector_3_4.become(Arrow(start=num_to_point(get_z_3()), end=num_to_point(get_z_4()), buff=0, stroke_width=5, color=YELLOW, max_tip_length_to_length_ratio=0.1))

		self.play(Create(vector_0_1))
		self.play(Create(z_1_dot))
		self.play(Create(vector_1_2))
		self.play(Create(z_2_dot))
		self.play(Create(vector_2_3))
		self.play(Create(z_3_dot))
		self.play(Create(vector_3_4))
		self.play(Create(z_4_dot))
		self.wait(0.5)

		# Move z around (duration: 4.5)
		self.play(z_0.animate.set_value(complex(-1, -1)))
		self.play(z_0.animate.set_value(complex(0.3, 0.2)))
		self.play(z_0.animate.set_value(complex(3, 1)))
		self.play(z_0.animate.set_value(complex(-0.4, 1.6)))
		self.wait(0.5)

		# Introduce c variable (duration: 1.5)
		c_dot = Dot(num_to_point(c.get_value()), color=GREEN)
		c_dot.add_updater(lambda d: d.move_to(num_to_point(c.get_value())))
		plus_c_func_def = MathTex("{{f}}({{z}}) = {{z}}^2 {{+}} {{c}}")
		plus_c_func_def.align_on_border(UL, buff=SMALL_BUFF).set_color_by_tex("f", YELLOW).set_color_by_tex("z", RED).set_color_by_tex("c", GREEN)
		self.play(TransformMatchingTex(plus_one_func_def, plus_c_func_def), Create(c_dot))
		self.wait(0.5)

		# Move c around (duration: 3.5)
		self.play(c.animate.set_value(complex(1.5, 1.5)))
		self.play(c.animate.set_value(complex(-3, -1.2)))
		self.play(c.animate.set_value(complex(-0.9, 3)))
		self.wait(0.5)

		# Add z^2 + 1 series definition (duration: 1.5)
		plus_c_series_def = MathTex("z_n = z_{n-1}^2 + {{c}}")
		plus_c_series_def.set_color_by_tex("c", GREEN)
		plus_c_series_def_additional = MathTex("{{z_0}}, {{c}} \\in \\mathbb{C}")
		plus_c_series_def_additional.set_color_by_tex("c", GREEN).set_color_by_tex("z_0", RED)
		plus_c_series_def.align_on_border(UR, buff=SMALL_BUFF)
		plus_c_series_def_additional.next_to(plus_c_series_def, DOWN, aligned_edge=RIGHT, buff=SMALL_BUFF)
		self.play(Write(plus_c_series_def))
		self.wait(0.5)

		# Add z^2 + 1 series definition additional stuff (duration: till end)
		self.play(Write(plus_c_series_def_additional))
		self.wait(0.5)
