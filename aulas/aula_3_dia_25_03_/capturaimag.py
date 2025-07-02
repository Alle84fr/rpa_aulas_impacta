import pyautogui
import time

#capturar uma imagem da tela toda/ imagem congelada

screenshot =  pyautogui.screenshot()
screenshot.save("Imagem_Tela.png")
print("Imagem salva com sucesso")

