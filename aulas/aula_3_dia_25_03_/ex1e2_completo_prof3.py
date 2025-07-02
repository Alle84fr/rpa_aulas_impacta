import pyautogui
import time

# Parte 1: Descobrindo posições do mouse (para rodar manualmente no terminal)
print("Mova o mouse. Pressione Ctrl+C para sair.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição atual: x={x}, y={y}", end="\r")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nCaptura encerrada.")

# Parte 2: Capturando imagem da tela
screenshot = pyautogui.screenshot()
screenshot.save("screenshot_tela.png")
print("Screenshot salva.")