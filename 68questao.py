def dividir_lucros():
    try:
        lucros = float(input("Digite o lucro do trimestre: "))
        acionistas = int(input("Digite a quantidade de acionistas: "))

        valor_por_acionista = lucros / acionistas

        print("Cada acionista vai receber:", round(valor_por_acionista, 2))

    except ZeroDivisionError:
        print("Erro: a quantidade de acionistas não pode ser zero.")

    except ValueError:
        print("Erro: digite apenas números válidos.")