# DESAFIO DE SEXTA!!!

idade = int(input("qual a sua idade: "))
genero = str(input("qual seu genero: ")).upper()

if idade >= 18 and genero == "MASCULINO":
    print("Esta apto para o alistamento")
else:
    print("Nao apto para o alistamento!")