from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", format="A4", unit="mm")

df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=0, h=12, border=0, align='l', ln=1, txt= row["Topic"])
    pdf.line(10,21,200,21)
    

pdf.output("output.pdf")

