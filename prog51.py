def calcular_media(nota1, nota2, nota3, nota4):
      nota = (nota1 + nota2 + nota3 + nota4) / 4

      if nota >= 7:
       print(f"a media do aluno foi: {nota}, Esta Aprovado!")  
      elif nota >= 5:
       print(f"a media doa aluno foi: {nota}, Esta De Recuperacao")
      else:
       print(f"a media do aluno foi abaixo de 5: {nota}, Esta Reprovado")

soma1 = float(input("digite a primeira nota do aluno: "))
soma2 = float(input("digite a segunda nota do aluno: "))
soma3 = float(input("digite a terceira nota do aluno: "))
soma4 = float(input("digite a quarta nota do aluno:  "))
calcular_media(soma1, soma2, soma3, soma4)