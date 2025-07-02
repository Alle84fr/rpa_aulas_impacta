import pyautogui

senha = pyautogui.password("Informe sua senha:")

if senha == "admin":
    #Senha estiver correta qualquer código a ser executado
    pyautogui.alert("Acesso concedido")
else:
    pyautogui.alert("Acesso negado")