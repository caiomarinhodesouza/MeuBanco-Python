# Variáveis para armazenar o saldo e as operações
saldo = 0.0
extrato = []
limite_saque_diario = 3
saques_diarios = 0
limite_valor_saque = 500

# Função para exibir o extrato
def mostrar_extrato():
    print("\n=== Extrato ===")
    if not extrato:
        print("Nenhuma operação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função para realizar um depósito
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

# Função para realizar um saque
def sacar(valor):
    global saldo, saques_diarios
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite_valor_saque:
        print(f"O valor máximo para saque é R$ {limite_valor_saque:.2f}.")
    elif saques_diarios >= limite_saque_diario:
        print("Limite de saques diários alcançado.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

# Função principal para o menu de operações
def menu():
    while True:
        print("\n=== Banco Python ===")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: "))
            sacar(valor)
        elif opcao == "3":
            mostrar_extrato()
        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")

# Iniciar o programa
menu()
