menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = input(menu)

    if opcao == "d":

        print("Depositar")

        deposito = float(input("Digite o valor para deposito: "))

        if deposito < 0:
            print("impossóvel depositar um número negativo")
        else:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'

    elif opcao == "s":

        print("Saque")

        if numero_saques >= LIMITE_SAQUES:

            print(f'limite de saques atingido: {numero_saques} saques')

        else:

            saque = float(input("Digite o valor do saque: "))

            if saque < 0 or saque > 500:

                print("Impossivel sacar (número negativo ou maior que R$ 500)")

            else:

                if saque > saldo:
                    print(f'Impossível sacar, pois o saldo é de: R$ {saldo:.2f}')
                else:
                    saldo -= saque
                    numero_saques += 1
                    extrato += f'Saque: R$ {saque:.2f}\n'

    elif opcao == "e":
        print("\n----------EXTRATO----------")
        print("Não foram realizadas Movimentações" if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("---------------------------")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada...")

