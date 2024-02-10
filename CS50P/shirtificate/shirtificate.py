from fpdf import FPDF


class PDF(FPDF):
	def __init__(self, name):
		super().__init__()
		self.add_page()
		self.set_font("helvetica", "B", 50)
		self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
		self.image("shirtificate.png", w=self.epw)
		self.set_font_size(25)
		self.set_text_color(255, 255, 255)
		self.cell(0, -240, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")

name = input("Name: ")
pdf = PDF(name)
pdf.output("shirtificate.pdf")