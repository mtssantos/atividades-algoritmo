lista = [1, 2, 3, 4, 5]

valor = int(input("Digite um número para buscar: "))

if valor in lista:
    index = lista.index(valor)
    print(f"O valor {valor} existe na lista. E está na posição {index} ")
else:
    print(f"O valor {valor} não existe dentro da lista.")