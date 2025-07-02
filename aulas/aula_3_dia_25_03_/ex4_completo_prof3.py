# Aula 5: Criação e conversão de arquivos PDF
# Duração: ~1h30

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pdf2image import convert_from_path

# Parte 1: Criar PDF com reportlab
c = canvas.Canvas("relatorio_livros.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 14)
c.drawString(100, 800, "Relatório de Livros")

c.setFont("Helvetica", 12)
y = 750
livros = []
for livro in livros:
    c.drawString(100, y, f"Título: {livro['Título']}")
    y -= 20
    c.drawString(100, y, f"Autor: {livro['Autor']}")
    y -= 20
    c.drawString(100, y, f"Ano: {livro['Ano']}")
    y -= 30

c.save()
print("PDF gerado com sucesso.")

# Parte 2: Converter PDF em imagem (para visualização)
imagens = convert_from_path("relatorio_livros.pdf")
imagens[0].save("relatorio_livros_preview.png")
print("PDF convertido em imagem.")