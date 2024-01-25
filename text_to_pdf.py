from fpdf import FPDF

def convert_to_pdf(input_file):
    
    pdf = FPDF() #usar a classe fpdf como pdf

    with open(input_file, 'r') as o:
        text = o.read()              #pegar o texto do txt

    pdf.add_page('A4') #adicionar a primeira pagina
    pdf.set_font('Times', '', 12) #fonte times new roman 12
    pdf.write(4, text)
    pdf.output('seupdf.pdf')
    print("funcionou")

convert_to_pdf('/home/python_ws/loremipsum.txt')
