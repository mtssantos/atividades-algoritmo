contador = 0
while contador != 4:
    usuario = input("Entre com o usuário: ")
    senha = input("Entre com a senha: ")

    if (usuario == "bolinha") and (senha == "troca"):
        print("Bem vindo.")
        contador = 4
    elif contador == 4:
        print("Você atingiu o limite.")
        exit()
    else:
        print("""\nUsuário ou senha inválida\n""")
        contador = contador + 1
print("Você atingiu o limite. O usuário será bloqueado.")

    