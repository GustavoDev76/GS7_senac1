try:
    numero = int(input("digite um valor á ser dividido: "))
    denominador = int(input("digite o valor da divisao: "))

    resultado = numero / denominador
    print(f"o resultado da conta: {numero} / {denominador} = {resultado}")

except ValueError:
    print("digite apenas numeros inteiros")

except ZeroDivisionError:
    print("nao pode dividir por zero")