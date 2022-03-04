import math

def calculaalturafilho(alturapai, idadepai, alturamae, idademae):
    media = ((idadepai + idademae) / 2)
    media_altura = ((alturapai + alturamae) / 2)
    if (media <= 30):
        altura_masculino = (math.trunc(media_altura) + 0.09) / 100
        altura_feminino = (math.trunc(media_altura) - 0.1) / 100
        print(f"A estimativa de altura do filho se for menino é de {round(altura_masculino, 2)} m e se for menina {round(altura_feminino, 2)} m")
    elif (media > 30):
        altura_masculino = (math.trunc(media_altura) + 0.09) / 100
        altura_feminino = (math.trunc(media_altura) - 0.1) / 100
        print(f"A estimativa de altura do filho se for menino é de {round(altura_masculino, 2)} m e se for menina {round(altura_feminino, 2)} m")


alturapai = float(input("Digite a altura do Pai: "))
idadepai = int(input("Sua altura: "))
alturamae = float(input("Digite a altura da Mãe: "))
idademae = int(input("Sua altura: "))

calculaalturafilho(alturapai, idadepai, alturamae, idademae)
