frase = "Bom dia, tudo bem? Aqui é Mateus Santos!"
posicao = input("Digite um caractere e veja se está na frase: ")
posicao_encontrada = frase.find(posicao)
if(posicao == posicao_encontrada):
    print(f"O caractere {posicao} existe na frase! Está na posição: {posicao_encontrada}")
else:
    print(f"O caractere {posicao} não foi enontrado na frase! Posição: {posicao_encontrada}")