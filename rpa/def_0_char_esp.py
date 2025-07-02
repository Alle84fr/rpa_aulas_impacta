
import sys
import io


# ___________________ CARACTERE ESPECIAL

def char_espec():
    salvando_stdout_restauro = sys.stdout
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    
