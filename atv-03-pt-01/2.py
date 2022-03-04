import math

def cadastrovendedor(nome, cpf, setor):
    print(f"""
        Vendedor Cadastrado:
        ID: 2
        NOME: {nome}
        CPF: {cpf}
        SETOR: {setor}  
    --------------------------------------------------
    """)

def calculacomissao(nome, salario):
    if (salario <= 5000):
        comissao = salario * 0.03
        salario_total = salario + comissao
        print(f"""
        Nome: {nome}
        Salário Total: R$ {math.floor(salario_total)}
        --------------------------------------------------
        """)
    elif (salario >= 5000) and (salario <= 10000):
        comissao = salario * 0.06
        salario_total = salario + comissao
        print(f"""
        Nome: {nome}
        Salário Total: R$ {math.floor(salario_total)}
        --------------------------------------------------
        """)
    elif (salario > 10000):
        comissao = salario * 0.1
        salario_total = salario + comissao
        print(f"""
        Nome: {nome}
        Salário Total: R$ {math.floor(salario_total)}
        --------------------------------------------------
        """)

opcao = 0

while (opcao != 3):
    print("Bem vindo ao nosso sistema!")
    print("""Selecione a opção desejada:
    1: Cadastrar Vendedor
    2: Calcular Salário
    3: Encerrar sistema
    """)
    opcao = int(input("Escolha a sua opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")
        setor = input("Digite o setor onde vai trabalhar: ")

        cadastrovendedor(nome, cpf, setor)
    elif opcao == 2:
        nome = input("Digite o nome do Vendedor: ")
        salario = float(input("Digite o salário do Vendedor: R$ "))

        calculacomissao(nome, salario)
    elif opcao == 3:
        print("Até logo!")
        exit()
    else:
        print("Digite uma opção válida!")
    



