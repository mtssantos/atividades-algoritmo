arq = open("teste.txt", "r")
linhas = arq.readlines()
for linha in linhas:
    print(f"Quantidade de Caracteres: {len(linha)}")
    print(f"Quantidade de Palavras: {len(linha.split())}")