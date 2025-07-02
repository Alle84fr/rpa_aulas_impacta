# pip install reportlab  ->  Trabalhar com PDf
from reportlab.pdfgen import canvas

#1 - Criar um novo arquivo pdf
pdf = canvas.Canvas("exemplo.pdf")

#2- Definir um Título
pdf.setTitle("Relatório de Atividades")

#3 Inserindo texto
pdf.drawString(100, 750, "Relatório de Atividades - 2025")

#4- Inserindo subTítulo
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(100, 720, "Atividades Realizadas")

#5 Criar a lista
atividades = [
    '- Reunião com a equipe de projetos',
    '- Desenvolvimento de novos módulos',
    '- Testes de funcionalidade',
    '- Treinamento para novos colaboradores'
]
#Escrever as atividades no PDF
y = 700 #Posição inicial na vertical
for atividade in atividades:
    pdf.setFont("Helvetica", 12)
    pdf.drawString(120, y, atividade)
    y -= 20 #Mover para baixo o Texto a ser inserido

pdf.save()
print("Arquivo criado com sucesso!")