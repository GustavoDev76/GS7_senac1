total = ""
print("---TABELA DE PRODUTOS PARA REFERENCIA---")
print("001 - ARROZ (R$4.00)")
print("002 - FEIJAO (R$7.00)")
print("003 - MACARRAO (R$5.00)")
print("0 - PARA FINALIZAR")

codigo = str(input("digite um codigo de produto: "))

while codigo != "0":
    if codigo == "001":
        print("Arroz adicionado")
        total += 4
    elif codigo == "002":
        print("feijao adicionado")
        total += 7
    elif codigo == "003":
        print("Macarrao adicionado")
        total += 5
    else:
        print("Codigo invalido")
    codigo = str(input("digite um outro codigo (0 para finalizar): "))

    print(f"Total da compra: R${total:.2f}")