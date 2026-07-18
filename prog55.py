cursos = ["python", "java"]

curso_novo = input("digite um outro curso que ira fazer: ")
cursos.append(curso_novo)
for lista in cursos:
    print(lista)

excluir_curso = input("exclua um curso de sua lista: ")
cursos.remove(excluir_curso)
for lista_excluir in cursos:
    print(lista_excluir)

