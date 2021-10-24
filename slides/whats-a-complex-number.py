from manim import *
	

class WhatsAComplexNumber(Scene):
	def construct(self):
		# Show sqrt(-1)
		sqrt_neg_1 = MathTex("\\sqrt{", "-1", "}")
		sqrt_neg_1.scale(1.5)
		self.play(Write(sqrt_neg_1))
		self.wait(0.5)

		# show i
		self.play(sqrt_neg_1.animate.scale(1 / 1.5))
		i_sqrt_def = MathTex("i", "=", "\\sqrt{", "-1", "}")
		self.play(TransformMatchingTex(sqrt_neg_1, i_sqrt_def))
		self.wait(0.5)

		# show i definition
		i_definition = MathTex("i", "^2", "=", "-1")
		self.play(TransformMatchingTex(i_sqrt_def, i_definition))
		self.wait(0.5)

		# show i usage example
		self.play(i_definition.animate.align_on_border(UP))
		i_example = MathTex("\\sqrt{-4}")
		self.play(Write(i_example))
		self.wait(0.5)

		# reduce i usage example
		i_example_step_1 = MathTex("\\sqrt{-4}", "=", "\\sqrt{-", "4}")
		self.play(TransformMatchingTex(i_example, i_example_step_1))

		i_example_step_2 = MathTex("\\sqrt{-4}", "=", "\\sqrt{", "4}", "\\sqrt{-", "1}")
		self.play(TransformMatchingTex(i_example_step_1, i_example_step_2))

		i_example_step_3 = MathTex("\\sqrt{-4}", "=", "\\sqrt{", "4}", "i")
		self.play(TransformMatchingTex(i_example_step_2, i_example_step_3))

		i_example_final = MathTex("\\sqrt{-4}", "=", "2", "i")
		self.play(TransformMatchingTex(i_example_step_3, i_example_final))
		self.wait(0.5)

		# prepare complex number definition
		self.play(Unwrite(i_example_final), run_time=0.5)
		z_eq_tex = MathTex("z", "=")
		i_tex = MathTex("i")
		i_tex.next_to(z_eq_tex, aligned_edge=DOWN)
		z_eq_i_tex = VGroup(z_eq_tex, i_tex)
		z_eq_i_tex.move_to(ORIGIN)
		z_eq_i_tex.shift(RIGHT * i_definition[2].get_x() - z_eq_tex[1].get_x())
		self.play(Write(z_eq_i_tex))

		# show imaginary part
		imag_decimal = DecimalNumber(
			0,
			num_decimal_places=2,
		)
		imag_dec_value = ValueTracker(0)
		imag_decimal.add_updater(lambda dec: dec.set_value(imag_dec_value.get_value()))
		imag_decimal.set_color(BLUE)
		imag_decimal.next_to(z_eq_tex, aligned_edge=DOWN)
		self.play(i_tex.animate.next_to(imag_decimal))
		self.play(Write(imag_decimal), run_time=0.5)
		self.play(imag_dec_value.animate.set_value(9.5), run_time=1.5)
		self.play(imag_dec_value.animate.set_value(1.4), run_time=1.5)

		imag_part = MathTex("b\\relax", "i")
		self.color_vars(imag_part)
		imag_part.next_to(z_eq_tex, aligned_edge=DOWN)
		self.play(FadeOut(imag_decimal, run_time=0.2), TransformMatchingTex(i_tex, imag_part))
		self.wait(0.5)

		# show real part
		real_decimal = DecimalNumber(
			0,
			num_decimal_places=2,
		)
		real_dec_value = ValueTracker(0)
		real_decimal.add_updater(lambda dec: dec.set_value(real_dec_value.get_value()))
		real_decimal.set_color(RED)
		real_decimal.next_to(z_eq_tex, aligned_edge=DOWN)

		plus_imag_part = MathTex("+", "b\\relax", "i")
		self.color_vars(plus_imag_part)
		plus_imag_part.next_to(real_decimal, aligned_edge=DOWN)
		self.play(TransformMatchingTex(imag_part, plus_imag_part))
		self.play(Write(real_decimal), run_time=0.5)
		self.play(real_dec_value.animate.set_value(9.5), run_time=1.5)
		self.play(real_dec_value.animate.set_value(1.4), run_time=1.5)

		complex_number_tex = MathTex("a\\relax", "+", "b\\relax", "i")
		self.color_vars(complex_number_tex)
		complex_number_tex.next_to(z_eq_tex, aligned_edge=DOWN)
		self.play(FadeOut(real_decimal, run_time=0.2), TransformMatchingTex(plus_imag_part, complex_number_tex))
		complex_number_def = VGroup(z_eq_tex, complex_number_tex)
		self.play(complex_number_def.animate.move_to(ORIGIN))
		self.wait(0.5)

		# show complex number set symbol
		complex_number_def_set = MathTex("z", "=", "a\\relax", "+", "b\\relax", "i", "\\in", "\\mathbb{C}")
		self.color_vars(complex_number_def_set)
		self.play(FadeOut(z_eq_tex, run_time=0.2), TransformMatchingTex(complex_number_tex, complex_number_def_set))
		self.wait(0.5)

		# Show real and imaginary parts
		self.play(Unwrite(i_definition), run_time=0.5)
		self.play(complex_number_def_set.animate.align_on_border(UP))

		real_part_text = Tex("Realteil:")
		imag_part_text = Tex("Imaginärteil:")
		imag_part_text.next_to(real_part_text, DOWN, aligned_edge=LEFT)
		real_imag_texts = VGroup(real_part_text, imag_part_text)

		real_part_maths = MathTex("\\mathrm{Re}(z) = {{a\\relax}}")
		imag_part_maths = MathTex("\\mathrm{Im}(z) = {{b\\relax}}")
		self.color_vars(real_part_maths, imag_part_maths)
		imag_part_maths.next_to(real_part_maths, DOWN, aligned_edge=LEFT)
		real_imag_maths = VGroup(real_part_maths, imag_part_maths)
		real_imag_maths.next_to(real_imag_texts, aligned_edge=DOWN)

		real_imag_part_explanation = VGroup(real_imag_texts, real_imag_maths)
		real_imag_part_explanation.move_to(ORIGIN)

		self.play(Write(real_imag_part_explanation))
		self.wait(0.5)

		# prepare arithmetic demonstration
		self.play(Unwrite(complex_number_def_set), Unwrite(real_imag_part_explanation), run_time=0.5)
		addition = MathTex("({{a\\relax}} + {{b\\relax}}i) + ({{c\\relax}} + {{d\\relax}}i)")
		subtraction = MathTex("({{a\\relax}} + {{b\\relax}}i) - ({{c\\relax}} + {{d\\relax}}i)")
		multiplication = MathTex("({{a\\relax}} + {{b\\relax}}i) \\cdot ({{c\\relax}} + {{d\\relax}}i)")
		division = MathTex("({{a\\relax}} + {{b\\relax}}i) \\divisionsymbol ({{c\\relax}} + {{d\\relax}}i)")
		self.color_vars(addition, subtraction, multiplication, division)
		
		subtraction.next_to(addition, DOWN, aligned_edge=LEFT)
		multiplication.next_to(subtraction, DOWN, aligned_edge=LEFT)
		division.next_to(multiplication, DOWN, aligned_edge=LEFT)
		demonstrations = VGroup(addition, subtraction, multiplication, division)
		demonstrations.scale(0.85)
		demonstrations.align_on_border(LEFT)
		demonstrations.set_y(0)
		self.play(Write(demonstrations))
		self.wait(0.5)

		# demonstrate arithmetic
		addition_sol = MathTex(*addition.tex_strings, "= ({{a\\relax}} + {{c\\relax}}) + ({{b\\relax}} + {{d\\relax}})i")
		subtraction_sol = MathTex(*subtraction.tex_strings, "= ({{a\\relax}} - {{c\\relax}}) + ({{b\\relax}} - {{d\\relax}})i")
		multiplication_sol = MathTex(*multiplication.tex_strings, "= ({{a\\relax}}{{c\\relax}} - {{b\\relax}}{{d\\relax}}) + ({{a\\relax}}{{d\\relax}} + {{b\\relax}}{{c\\relax}})i")
		division_sol = MathTex(*division.tex_strings, "= \\frac{1}{ {{c\\relax}}^2 + {{d\\relax}}^2 }",
		"(({{b\\relax}}{{d\\relax}} + {{a\\relax}}{{c\\relax}}) + ({{b\\relax}}{{c\\relax}} - {{a\\relax}}{{d\\relax}})i)")
		self.color_vars(addition_sol, subtraction_sol, multiplication_sol, division_sol)

		subtraction_sol.next_to(addition_sol, DOWN, aligned_edge=LEFT)
		multiplication_sol.next_to(subtraction_sol, DOWN, aligned_edge=LEFT)
		division_sol.next_to(multiplication_sol, DOWN, aligned_edge=LEFT)
		solutions = VGroup(addition_sol, subtraction_sol, multiplication_sol, division_sol)
		solutions.scale(0.85)
		solutions.align_on_border(LEFT)
		solutions.set_y(0)
		self.play(
			TransformMatchingTex(addition, addition_sol),
			TransformMatchingTex(subtraction, subtraction_sol),
			TransformMatchingTex(multiplication, multiplication_sol),
			TransformMatchingTex(division, division_sol)
		)
		self.wait(0.5)

		self.wait()

	def color_vars(self, *texs: MathTex):
		for tex in texs:
			tex.set_color_by_tex("a\\relax", RED)
			tex.set_color_by_tex("b\\relax", BLUE)
			tex.set_color_by_tex("c\\relax", YELLOW)
			tex.set_color_by_tex("d\\relax", GREEN)