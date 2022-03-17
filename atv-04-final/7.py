palavra_um = input("Primeira palavra: ")
palavra_dois = input("Segunda palavra: ")

if (palavra_um == palavra_dois):
    print("As palavras são iguais!")
elif (palavra_um != palavra_dois):
    if(len(palavra_um) == len(palavra_dois)):
        print("As palavras tem o mesmo comprimento!")
    elif (len(palavra_um) > len(palavra_dois)):
        print("A primeira palavra é maior que a segunda!")
    elif (len(palavra_um) < len(palavra_dois)):
        print("A segunda palavra é maior que a primeira!")
    

