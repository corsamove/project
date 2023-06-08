from docx import Document
from docx.shared import Pt 
from function import change_text_style
if __name__ =='__main__':
  files_to_change = ['1.docx', '2.docx', '3.docx', '4.docx', '5.docx']
  change_text_style(files_to_change)