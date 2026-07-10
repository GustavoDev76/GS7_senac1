pessoas = {}
for i in range (2):
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    pessoas [nome] = idade
    print(f"Dicionario completo: {pessoas}")
