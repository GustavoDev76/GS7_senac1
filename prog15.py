print("------------------")
print("OPCOES DE VOTOS")
print("15 - Juquinha")
print("25 - Luizinho")
print("36 - Aninha")
print("------------------")

votacao = int(input("escolha sua votacao: "))

if votacao == 15:
    print("Voce votou em Juquinha")
elif votacao == 25:
    print("Voce votou em Luizinho")
elif votacao == 36:
    print("Voce votou em Aninha")
else:
    print('Numéro invalido')
