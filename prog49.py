def somar(valor, porcento):
    return valor * porcento

soma = int(input("digite um valor: "))
calculo = somar(soma, 0.15)
print(f"15% do valor total: {calculo}")

# SEM RETURN
def somar(valor, porcento):
    total = valor * porcento
    print(f"15% de {valor} é (total)")

soma = int(input("digite um valor: "))
somar(soma, 0.15)