from docx import Document
from docx.shared import Pt

def change_text_style(files_list):
    for file_name in files_list:
        document = Document('Table/' + file_name)
        
files_to_change = ['1.docx', '2.docx', '3.docx', '4.docx', '5.docx']
change_text_style(files_to_change)