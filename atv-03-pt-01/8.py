import random

print("Bem vindo a nossa calculadora.")

contador_erros = 0
contador_acertos = 0
while (contador_erros != 4):
    valor_1 = random.randrange(0,100)
    valor_2 = random.randrange(0,100)
    operador = random.choice(["+", "-"])
    print(f"A operação é {valor_1} {operador} {valor_2}")
    if operador == "+":
        total = valor_1 + valor_2
    elif operador == "-":
        total = valor_1 - valor_2
    resultado_recebido = int(input("Qual o resultado: "))
    if contador_acertos == 10:
        print("Meus parabéns, você atingiu o resultado desejado.")
        exit()
    elif contador_erros == 4:
        print("Que pena... Você atingiu o limite de erros. Tente novamente.")
        exit()
    else:
        if (resultado_recebido == total):
                print("Muito Bem!")
                contador_acertos = contador_acertos + 1
        else:
                print("Errrrrouuuuuuu.")
                contador_erros = contador_erros + 1
print("Limite atingido.")







