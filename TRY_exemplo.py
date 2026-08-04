try:
    idade = int(input("digite sua idade: "))
    print(f"Sua idade é {idade} anos")
except ValueError:
    print("Digite apenas numeros validos") 