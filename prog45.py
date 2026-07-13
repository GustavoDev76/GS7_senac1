total = 0 
print("---TABLA DE PRODUTOS PARA REFERENCIA---")
print("1 - ARROZ (R$4.00)")
print("2 - FEIJAO (R$7.00)")
print("3 - MACARRAO (R$5.00)")
print("0 - PARA FINALIZAR")

codigo = int(input("digite um codigo de produto: "))

while codigo != 0:
    if codigo == 1:
        print("Arroz adicionado")
        total += 4
    elif codigo == 2:
        print("feijao adicionado")
        total += 7
    elif codigo == 3:
        print("Macarrao adicionado")
        total += 5
    else:
        print("Codigo invalido")
    codigo = int(input("digite um outro codigo (0 para finalizar): "))

    print(f"Total da compra: R${total:.2f}")