ano_nascimento = int(input("digite sua data de nascimento: "))
ano_atual = int(input("em que ano estamos? "))

idade = ano_atual - ano_nascimento
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

    # usando (elif)
    ano_nascimento = int(input("digite sua data de nascimento: "))
ano_atual = int(input("em que ano estamos? "))

idade = ano_atual - ano_nascimento
if idade >= 18:
    print("Maior de idade")
elif idade >= 65:
    print("Idosos")
        
else:
    print("Menor de idade")