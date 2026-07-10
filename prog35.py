for i in range (4):
 aluno = str(input("digite aluno: "))

 nota1 = float(input("digite a primeira nota: "))
 nota2 = float(input("digite a segunda nota: "))
 nota3 = float(input("digite a terceira nota: "))
 
 media = (nota1 + nota2 + nota3) / 3

 if media >= 7.0:
     print(f"o {aluno} Tirou as notas: {nota1}, {nota2}, {nota3} entao sua media é {media:.2f} = APROVADO")
 elif media >= 5.0:
    print(f"o {aluno} Tirou as notas: {nota1}, {nota2}, {nota3} entao sua media é {media:.2f} = RECUPERACAO")
 else:
    print(f"o {aluno} Tirou as notas: {nota1}, {nota2}, {nota3} entao sua media é {media:.2f} = REPROVADO")   