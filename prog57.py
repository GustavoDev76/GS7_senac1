lista_mercado = []
print("=== LISTA DE COMPRAS DO MERCADO ===")
while True:

    produto = input("adicione um produto em sua lista de compras: ")
    if produto == "sair":
        print("saindo da lista...")
        break

    lista_mercado.append(produto)
    print(f"{produto} foi adicionado a sua lista")

for item in lista_mercado:
    print(item)
    
itens_totais = len(lista_mercado)
print(f"voce tem {itens_totais} de itens em sua lista")