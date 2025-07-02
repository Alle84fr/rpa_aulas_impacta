#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO CAPTURA TELA NA DEF                |
#                     |_____________________________________________________________|

import pyautogui
import time 
import sys
import io


# ___________________ CARACTERE ESPECIAL

# std = standard/ fluxo, canal PADRÃO 
# out = Output - saída padrão no qual o programa envia dados
# ex: print
# destino = vai para tecla/console
# extra para registrar - in = Input -entrada, ex: input, vem, origem do teclado
# extra para registrar - err = Error - mensagens de erros e diagnósticos, destino tecla/console em um canal separado

# salvando_stdout_restauro = sys.stdout
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ___________________ FUNÇÃO PRINT AUTOMATICO
def print_tela():
    
    """Função sem retorno, ela apenas mostra o print que será realizado me pontos chaves do cód"""
    
    salvando_stdout_restauro = sys.stdout
    
    # infromação de print    
    sys.__stdout__.write("\nPrint 📸 da tela em ⏰ 2 segundo")
    sys.__stdout__.flush()
    time.sleep(2)
                    
    # processo de print e salvar

    printando = pyautogui.screenshot()
    intervalo = time.strftime("%d-%b-%Y__%H-%M")
    nome_print = f"Print_tela_{intervalo}.png"
    printando.save(nome_print)
        
    # mensagem final de ciclo

    sys.__stdout__.write(f"\n print {nome_print} salvo")
    sys.__stdout__.flush()

    # restaurar para estado inicial

 
    sys.stdout = salvando_stdout_restauro

