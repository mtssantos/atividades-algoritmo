lista_alunos = []
lista_nota = []


contador = 0

while contador != 5:
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do Aluno: "))
    participacao = int(input("Participou do evento? Digite [1] para sim e [2] para não: "))

    if (participacao == 1):
        nota = nota + 10.0
        lista_nota.append(nome)
        lista_nota.append(nota)
        lista_alunos.append(lista_nota)
        contador = contador + 1
    elif (participacao == 2):
        print("Nota não adicionada.")
        lista_nota.append(nome)
        lista_nota.append(nota)
        lista_alunos.append(lista_nota)
        contador = contador + 1

print(lista_alunos)




    

