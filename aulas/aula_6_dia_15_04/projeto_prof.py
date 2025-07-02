import requests
from bs4 import BeautifulSoup
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Função para extrair dados de livros de uma página específica
def extrair_livros(pagina):
    try:
        url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
        response = requests.get(url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        livros = []

        for artigo in soup.find_all("article", class_="product_pod"):
            titulo = artigo.h3.a["title"]
            preco = artigo.find("p", class_="price_color").text.strip()
            disponibilidade = artigo.find("p", class_="instock availability").text.strip()
            livros.append({
                "Título": titulo,
                "Preço": preco,
                "Disponibilidade": disponibilidade
            })

        return livros
    except Exception as e:
        print(f"Erro ao extrair livros da página {pagina}: {e}")
        return []

# Função para exportar para Excel
def exportar_para_excel(dados, nome_arquivo="livros.xlsx"):
    try:
        df = pd.DataFrame(dados)
        df.to_excel(nome_arquivo, index=False)
        print(f"✅ Arquivo Excel salvo como: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao exportar para Excel: {e}")

# Função para exportar para PDF
def exportar_para_pdf(dados, nome_arquivo="livros.pdf"):
    try:
        c = canvas.Canvas(nome_arquivo, pagesize=A4)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 800, "Relatório de Livros")

        y = 770
        c.setFont("Helvetica", 10)
        for livro in dados:
            texto = f"{livro['Título']} | {livro['Preço']} | {livro['Disponibilidade']}"
            c.drawString(50, y, texto)
            y -= 20
            if y < 50:
                c.showPage()
                y = 800

        c.save()
        print(f"✅ Arquivo PDF salvo como: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao exportar para PDF: {e}")

# Menu principal
def menu():
    print("""
==============================
  PROJETO SCRAPING DE LIVROS
==============================
[1] Buscar livros de 1 página
[2] Buscar livros de múltiplas páginas
[3] Exportar dados para Excel
[4] Exportar dados para PDF
[0] Sair
""")

# Execução do projeto
todos_os_livros = []

while True:
    try:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pagina = input("Número da página (1 a 50): ")
            livros = extrair_livros(pagina)
            todos_os_livros.extend(livros)
            print(f"{len(livros)} livros encontrados na página {pagina}.")

        elif opcao == "2":
            qtd = int(input("Quantas páginas deseja percorrer? "))
            for p in range(1, qtd + 1):
                print(f"🔍 Coletando página {p}...")
                livros = extrair_livros(p)
                if not livros:
                    print("Fim da coleta - página inválida ou vazia.")
                    break
                todos_os_livros.extend(livros)
            print(f"✅ Total de livros coletados: {len(todos_os_livros)}")

        elif opcao == "3":
            if todos_os_livros:
                exportar_para_excel(todos_os_livros)
            else:
                print("⚠️ Nenhum dado para exportar.")

        elif opcao == "4":
            if todos_os_livros:
                exportar_para_pdf(todos_os_livros)
            else:
                print("⚠️ Nenhum dado para exportar.")

        elif opcao == "0":
            print("Encerrando o programa. 👋")
            break

        else:
            print("Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"Erro no menu principal: {e}")