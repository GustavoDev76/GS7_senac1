carros = {}
for i in range (2):
    carro = str(input("Qual Carro: "))
    marca = str(input("Qual Marca do Carro: "))
    valor = float(input("valor do carro: "))
    carros [carro, marca] = valor
    print(f"Informacoes Do Carro = {carros} ")
