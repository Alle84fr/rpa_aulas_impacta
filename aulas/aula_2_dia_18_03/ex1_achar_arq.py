import os
import pyautogui

# como está passando só o nome do arquivo o .py vai pesquisar só no diretório dele, que está o aquivo do py que foi salvo
# OBSERVAÇÃO - SE DER PLAY EM PS C:\Users\arfur\RPA\aulas\aula_2_dia_18_03 COM ARQUIVO DADOS1, DÁ ACHADO
# SE DER PLAY COM PS C:\Users\arfur\RPA\aulas COM FOLDER DIA_15_04 DÁ ACHADO
# SE DER PLAY EM PS C:\Users\arfur\RPA\aulas COM ARQUIVO DADOS1, DÁ NÃO ACHADO POIS ESTÁ DENTRO DE OUTRA PASTA

# arquivo = "dados.csv"  # se quiser ver dando não encontrado
# arquivo = "dia_15_04"       # se quiser ver encontrado folder 
arquivo = "dados1.csv"        # se quiser ver encontrado file (antes entrar na pasta)
if os.path.exists(arquivo):
    #Código que vai processar algo
    pyautogui.alert("pasta encontrada!") # não retorna print, retorna um alert/ caixa com mensagem e botão de ok
else:
    pyautogui.alert("Arquivo não encontrado.")