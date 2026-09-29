produtos = {
    1: "Camiseta",
    2: "Calça"
}


def rota_produto(id):
    try:
        if id in produtos:
            nome = produtos[id]
            return {"nome": nome}, 200
        else:
            return {"erro": "Produto não encontrado"}, 404

    except Exception:
        return {"erro": "Erro interno do servidor"}, 500