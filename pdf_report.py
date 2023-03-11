from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        # Logo
        #self.image('logo_pb.png', 10, 8, 33)
        # helvetica bold 15
        self.set_font('helvetica', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title','C')
        # Line break
        self.ln(20)


data = (
    ("Product Name", "Quantity", "Amount"),
    ("Mobile", "1", "3500"),
    
)
h = "wer"
g = "Werwer"
df="werwer"
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=10)
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 4  # distribute content evenly
pdf.cell(40, 10, '**TO**',ln=1,markdown=True)
pdf.cell(50, 10, f'Name : {h} ',ln=1)
pdf.cell(60, 10, f'Email : {g} ',ln=1)
pdf.cell(70, 10, f'Invoice Id : {df} ',ln=1)
for row in data:
    for datum in row:
        pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
    pdf.ln(line_height)
pdf.output('1.pdf')
