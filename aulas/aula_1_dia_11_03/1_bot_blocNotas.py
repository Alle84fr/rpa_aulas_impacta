'''
1° menu inicar
2° pesquisar bloco de notas
3° pressionar enter
4° digitar texto bloco notas
5° salvar
6° sair

time executa linha alinha
na linha de abrir nota e diálogo não se sabe tempo desta ação
seria para dar um delay - aguarde antes de ir para cada ação externa
neste caso seria pausa de 2 seg entre comando do pyautogui
'''

import pyautogui
import time

pyautogui.PAUSE = 2
'''AGUARDE 2 SEG A CADA COMANDO'''

pyautogui.press("Win")
'''ao clicar em win, botão windows, com bandeira aparece o que desej0
ao dar run - aparece como se tivesse apertado o botão
agora vou digitar bloco de notas na pesquisa
'''
pyautogui.write("Bloco de Notas", interval =0.1 )
'''Escreve no local de texto aberto e posiciona o curso no local correto
depois da vírgula coloca delay de 0.1 -> interval -> velocidade mais lenta
agora dar enter'''
pyautogui.press("enter")

'''cada computador tem sua memória e configuração -> se o computador for um pouco mais lento
esperar o bloco de notas abrir e depois texto, caso contrário, se não ter delay, quando o bloco
de notas abrir, vai perder o início do texto'''
time.sleep(2)

'''Afora que esperou, chama para digitar
já que digitou, salve o texto, usar a tecla de atalho de salvar
para chamar ctrl + s usa pyoutogui hotkey
irá abrir janela par dar nome e salvar
esperar abrir caixa de diálogo
dar o nome
fechar bloco de notas alt f4
para florear colocar no console texto
'''
'''pyautogui.write("Saluton Mondo komicanto! atomatizando com .py usando pyautogui.Manipula a tela")
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.write("Meu file 1° aula RPA")
pyautogui.press("enter")kotlin
pyautogui.hotkey("alt", "F4")

print("Foi")

até aqui abriu no bloco de notas  já existente
Quando faz automação deve ser passo a passo, lapidando
ele abriu e não fechou
quando termina arquivo txt, deve dar close ou o py mantém o mesmo bloco, pois está na memória e
não fechou
deve usar entre escrever e sleep para tirar da emória
'''

pyautogui.write("Saluton Mondo komicanto! atomatizando com .py usando pyautogui.Manipula a tela")

pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.write("Meu file 1° aula RPA")
pyautogui.press("enter")
pyautogui.hotkey("alt", "F4")

