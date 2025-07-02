import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def dez_titulos():
    '''Percorrer os 10 primerios titulos da 1° pag e extrair infromações sobre o livro'''
    
    try:
        url = "https://books.toscrape.com/catalogue/page-1.html"
        retorno = requests.get(url)
        
        if retorno.status_code != 200:
            return []
            
        soup = BeautifulSoup(retorno.text, "html.parser")
        titulos = []
        
        for dados in soup.find_all("article", class_="product_pod")[:10]:  # percorrerá penas os 10 primeiros
            titulo = dados.h3.a["title"]
            preco = dados.find("p", class_="price_color").get_text()
            estoque = "icon-ok" if dados.find("p", class_="instock availability") else "Out of stock"
            aval_dado = dados.find("p", class_="star-rating")
            aval_estre = {"Zero": "🚫", "one": "⭐","Two": "⭐⭐", "Three": "⭐⭐⭐", "Four": "⭐⭐⭐⭐", "Five": "⭐⭐⭐⭐⭐" }
            aval = aval_estre.get(aval_dado["class"][1])
            
            titulos.append(f" titulo {titulo}, preço {preco}, estoque {estoque} e valiação {aval}")
            # titulos.append(preco)
            # titulos.append(aval)
            # titulos.append(estoque)
            
        return titulos
    
    except Exception as e:
        print(f"Erro na extração: {e}")
        return []

# Extrair os 10 primeiros títulos
titulos = dez_titulos()

# Gerar PDF simples
pdf_file = "titulos_livros.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Configurações do PDF
c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 100, "10 Primeiros Títulos de Livros")

c.setFont("Helvetica", 12)
y_position = height - 140

# Adicionar títulos ao PDF
for i, titulo in enumerate(titulos, 1):
    c.drawString(100, y_position, f"{i}. {titulo}")
    y_position -= 25
    
    if y_position < 50:  # Nova página se necessário
        c.showPage()
        y_position = height - 100
        c.setFont("Helvetica", 12)

c.save()

print("Relatório PDF gerado com sucesso!")
print("\nTítulos extraídos:")
for i, titulo in enumerate(titulos, 1):
    print(f"{i}. {titulo}")