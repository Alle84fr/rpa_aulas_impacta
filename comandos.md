
# automação de planilha

# 1° criar:
# a - dataframe com os dados
# b - calccular média e criar nova coluna
# c - criar planilha
# d - formatar dados numéricos 2 casas
# e - formatar cabeçalho
# f - formatar dados inserindo e verificar notas abaixo de 7
# g - salvar

# biblioteca pandas - manipular dados - pip install pandas
# bibliotexa openpycl - manipula excel - pip install openpyxl - como ela é grande, muitos módulos grandes - então chamar o que usará
# já instalado - sempre instalar como adm no pronpt

import pandas as pd
from openpyxl import load_workbook #leitura de planilha
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

#criar dataFRame

dados = {
    "nome": ["Ana", "clara", "Carlos", "Diogo"],
    "nota_1": [8.5, 6.9, 7.0, 9.1],
    "nota_2": [9.0, 6.5, 7.7, 10.0]
}

#df = dataframe

df = pd.DataFrame(dados)
print(df)                              #mostra a tabela com coluna n°intem, nome, nota_1 e nota_2

#criar média e coluna
#dentro do objeto dataframe passar as chaves, conteúdo da coluna é o que está dentro das chaves
#mean = média - axis=1 é média simples

df["média"] = df[["nota_1", "nota_2"]].mean(axis=1)
print(df)

# dados já estão prontos, agora salvar em excel

arq_excel = "notas.xlsx"

# sheet_name = notas = uma das planilhas será nomeada como notas
df.to_excel(arq_excel, index=False, sheet_name="Notas")

# abrir arquivo com openpyxl para formatar
# worldworkbook = wb
wb = load_workbook(arq_excel)
ws = wb["Notas"]

# formatar cabeçalho - nome, nota_1 e _2
# negrito e preenchimento cor 

header_fill = PatternFill(start_color="D8E2DC", fill_type="solid")
for cell in ws [1]:               # a partir da 1° cédulas
    cell.font = Font(bold=True)  #título em negriito
    cell.fill = header_fill      #cor de fundo
    
# dados numéricos

# ormatar colunas numéricas para duas casas decimais

for row in ws.iter_rows(min_row=2, min_col=2, max_col=4):
    for cell in row:
        cell.number_format ="0.00"
        
# destacar notas abaixo de 7, fundo outra cor

for row in ws.iter_rows(min_row=2, min_col=2, max_col=4):
    for cell in row:
        if isinstance(cell.value, (int, float)) and cell.value <7:
            cell.fill = PatternFill(start_color="FFE5D9", fill_type="solid")

#
wb.save(arq_excel)

print(arq_excel)

-tipos                         -dados
click - clica em algo           endereço da imgem ou file
textor - digita algo            "texo qualquer"
tecla - pressiona tecla         "enter", "esc"
hotkey - combina teclas         ctrl+s
espera - espera x seg           "3"

pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)

 pyautogui.hotkey('ctrl', 'c') copiar
  pyautogui.hotkey('ctrl', 'v') colar