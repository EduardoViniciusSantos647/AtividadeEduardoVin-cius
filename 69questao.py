def ler_relatorio():
    try:
        with open("relatorio_vendas.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do relatório:")
            print(conteudo)

    except FileNotFoundError:
        print("Erro: o arquivo relatorio_vendas.txt não foi encontrado.")

    finally:
        print("Encerrando a leitura do arquivo.")