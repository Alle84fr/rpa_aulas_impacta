import pyautogui
import time

print("Mostrando posição do mouse")
print("Mova o cursor do maouse")

try:
    while True:
        x, y = pyautogui.position()
        #print(f"\nLocal atual x = {x} e y = {y}", end="\r") -> aqui dá uma lista de posições
        print(f"Local atual x = {x} e y = {y}", end="\r")    #aqui muda a posição sem mostrar o "histórico" de posição
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nCaptura interrompida")