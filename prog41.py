numero = int(input("escolha um numero: "))

contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} X {contador} = {resultado}")
    contador += 1