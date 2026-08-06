contador = 1
tabuada = int(input("escolha um valor para a tabuada: "))

while contador <= 10:
    resultado = tabuada * contador
    print(f"{tabuada} x {contador} = {resultado}")
    contador += 1
    