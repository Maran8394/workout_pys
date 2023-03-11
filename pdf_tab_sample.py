from fpdf import FPDF

data = {
            ('Name','email','Invoice id','Product Name','Quantity','Amount'),
            ('Maran','maran@gmail.com','Inv_089923jhdd','Mobil','1','6500')
        }
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica",size=10)
line_height = pdf.font_size*2.5
col_width = pdf.epw /4
for row in data:
    for dataum in row:
        pdf.multi_cell(col_width,line_height,dataum,border=1, ln=3, max_line_height=pdf.font_size)
    pdf.ln(line_height)
pdf.output("t.pdf")
