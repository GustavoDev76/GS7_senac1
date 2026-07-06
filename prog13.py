nome = input("digite seu nome: ")

nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))
nota3 = float(input("terceira nota: "))
nota4 = float(input("quarta nota: "))

soma = (nota1 + nota2 + nota3 + nota4) / 4

if soma >= 6:
    print(f"{nome} está aprovado")
else:
    print(f"{nome} está de recuperacao")
    