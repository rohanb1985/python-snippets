from fpdf import FPDF

pdf = FPDF(unit = "pt", format = [2200, 3400])

counter = 1
while (counter < 16):
	pdf.add_page()
	pdf.image("page" + str(counter) + ".jpg", 0, 0)	
	counter += 1

pdf.output("Epaper.pdf", "F")

	
	
	
	