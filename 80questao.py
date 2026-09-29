class ProdutoInvalidoError(Exception):
    """Erro para nome de produto vazio"""


class ValorInvalidoError(Exception):
    """Erro para preço menor ou igual a zero"""


class QuantidadeInvalidaError(Exception):
    """Erro para quantidade que não é inteiro positivo"""


def registrar_venda(produto, preco, quantidade):
    if produto == "":
        raise ProdutoInvalidoError("O nome do produto não pode ser vazio.")

    if preco <= 0:
        raise ValorInvalidoError("O preço deve ser maior que zero.")

    if type(quantidade) != int or quantidade <= 0:
        raise QuantidadeInvalidaError("A quantidade deve ser um inteiro positivo.")

    total = preco * quantidade

    venda = {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }
    return venda


def gerar_relatorio(vendas):
    if len(vendas) == 0:
        print("Nenhuma venda registrada.")
        return

    total_vendas = len(vendas)
    faturamento = 0
    quantidades = {}

    for venda in vendas:
        faturamento = faturamento + venda["total"]

        nome = venda["produto"]
        if nome in quantidades:
            quantidades[nome] = quantidades[nome] + venda["quantidade"]
        else:
            quantidades[nome] = venda["quantidade"]

    mais_vendido = ""
    maior_quantidade = 0

    for nome in quantidades:
        if quantidades[nome] > maior_quantidade:
            maior_quantidade = quantidades[nome]
            mais_vendido = nome

    ticket_medio = faturamento / total_vendas

    print("----- RELATÓRIO DO DIA -----")
    print("Quantidade de vendas:", total_vendas)
    print("Produto mais vendido:", mais_vendido, "(", maior_quantidade, "unidades )")
    print("Faturamento total: R$", round(faturamento, 2))
    print("Ticket médio: R$", round(ticket_medio, 2))


vendas = []

while True:
    produto = input("Nome do produto (ou 'fim' para encerrar): ")

    if produto == "fim":
        break

    try:
        preco = float(input("Preço unitário: "))
        quantidade = int(input("Quantidade vendida: "))
        venda = registrar_venda(produto, preco, quantidade)
    except ProdutoInvalidoError as erro:
        print("Erro:", erro)
    except ValorInvalidoError as erro:
        print("Erro:", erro)
    except QuantidadeInvalidaError as erro:
        print("Erro:", erro)
    except ValueError:
        print("Erro: digite números válidos para preço e quantidade.")
    else:
        vendas.append(venda)
        print("Venda registrada com sucesso!")
    finally:
        print("Pedido processado.")
        print()

gerar_relatorio(vendas)