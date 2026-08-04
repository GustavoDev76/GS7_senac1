while True:
    try:
        numero = int(input("digite um numero inteiro para saber a metade de 2: "))
        resultado = numero / 2

        print(f"a metade de é: {numero} / 2 = {resultado}")
        break

    except ValueError:
        print("Erro: voce digitou letras, pro favor, digite apenas numeros inteiros")