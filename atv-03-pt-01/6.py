import random

limite_inferior = random.randrange(0,100)
limite_superior = random.randrange(0,100)
numero = random.randint(limite_inferior, limite_superior)

contador = 0
while contador != 1:
    print(limite_inferior)
    print(limite_superior)
    print(int(numero))
    resposta = int(input("Resultado Desejado: "))
    if (resposta > numero):
        limite_superior = resposta
    elif (resposta < numero):
        limite_inferior = resposta
    elif (resposta == numero):
        print("Acertou o miserável.")
        contador = 1