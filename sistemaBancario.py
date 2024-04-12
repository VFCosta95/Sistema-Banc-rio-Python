# Sistema Bancário com Python

# Sacar, Deposito e Visualizar Extrato

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3
#-------------------------------------------------------------------
while True:
    opcao = input(menu)

    if opcao == 'd': 
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato = f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: O valor informado e invalido.")
#-------------------------------------------------------------------
    elif opcao == 's':
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excedeu limites.')

        elif excedeu_saque:
            print('Operação falhou! N° maximos de saques excedidos.')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1

        else:
            print('Operação falhou: O valor informado é invalido.')
#-------------------------------------------------------------------
    elif opcao == 'e':
        print("\n *********** Extrato ***********")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print('******************************')
#-------------------------------------------------------------------
    elif opcao == 'q':
        break
#-------------------------------------------------------------------
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada!')
#-------------------------------------------------------------------
