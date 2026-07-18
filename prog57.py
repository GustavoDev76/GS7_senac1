lista_mercado = []
print("=== LISTA DE COMPRAS DO MERCADO ===")
while True:

    produto = input("adicione um produto em sua lista de compras: ")
    if produto.lower() == "sair":
        print("saindo da lista...")
        break

    if produto in lista_mercado:
        print("produto ja cadastrado")
    else:
        lista_mercado.append(produto)       
        for lista in lista_mercado:
            print(lista)
total_itens = len(lista_mercado)
print(f"tem {total_itens} itens em sua lista")

