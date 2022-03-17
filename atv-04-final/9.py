lista_frases = []
palavra = input("Digite a Palavra: ")
frase = ""
contador = 0
while frase != "FIM":
    frase = input("Digite a Frase: ")
    lista_frases.append(frase)
    contador += 1

print(f"Palavra: {palavra}")
for lista in lista_frases:
    print(f"Frase {lista_frases.index(lista) + 1}: {lista}")

    
