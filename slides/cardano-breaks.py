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
				"number_to_include": np.arange(-4, 4, 2)
			},
			y_axis_config={
				"numbers_to_include": np.arange(-2, 10, 4)
			}
		)
		axes.align_on_border(RIGHT, buff=SMALL_BUFF)
		axis_labels = axes.get_axis_labels()
		counter_example_graph = axes.get_graph(lambda x: x** - 6*x + 4)
		root_dots = [
			Dot(axes.coords_to_point(-2.73, 0), color=YELLOW),
			Dot(axes.coords_to_point(0.73, 0), color=YELLOW),
			Dot(axes.coords_to_point(2, 0), color=YELLOW)
		]
		counter_example_graph_label = axes.get_graph_label(counter_example_graph, "g")
		counter_example = MathTex("g(x) = x^3 {{-6}}x + 4")
		counter_example.set_color_by_tex("-6", RED)
		counter_example.set_color_by_tex("4", BLUE)
		counter_example.align_on_border(UP + RIGHT, buff=SMALL_BUFF)
		self.play()