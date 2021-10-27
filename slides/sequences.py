from manim import *;

class Sequences(Scene):
	def construct(self):
		axes = Axes(
			x_range=[-12, 12, 1],
			y_range=[-6, 6, 1],
			x_length=8,
			y_length=4
		)
		axis_labels = axes.get_axis_labels(Tex("Re"), Tex("Im"))
		z_0 = ComplexValueTracker(complex(1, 1))
		def num_to_point(num: complex):
			return axes.coords_to_point(num.real, num.imag)
		z_0_dot = Dot(num_to_point(z_0.get_value()), color=RED)
		z_0_dot.add_updater(lambda d: d.move_to(num_to_point(z_0)))
		z_0_label = MathTex("z", color=RED)
		z_0_label.scale(0.7).next_to(z_0_dot, UR, buff=SMALL_BUFF)
		z_0_label.add_updater(lambda l: l.next_to(z_0_dot, UR, buff=SMALL_BUFF))
		
		self.play(Create(axes), Write(axis_labels), Create(z_0_dot), Write(z_0_label))
		self.wait(0.5)

		function_def = MathTex("f({{z}}) = {{z}}^2")
		function_def.set_color_by_tex("z", RED)
		function_def.align_on_border(UL)
		self.play(Write(function_def))
		self.wait(0.5)

		z_1_dot = Dot(num_to_point(z_0.get_value()**2))
		z_1_dot.add_updater(lambda d: d.move_to(num_to_point(z_0.get_value())))

		z_2_dot = Dot(num_to_point(z_0.get_value()**3))
		z_2_dot.add_updater(lambda d: d.move_to(num_to_point(z_0.get_value())))

		z_3_dot = Dot(num_to_point(z_0.get_value()**4))
		z_3_dot.add_updater(lambda d: d.move_to(num_to_point(z_0.get_value())))

		vector_0_1 = Arrow(start=z_0_dot, end=z_1_dot)

		self.wait()
