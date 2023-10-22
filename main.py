from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", format="A4", unit="mm")
df = pd.read_csv('topics.csv')

"""
Below is a class to create a footer component
that is created at every page addition
"""

class PDFWithPageNumber(FPDF):
    def footer(self):
        self.set_y(-1 * self.l_margin)
        self.set_font('Arial', 'I', 12)
        page_number = 'Page %s' % self.page_no()
        self.cell(0, 10, page_number, 0, 0, 'C')
    
pdf = PDFWithPageNumber()

for index, row in df.iterrows():
    #header
    
    pdf.add_page()
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.set_font(family='Times', style='B', size=18)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, border=0, align='L', ln=1, txt= row["Topic"])
    pdf.line(10,21,200,21)
    
    #footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, border=0, align='R',txt=row['Topic'])
    
    
    
    
    for i in range(row['Pages']-1):
        # footer
        pdf.add_page()
        pdf.ln(273)
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10, border=0, align='R',txt=row['Topic'])
        
    
        
    

pdf.output("output.pdf")

