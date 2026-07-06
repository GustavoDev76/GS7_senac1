opcao = int(input("escolha uma opcao: "))

match opcao:
    case 1:
        print("Voc escolheu a opcao 1: Ver Saldo")
    case 2:
        print("Voce escolheu a opcao 2: Fazer Saque")
    case 3:
        print("Voce escolheu a opcao 3: Falar com atendente")
    case _:
        print("Opcao invalida! Escolha um numero de 1 a 3")