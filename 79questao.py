def cadastrar_produto(nome, preco, quantidade):
    if nome == "":
        raise ValueError("O nome não pode ser vazio.")

    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    return "Produto cadastrado com sucesso!"