#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO CAPTURA TELA NA DEF                |
#                     |_____________________________________________________________|

import pyautogui
import time 
import sys
import io

# ___________________ FUNÇÃO PRINT AUTOMATICO

    
"""Função sem retorno, ela apenas mostra o print que será realizado me pontos chaves do cód"""
    
salvando_stdout_restauro = sys.stdout
    
    # infromação de print    
sys.__stdout__.write("\nPrint 📸 da tela em ⏰ 3 segundo")
sys.__stdout__.flush()
time.sleep(3)
                    
    # processo de print e salvar

printando = pyautogui.screenshot()
intervalo = time.strftime("%d-%b-%Y__%H-%M-%S")
nome_print = f"Print_tela_{intervalo}.png"
printando.save(nome_print)
        
    # mensagem final de ciclo

sys.__stdout__.write(f"\n print {nome_print} salvo")
sys.__stdout__.flush()

    # restaurar para estado inicial

 
sys.stdout = salvando_stdout_restauro

