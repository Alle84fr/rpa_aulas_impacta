#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO BANCO DE DADOS   4/                |
#                     |_____________________________________________________________|


############# BANDO DE DADOS DEVE SE CHAMAR PROJETO_RAP.DB
import requests
import sqlite3
import sys
import io


from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, Alignment



from datetime import datetime


#devido pesquisas, resolvi usar este ao invéz do canvas, mais fácil diagramar parágrafos
 
from def_3_desen_bas import desenhos_base

# ___________________ CARACTERES ESPECIAIS ____________________________________

#sya,stdou.buffer t=  padrão de saída, toda ver que o .py usa esta formatção
# io.Text.... garante saída de texto com caracteres especiais
# sys.stadout = atribui Text... como novo sys.stdout

salvando_stdout_restauro = sys.stdout         #add esta parte para fazer "backup" da saída para por no final
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("sys.stdou")

# ___________________ BD ____________________________________
try:
    data_file= datetime.now().strftime("%d-%b-%Y")     # erro nos  %D-%d
    nome_aquiv = f"desenhos_geral_{data_file}.db"
    #solicitacao = juncao.cursor()     #para não esquecer, CURSOR = executa comando sql

    with sqlite3.connect(nome_aquiv) as juncao:
        solicitacao = juncao.cursor()       #esqueci do ()
    
        solicitacao.execute('''
        CREATE TABLE IF NOT EXISTS desenhos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                titulo_oficial TEXT,
                ano INTEGER,
                imagem TEXT)''')

        for i, desenho in enumerate(tod16):
            heranca = desenhos_base()
            solicitacao.execute('INSERT INTO desenhos (titulo, titulo_oficial, ano, imagem) VALUES (?, ?, ?, ?)',heranca)  # erro, estava VALEU
            print(f"heranca {i+1}: {heranca}")
            
        print("dados criados")
        print(heranca)
    
except sqlite3.Error as e:
    print(f" Erro no banco de dados do SQLite: {e}")

except Exception as e:
    print(f"Erro fora do SQL: {e}")
 
finally:
    sys.stdout = salvando_stdout_restauro
    
        
# juncao.commit() #salva
# juncao.close()  #fecha
    
        
# sqlite3.OperationalError: no such column: ano
# a coluna, "chave" ano não existe na tabela SQLlite
# pode ser erro de digitação, não existir coluna, consulando tabela com outro anoomimagem
# Erro VALUES (?, ?, ano, imagem), deveria estar tudo ?

# print("dados criados")  - > ValueError: I/O operation on closed file.
# tentando imprimir algo depois de fechar arquivo
# osys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8") ele iniciou e fechou 
# procurar por sys.stdout.close() no aquivo ou outro file
# with - gerenciamento de recurso
# se o with terminar sem erros/exceção, automaticamnete o commit() é chamado, então ele não será posto no final do cód
# ao terminar o bloco o with irá chamar close(), fechando o bloco, sendo assim, ele também sai do final do cód