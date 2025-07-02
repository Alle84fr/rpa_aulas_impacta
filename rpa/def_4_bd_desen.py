#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO BANCO DE DADOS   4/                |
#                     |_____________________________________________________________|


############# BANDO DE DADOS DEVE SE CHAMAR PROJETO_RAP.DB

import sqlite3
import sys
import io
from datetime import datetime
from def_3_desen_bas import desenhos_base

#devido pesquisas, resolvi usar este ao invéz do canvas, mais fácil diagramar parágrafos

# ___________________ BD ____________________________________

def bd_geral(todosDes):
    """ Recebe as informações da def desenho_bas e irá criar quatro tabelas
    1° tabela geral com os 15 desenho
    2° tabela de desenhos que amo
    3° tabela de desenhos que quero assistir
    4° tabela de desenhos que não quero ver """
    
    salvando_stdout_restauro = sys.stdout
    
    try:
        data_arqui= datetime.now().strftime("%d-%b-%Y")     # erro nos  %D-%d
        # nome_aquiv = f"projeto_rpa_{data_arqui}.db"
        nome_aquiv = f"projeto_rpa.db" #resolvit tirar datas para ser padrão para chamar no terminal
        #solicitacao = juncao.cursor()     #para não esquecer, CURSOR = executa comando sql

        with sqlite3.connect(nome_aquiv) as juncao:
            solicitacao = juncao.cursor()       #esqueci do ()
        
        # ___________________ TABELA TODOS DESENHOS
        
            solicitacao.execute('''
            CREATE TABLE IF NOT EXISTS quinze_desenhos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    titulo_oficial TEXT,
                    ano INTEGER,
                    imagem TEXT)''')

            print("Tabela quinze_desenhos criada")

            # ___________________ TABELA DESENHOS AMO
            
            solicitacao.execute('''
            CREATE TABLE IF NOT EXISTS desenhos_q_amo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    titulo_oficial TEXT,
                    ano INTEGER,
                    imagem TEXT)''')
            
            print("Tabela desenhos q amo criada")
            
            # ___________________ TABELA DESENHOS QUERO VER
            
            solicitacao.execute('''
            CREATE TABLE IF NOT EXISTS desenhos_q_verei (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    titulo_oficial TEXT,
                    ano INTEGER,
                    imagem TEXT)''')
            
            print("Tabela desenhos q não verei criada")
            
            # ___________________ TABELA DESENHOS NÃO QUERO VER
            
            solicitacao.execute('''
            CREATE TABLE IF NOT EXISTS desenhos_q_nao_verei (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    titulo_oficial TEXT,
                    ano INTEGER,
                    imagem TEXT)''')
            
            print("Tabela desenhos q não verei criada")
            
            # ___________________ CONDIÇÃO
            
            for desenho in todosDes:
                solicitacao.execute('INSERT INTO quinze_desenhos (titulo, titulo_oficial, ano, imagem) VALUES (?, ?, ?, ?)',desenho)
                print(f"\n{desenho[0]} adicionado a tabela 😁 Quinze_desenhos 📼")
                
                if desenho[0] == "Howl's Moving Castle" or desenho[0] == "Spirited Away":
                    solicitacao.execute('INSERT INTO desenhos_q_amo (titulo, titulo_oficial, ano, imagem) VALUES (?, ?, ?, ?)',desenho)
                    print(f"\n{desenho[0]} adicionado a tabela 😍 Desenhos que amo 🎥")
            
                if desenho[0] == "Castle in the Sky" or desenho[0] == "Grave of the Fireflies" or desenho[0] == "Only Yesterday" or desenho[0] == "Tales from Earthsea":
                    solicitacao.execute('INSERT INTO desenhos_q_verei (titulo, titulo_oficial, ano, imagem) VALUES (?, ?, ?, ?)',desenho)
                    print(f"\n{desenho[0]} adicionado a tabela 🤓 Desenhos que quero ver 📽️")
                
                else:
                    solicitacao.execute('INSERT INTO desenhos_q_nao_verei (titulo, titulo_oficial, ano, imagem) VALUES (?, ?, ?, ?)',desenho)
                    print(f"\n{desenho[0]} adicionado a tabela 😒 Desenhos que não quero ver ✂️")
           
            # ___________________ SALVAR 
            
            juncao.commit()
            print("Tabalas criadas com sucesso")
          
    except sqlite3.Error as e:
        print(f" Erro no banco de dados do SQLite: {e}")

    except Exception as e:
        print(f"Erro fora do SQL: {e}")
    
    finally:
        sys.stdout = salvando_stdout_restauro
    
