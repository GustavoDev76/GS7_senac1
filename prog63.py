while True:
    ano_atual = 2026
    ano_nascimento = int(input("digite seu ano de nascimento: "))
    
    if ano_nascimento == 0:
        print("digite 0 para sair do programa")
        print("saindo do programa...")
        break

    idade = ano_atual - ano_nascimento

    if idade > 65:
        print(f"sua idade é {idade} anos Idoso")
    elif idade >= 18:
        print(f"Sua idade é {idade} anos Maior de idade")
    else:
        print(f"Sua idade é {idade} anos Menor de idade")        