total = ""
valor = 0
print("---CARDAPIO RESTAURANTE---")
print("1 - BATATA FRITA (R$20.00)")
print("2 - CHOPP (R$12.00)")
print("3 - HAMBURGUER (R$ 20.00)")
print("4 - LASCOSTA (R$65.00)")
print("0 - PARA FINALIZAR O PEDIDO")

pedido = str(input("Escolha seu item do pedido: "))

while pedido != "0":
    
    if pedido == "1":
        print("O Item (Batata Frita) de R$20.00 foi adicionado ao pedido")
        valor += 20
    elif pedido == "2":
        print("o Item (Chopp) de R$12.60 foi adicionado ao cardapio")
        valor += 12
    elif pedido == "3":
        print("o Item (Hamburguer) de R$20.00 foi adicionado ao caradapio")
        valor += 20
    elif pedido == "4":
        print("o Item (Lascosta) de R$65.00 foi adicionado ao cardapio")
        valor += 65
    else:
        print("Nao existe esse Item no cardapio. Desculpe!")
    pedido = str(input("escolha outro item do cardapio (0 - para finalizar o pedido): "))
    
print("---PEDIDO FINALIZADO---")
print(f"O valor total do pedido: R${valor}")

print("---COM 10% DE DESCONTO---")
valor_desconto = valor * 0.9
print(f"O valor total do pedido com 10 de desconto: R${valor_desconto}")
