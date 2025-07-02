#                     _______________________________________________________________
#                     |                                                             |
#                     |             FUNÇÃO CAPTURA TELA USUÁRIO DIGITANDO           |
#                     |_____________________________________________________________|

import pyautogui
import time 
from pynput import keyboard
# resolvi usar método de tecla e não botão mouse por achar que btn do mouse é muito usado
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

# ___________________ VERIFICA SE A ÚLTIMA TECLA FOI P

# só será tirado print quando usuário der p + enter

p_para_enter_print = False 

# ___________________ FUNÇÃO BOTÃO E GERAL ____________________________

# hasattr = função, booleana, que verifica o atributo ou método do objeto
# char é o atributo das keys com caracteres visíveis como letras,, n°s, espaço e enter
# sys - módulo do sistema que  fornece acesso a variáveis e funções que interagem com o interpretador
# flush() - obrigada o conteúdo a ser "escrito" imediatamente, depois que o write enviar a mensagem, o flush mostra na tela a imagem
    
def btn_p_print(key):
    
    """Função que irá chamar pynput ("input") - que verificará se a ultima tecla pressionada foi o p.
    com a junção do enter o usuário poderá tirar um print"""
    
    global p_para_enter_print
    
    try:
        """ verifica se foi char (caractere) é string ou n°, se for true e p entra em processo de espera para enter,
        se não for ou não ter enter sai do estado de espera"""
        
        # se a o atributo for tecla/key char, o P será igual a p, a variável de verificação será True, mensagem de comando, print na tela
        
        if hasattr(key, "char"):
            if key.char.lower() == "p":
                p_para_enter_print = True
                sys.__stdout__.write("\n👉 P + ENTER 👈 para tirar 📸 da tela")
                sys.__stdout__.flush()
            else:
                p_para_enter_print = False
                
       # se for enter, se última key for p, gera print
        elif key == keyboard.Key.enter:
            if p_para_enter_print:
                printando = pyautogui.screenshot()
                intervalo = time.strftime("%d-%b-%Y")
                nome_print = f"Print_tela_{intervalo}.png"
                printando.save(nome_print)
    
                # ___________________ MESAGEM E IMAGEM PARA USUÁRIO
    
                # sys - módulo do sistema que  fornece acesso a variáveis e funções que interagem com o interpretador
                # flush() - obrigada o conteúdo a ser "escrito" imediatamente, depois que o write enviar a mensagem, o flush mostra na tela a imagem
                # lembrar de retornar "p" para falso
                
                sys.__stdout__.write(f"\n print {nome_print} salvo")
                sys.__stdout__.flush()
                p_para_enter_print = False
            
            else:
                p_para_enter_print = False
                # se não teve p, não tem professo "p"
                
        else:
            # não foi p e enter
            p_para_enter_print = False
     
    except AttributeError:
        # para outra tecla se não enter, fora do char visivel, ex: shift, ctrl, alt
        if key != keyboard.Key.enter:
            p_para_enter_print = False
        
        # se for alguma key fora das listadas, apenas segue o bloco
        pass

# ___________________ FUNÇÃO BOTÃO FINALIZAR ____________________________

def finalizar_print (key):
    
    """ Função para parar o ciclo da funçao btn_p_prin, que será ao dar clic em ESC """
    
    if key == keyboard.Key.esc:
        # se a tecla/key for igual a tecla do eclado esc
        sys.__stdout__.write("\n👉 ESC 👈 para ❌ finalizar ")
        sys.__stdout__.flush()
        return False
    
# ___________________ MAIN__________________ ____________________________

sys.__stdout__.write("\n👉 P + ENTER 👈 para tirar 📸 da tela")
sys.__stdout__.write("👉 ESC 👈 para ❌ finalizar\n")
sys.__stdout__.flush()

# ___________________ DEIXA PROGRAMA ATIVO, ESPERANDOS SER CHAMADO

# Listener = ouvinte, captura de evento, no caso captura do teclado
# join =  mantém programa tivo, esperandos ser chamado
# Só fecha o ciclo quando for False/ clicl no ESC

with keyboard.Listener(on_press= btn_p_print, on_release=finalizar_print) as Listener:
    Listener.join()
    
sys.__stdout__.write("\nFunção finaliza\n")
sys.__stdout__.flush()

# restaurar para estado inicial

sys.stdout = salvando_stdout_restauro
