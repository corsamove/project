from docx import Document
from docx.shared import Pt

def change_text_style(files_list):
    for file_name in files_list:
        document = Document(file_name)
        for paragraph in document.paragraphs:
            paragraph.style.font.name = 'Times New Roman'
            paragraph.style.font.size = Pt(14)
            paragraph.style.paragraph_format.line_spacing = 1.5 
        document.save(file_name + 'restyled.docx')
