from math import inf, isinf, isnan, log
from manim import *

def argument(z: complex):
	return np.arctan(z.imag / z.real)

class Exponents(Scene):
	_apply_limit = True
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
			x_range=[-8, 8, 1],
			y_range=[-4, 4, 1],
			x_length=8,
			y_length=4,
		)
		axis_labels = axes.get_axis_labels(Tex("Re"), Tex("Im"))
		z_0 = ComplexValueTracker(value=complex(0.7, 1.2))
		def num_to_point(z: complex):
			return axes.coords_to_point(z.real, z.imag)

		z_0_dot = Dot(num_to_point(z_0.get_value()), color=RED)
		z_0_dot.add_updater(lambda z: z.move_to(num_to_point(z_0.get_value())))
		z_1_dot = Dot(num_to_point(z_0.get_value()**2))
		z_1_dot.add_updater(lambda z: z.move_to(num_to_point(z_0.get_value()**2)))
		z_2_dot = Dot(num_to_point(z_0.get_value()**3))
		z_2_dot.add_updater(lambda z: z.move_to(num_to_point(z_0.get_value()**3)))
		z_3_dot = Dot(num_to_point(z_0.get_value()**4))
		z_3_dot.add_updater(lambda z: z.move_to(num_to_point(z_0.get_value()**4)))

		z_0_label = MathTex("z", color=RED)
		z_0_label.next_to(z_0_dot, UR, buff=SMALL_BUFF).add_updater(lambda l: l.next_to(z_0_dot, UR, buff=SMALL_BUFF))
		z_1_label = MathTex("z^2")
		z_1_label.next_to(z_1_dot, UR, buff=SMALL_BUFF).add_updater(lambda l: l.next_to(z_1_dot, UR, buff=SMALL_BUFF))
		z_2_label = MathTex("z^3")
		z_2_label.next_to(z_2_dot, UR, buff=SMALL_BUFF).add_updater(lambda l: l.next_to(z_2_dot, UR, buff=SMALL_BUFF))
		z_3_label = MathTex("z^4")
		z_3_label.next_to(z_3_dot, UR, buff=SMALL_BUFF).add_updater(lambda l: l.next_to(z_3_dot, UR, buff=SMALL_BUFF))

		exp_curve = axes.get_parametric_curve(lambda t: self.compute_curve_at_t(z_0.get_value(), t), t_range=np.array([0, 2 * TAU]), color=BLUE)
		exp_curve.add_updater(lambda c: c.become(axes.get_parametric_curve(lambda t: self.compute_curve_at_t(z_0.get_value(), t), t_range=np.array([0, 2 *  TAU]), color=BLUE)))

		# Initial setup (duration: 2.5)
		self.play(
			Create(axes),
			Write(axis_labels)
		)
		self.play(Create(z_0_dot), Write(z_0_label))
		self.wait(0.5)

		# Draw exponents (duration: 3.5)
		self.play(Create(z_1_dot), Write(z_1_label))
		self.play(Create(z_2_dot), Write(z_2_label))
		self.play(Create(z_3_dot), Write(z_3_label))
		self.wait(0.5)

		# Draw curve (duration: 1.5)
		self.play(Create(exp_curve))
		self.wait(0.5)

		# Move curve around (duration: 2.5)
		self.play(z_0.animate.set_value(complex(1, 2)))
		self.play(z_0.animate.set_value(complex(2, 1)))
		self.wait(0.5)

		# Move curve on real axis (duration: 1.5)
		self.play(z_0.animate.set_value(complex(2, 0)))
		self.wait(0.5)

		# Move curve back (duration: 1.5)
		self.play(z_0.animate.set_value(complex(2, 1)))
		self.wait(0.5)
		
		# Draw central circle and move z into it (duration: till end)
		circle = Circle(axes.get_y_unit_size(), color=GRAY)
		circle.move_to(axes.get_origin())
		circle.set_fill(GRAY, opacity=0.3)
		self.play(DrawBorderThenFill(circle))
		self._apply_limit = False
		self.play(z_0.animate.set_value(complex(0.6, 0.6)))
		self.wait(0.5)