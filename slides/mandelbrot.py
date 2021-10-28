from manim import *;

config.pixel_width = 1920
config.frame_height = 6
config.background_color=WHITE

class Mandelbrot(Scene):
	def construct(self):
		axes = Axes(
			x_range=[-2.3, 2.3, 1],
			y_range=[-1.5, 1.5, 1],
			x_length=9.2,
			y_length=6,
			x_axis_config={
				"color": GRAY_C,
				"include_numbers": True,
				"decimal_number_config": {
					"color": GRAY_C
				}
			},
			y_axis_config={
				"color": GRAY_C,
				"include_numbers": True,
				"decimal_number_config": {
					"color": GRAY_C
				}
			}
		)
		series_def = MathTex("z_n = z_{n-1}^2 + {{c}} \\\\ z_0 = 0", color=GRAY_E)
		series_def.set_color_by_tex("c", GREEN)
		c_num = ComplexValueTracker(complex(1, 1))
		c_dot = Dot(axes.coords_to_point(c_num.get_value().real, c_num.get_value().imag), color=GREEN)
		c_dot.add_updater(lambda d: d.move_to(axes.coords_to_point(c_num.get_value().real, c_num.get_value().imag)))
		c_label = MathTex("c", color=GREEN)
		c_label.next_to(c_dot, UR, buff=SMALL_BUFF).add_updater(lambda l: l.next_to(c_dot, UR, buff=SMALL_BUFF))
		
		self.play(Write(series_def))
		self.wait(0.5)

		self.play(
			series_def.animate.align_on_border(UL, buff=SMALL_BUFF),
			Create(axes)
		)
		self.wait()

		self.play(Create(c_dot), Write(c_label))
		self.play(c_num.animate.set_value(complex(-0.3, 0.6)))
		self.play(c_num.animate.set_value(complex(-0.7, -0.1)))
		self.play(c_num.animate.set_value(complex(1.3, 0.1)))
		self.wait(0.5)

		self.play(Uncreate(c_dot), Unwrite(c_label))
		self.wait(0.5)

		x_range = MathTex("x \\in [-2; \\frac{1}{4}]", color=GRAY_E)
		x_range.align_on_border(UR, buff=SMALL_BUFF)
		black_line = Line(axes.coords_to_point(-2, 0), axes.coords_to_point(0.25, 0), color=BLACK)
		self.play(Create(black_line), Write(x_range))
		self.wait(0.5)

		plot = VGroup(axes, black_line)
		self.play(Unwrite(series_def), Unwrite(x_range), plot.animate.scale(1.2))
		self.play(plot.animate.shift(RIGHT))