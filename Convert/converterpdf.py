# pip3 install pdf2docx
from pdf2docx import Converter, parse
from datetime import datetime

def converterPDf():

    pdf = input("Digite o nome do arquivo ex.: demo.pdf: ")
    now = datetime.now()
    now = datetime.strftime(now, "%d %m %Y %H %M %S")
    pdf_file = f'pdf/{pdf}'
    word_file = f'pdf/pdfconvertido {now}.docx'

    # cv = Converter(pdf_file)
    # cv.convert(pdf_file, start=0, end=None)
    # cv.close()

    parse(pdf_file, word_file, start=0, end=None)
