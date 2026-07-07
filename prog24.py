codigo = int(input("digite o codigo de erro: "))

match codigo:
    case 200:
        print("Sucesso! tudo certo com sua requisicao.")
    case 400:
        print("Erro do cliente: requesicao maliformada.")
    case 401 | 403:
        print("Erro de permissao: voce nao tem acesso a esta pagina,.")
    case 404:
        print("Erro: pagina nao encontrada.")
    case 500 | 503:
        print("Erro no servidor: nosso sistema esta instavel no momento.")
    case _:
        print("Codigo invalido = codigo HTTP (codigo_status) desconhecido.")
print("teste de commit")
print("teste de push pelo vscode")