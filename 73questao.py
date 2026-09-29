def calcular_descontos(precos):
    for texto in precos:
        try:
            preco = float(texto)
        except ValueError:
            print("Preço inválido:", texto)
        else:
            preco_final = preco * 0.90
            print("Preço", preco, "com 10% de desconto:", round(preco_final, 2))


# Lista de preços em texto
lista_precos = ["100", "50.5", "abc", "200"]

calcular_descontos(lista_precos)