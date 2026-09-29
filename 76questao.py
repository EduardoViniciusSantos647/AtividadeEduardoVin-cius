import traceback


def processar_dados(dados):
    soma = 0

    for item in dados:
        try:
            numero = float(item)
            soma = soma + numero
        except (TypeError, ValueError):
            print("Problema no elemento:", item)
            traceback.print_exc()

    print("Soma dos valores válidos:", soma)


lista = [10, "20", "abc", None, 5.5]

processar_dados(lista)