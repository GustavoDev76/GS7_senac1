valor1 = int(input("digite um valor: "))
valor2 = int(input("digite outro valor: "))

if valor1 > valor2:
    print(f"o primeiro valor ({valor1}) é maior")
elif valor2 > valor1:
    print(f"o segundo valor ({valor2}) é maior ")
else:
    print(f"os valores sao iguais")