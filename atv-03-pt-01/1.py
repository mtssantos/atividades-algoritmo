def classificanadador(idade):
    if (idade >= 5) and (idade <= 10):
        print("Sua classsificação é a Infantil!")
    elif (idade >= 11) and (idade <= 17):
        print("Sua classsificação é a Juvenil!")
    elif (idade >= 18) and (idade <= 25):
        print("Sua classsificação é a Adulto!")
    elif (idade < 5) or (idade > 25):
        print("Inapto")
    else:
        print("Ocorreu um erro no recebimento da Idade.")


print("Bem vindo ao classificador de idades para a natação! \n")

idade = int(input("Digite a sua idade para saber a sua classificação: "))

classificanadador(idade)
