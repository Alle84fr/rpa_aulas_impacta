
# Automação para abrir o Bloco de Notas, garantir que uma nova aba
# seja aberta antes de começar a digitar e evitar sobrescrita.


import pyautogui                #resumindo automatiza
import time                     #traz sleep/delay
import os
from datetime import datetime   #trabalha com datas e horas

# Define uma pausa de 2 segundos entre os comandos para evitar problemas de execução rápida
pyautogui.PAUSE = 2

# Fecha qualquer instância do Bloco de Notas aberta antes de iniciar
os.system("taskkill /f /im notepad.exe")

# Aguarde um pouco para garantir que foi fechado
time.sleep(2)

#Abrir o menu iniciar do windows
pyautogui.press("win")

#Pesquisar digitando "Bloco de Notas" e pressiona a tecla enter
pyautogui.write("Bloco de Notas", interval=0.1)
pyautogui.press("enter")

#Aguardar abrir o bloco de notas
time.sleep(2)

# Abrir uma nova aba do Bloco de Notas usando Ctrl + N
pyautogui.hotkey("ctrl", "n")

# Aguardar um pouco para garantir que a nova aba abriu corretamente
time.sleep(1)

# Começar a digitar no Bloco de Notas
pyautogui.write("Saluton Mondo Komincantos! 1° bots", interval=0.1)   # interval - tempo de digitção entre cada caracteres, aqui 1seg

# Abrir a caixa de diálogo "Salvar Como" usando F12
pyautogui.hotkey("ctrl","shift","s") 
#pyautogui.hotkey("f12")

# Aguardar a abertura da caixa de diálogo "Salvar Como"
time.sleep(1)

# Gerar um nome de arquivo dinâmico com base no timestamp
# datetime.now() = retorna data e hora atual (ano, mês, dia, horas, min, seg, microsegundos) -> ex (2025,05,19,19,31,12365)
# .strftime() = formata o retorno do datetie em string formatada, que será
# "nome_do_arquvo_ano(%Y),mês(%m),dia(%d),hora(%H),min(%M),seg(%S).txt(no formato de texto)" -> ex nome_do_arquivo_20250519_193620.txt

nome_arq = datetime.now().strftime("aula_1_%Y%m%d_%H%M%S.txt")
pyautogui.write(nome_arq)

# Pressionar Enter para salvar
pyautogui.press("enter")

# Aguarde um pouco para garantir que o arquivo foi salvo
time.sleep(2)

# Fechar o Bloco de Notas corretamente
pyautogui.hotkey("alt", "f4")  # fecha a janela

# Garantir que o processo foi encerrado corretamente
# os.system() = executa comando no terminal do sistema operacional (CMD)
# taskkill = comando nativo do windows para "matar processor em execução"
# /f = forçar a ação (neste caso fecha sem pedir confirmação)
# /im = especifica o nome do processo a ser encerrado
# notepad.exe é o nome do processo a ser ecerrado
 
time.sleep(1)
os.system("taskkill /f /im notepad.exe")

print(f"Automação concluída com sucesso! Arquivo salvo como: {nome_arq}")