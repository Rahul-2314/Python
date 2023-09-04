from PyPDF2 import PdfWriter, PdfReader
import os

merger = PdfWriter()
dir = "C:/Users/chowd/Desktop/Python/programs/pdf_merger/pdf"
files = [file for file in os.listdir(dir) if file.endswith(".pdf")]

for pdf in files:
    pdf_path = os.path.join(dir, pdf)
    pdf_reader = PdfReader(pdf_path)
    merger.append(pdf_reader)

output_pdf_path = os.path.join(dir, "merged-pdf.pdf")
merger.write(output_pdf_path)
merger.close()

print("\nPDF files merged successfully!")
