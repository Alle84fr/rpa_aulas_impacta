import time

status = "pendente"
while status == "pendente":
    print("Aguardando aprovação....")
    time.sleep(6) # Esperar 6 segundos antes fazer outro processamento
    #simular a mudança de status
    status = "aprovado"

print("Processo aprovado! \nContinuando automação....")