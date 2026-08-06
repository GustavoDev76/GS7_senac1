numero = 1
valor = 0
while numero != 0:
    numero = int(input("digite um valor: "))
    valor = valor + numero
resultado = valor * 1.10
print("--- ACRESCIMO DE 10%")
print(f"{resultado:.2f}")