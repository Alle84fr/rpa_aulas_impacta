import pyautogui
import time

#Definir uma área
AREA_X1, AREA_Y1 = 500, 300 # Canto superior esquerdo
AREA_X2, AREA_Y2 = 600, 400 # Canto Inferior direito

print("MOva o cursor para exibir sua posição")

while True:
    x, y = pyautogui.position() # capturar a posição do Mouse
    
    #Verificar se o cursos estão dentro da área definida
    if AREA_X1 <= x <= AREA_X2 and AREA_Y1 <= y <= AREA_Y2:
        pyautogui.click(x,y) #Simular o clique onde estiver o cursos
        print(f"Clique automático em: X={x}, Y={y}")
        time.sleep(2)
    else:
        print(f"Cursor fora da área: X={x}, Y={y}")
    
    time.sleep(1)