visitante_idade = int(input("qual a sua idade: "))
possui_ingresso = str(input("voce tem ingresso valido: ")).upper() .strip()

if visitante_idade >= 12 and possui_ingresso == "TENHO":
    print("Acesso liberado, Divitar-se no brinquedo!")
elif visitante_idade <= 11:
    print("Voce tem o ingresso, mas nao tem a idade minina de 12 anos")
else:
    print("Acesso negado, Voce precisa de um ingresso")