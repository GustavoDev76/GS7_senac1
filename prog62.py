aluno = str(input("nome do aluno: "))
nota1 = float(input("primeira nota do aluno: "))
nota2 = float(input("segunda nota do aluno: "))
nota3 = float(input("terceira nota do aluno: "))
nota4 = float(input("quarta nota do aluno: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(F"--- MEDIA FINAL DO ALUNO ---")

if media >= 6:
    print(f"O aluno {aluno} está aprovado!")
else:
    print(f"O aluno {aluno} está de recuperacao!")

print(f"o aluno obteve uma media total de {media:.2f} pontos")