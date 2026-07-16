def data(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

ano_atual1 = 2026
ano_nascimento1 = int(input("em que ano voce nasceu: "))
idade = data(ano_atual1, ano_nascimento1)

if idade > 60:
    print(f"Voce tem {idade} anos, Idoso")
elif idade >= 18:
    print(f"Voce tem {idade} anos, é Maior de Idade")
else:
    print(f"Voce tem {idade} anos, é Menor de idade")
