def somar(valor1, valor2):
    return valor1 + valor2

numero1 = int(input("digite um valor: "))
numero2 = int(input("digite o segundo valor: "))
total = somar(numero1, numero2)
print(f"{numero1} + {numero2} = {total}")