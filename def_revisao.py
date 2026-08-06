def idade_nascimento():
    idade = 2026 - ano_nascimento

    if idade >= 65:
        print("Idoso")
    elif idade >= 18 and idade < 65:
        print("Maior de idade")
    else:
        print("Menor de idade")

ano_nascimento = int(input("digite seu ano de nascimento: "))
idade_nascimento()