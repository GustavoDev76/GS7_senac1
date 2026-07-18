    # EXERCICIO 4 (LISTA)
carros = []
contador = 0
while contador < 3:
    carro = input("adicione 3 carros em sua lista: ")
    carros.append(carro)
    contador += 1

    for lista in carros:
        print(lista)