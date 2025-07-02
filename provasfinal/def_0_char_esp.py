
import sys
import io
from def_2_print_atom import print_tela

print_tela()


# ___________________ CARACTERE ESPECIAL

# std = standard/ fluxo, canal PADRÃO 
# out = Output - saída padrão no qual o programa envia dados
# ex: print
# destino = vai para tecla/console
# extra para registrar - in = Input -entrada, ex: input, vem, origem do teclado
# extra para registrar - err = Error - mensagens de erros e diagnósticos, destino tecla/console em um canal separado

def char_espec():
    salvando_stdout_restauro = sys.stdout
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    
