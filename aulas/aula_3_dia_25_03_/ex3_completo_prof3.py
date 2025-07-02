# Aula 3: Automação de login em sistema local (formulário simulado)
# Duração: ~2h

# Este exemplo simula login em um sistema fictício (campo usuário e senha)
# Use algum app aberto ou formulário HTML local para simulação
import pyautogui
import time
time.sleep(2)  # Tempo para usuário abrir o formulário manualmente

usuario = "admin"
senha = "123456"

pyautogui.write(usuario)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")
print("Login automático enviado.")