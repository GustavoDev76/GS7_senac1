carros = {}
for i in range (2):
    carro = input("Qual Carro: ")
    marca = input("Qual Marca do Carro: ")
    valor = float(input("valor do carro: "))
    carros[carro] = {
        "marca": marca,
        "valor": valor
    }
    print(f"Informacoes Do Carro = {carros} ")
