import time, datetime
from datetime import datetime

def menu_inicial():
    menu_inicial = """
    Seja bem vindo ao PatrickBank\n
    Escolha uma opção no Menu:
    [1]Já Sou Um Cliente
    [2] Quero Abrir Uma Conta"""

    return input(menu_inicial)

def menu_cliente():
    menu_cliente = """
    Opção Escolhida: Já Sou um Cliente\n
    Escolha uma opção no Menu Abaixo
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova Conta
    [l] Listar Contas
    [q] Sair"""

    return input(menu_cliente)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print('_'*50)
        print(f"\nSeu saldo atual é de: R${saldo:.2f}\n",
              datetime.now())
        print('_' * 50)

    else:
        print('x' * 50)
        print("Operação falhou! O valor informado é inválido.")
        print('x' * 50)

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('x' * 50)
        print("Operação falhou! Você não tem saldo suficiente.")
        print('x' * 50)

    elif excedeu_limite:
        print('x' * 50)
        print("Operação falhou! O valor do saque excede o limite.")
        print('x' * 50)

    elif excedeu_saques:
        print('x' * 50)
        print("Operação falhou! Número máximo de saques excedido.")
        print('x' * 50)

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print('_' * 50)
        print(f"\nSeu saldo atual é de: R${saldo:.2f}",
              datetime.now())
        print('_' * 50)

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}",
              datetime.now())
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (Somente Numeros)")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print('Já existe um cliente com esse CPF Cadastrado')
        return

    nome = input('Informe o seu nome Completo: ')
    dn = input("Informe a sua data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço:")

    usuarios.append({"nome": nome, "dn": dn, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastrado com sucesso")

def filtro_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF de Usuario:")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com Sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Ag: {conta['agencia']}
                C/C: {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}"""

        print(linha)


def Codigo_Bancario():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao_inicial = menu_inicial()



        if opcao_inicial == '1':
            while True:
                print('\n','#'*100)
                opcao_cliente = menu_cliente()

                if opcao_cliente == "d":
                    valor = float(input("Informe o valor do depósito: "))

                    saldo, extrato  = depositar(saldo, valor, extrato)

                elif opcao_cliente == "s":
                    valor = float(input("Informe o valor do saque: "))

                    saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)

                elif opcao_cliente == "e":
                    exibir_extrato(saldo, extrato=extrato)

                elif opcao_cliente == "n":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        contas.append(conta)

                elif opcao_cliente == "l":
                    listar_contas(contas)

                elif opcao_cliente == "q":
                    break

            else:
                print("Operação Inválida")

        elif opcao_inicial == '2':

            criar_usuario(usuarios)

        else:
            print ("Operação Inválida")

    print("Operação Finalizada")

Codigo_Bancario()
