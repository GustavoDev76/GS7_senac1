def montar_carrinho():
    # 1. Criamos a lista vazia (o carrinho)
    carrinho = []
    
    print("=== BEM-VINDO AO SUPERMERCADO PYTHON ===")

    # 2. laco de repeticao para capturar multiplos itens
    while True:
        produto = input("Digite um produto (ou digite 'sair'): ")

        # se o usuario quiser sair, interrompa o,laco
        if produto.lower() == "sair":
            break

        # 3. adiciona o produto digitado ao final da lsita
        carrinho.append(produto)
        print(f"--> '{produto}' adiciona ao carrinho com sucesso!")

        # 4. exibe o resultado final
    print("=== SEU CARRINHO DE COMPRAS ===")

    if len(carrinho) == 0:
     print("seu carrinho esta vazio")
    else:
       # exibe os itens um embaixo do outro
       for item in carrinho:
          print(f"- {item}")

    print(f"total de itens no carrinho: {len(carrinho)}")
# testando a funcao
montar_carrinho()
