palavra = input("Palavra a ser recebida: ")
caractere = input("Caractere a ser removido: ")
palavra.upper()
palavrafinal = palavra.replace(caractere.upper(), "")
print(f"Resultado: {palavrafinal}")