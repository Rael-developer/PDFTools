from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def draw_rotated_text(canvas, text, x, y, angle):
    canvas.saveState()
    canvas.translate(x, y)
    canvas.rotate(angle)
    canvas.drawCentredString(0, 0, text)
    canvas.restoreState()

def create_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    
    # Definir o ângulo desejado (160 graus)
    angle = 160

    # Configurar a fonte e o tamanho do texto
    c.setFont("Helvetica", 12)

    # Posição da página (centralizada)
    page_width, page_height = letter
    x = page_width / 2
    y = page_height / 2

    # Escrever texto na página com rotação
    draw_rotated_text(c, "rascunho", x, y, angle)

    # Salvar o arquivo PDF
    c.save()

if __name__ == "__main__":
    pdf_file_path = "rascunho.pdf"
    create_pdf(pdf_file_path)
    print(f"PDF criado com sucesso em: {pdf_file_path}")
