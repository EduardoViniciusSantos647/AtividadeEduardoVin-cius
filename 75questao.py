import random


def conectar_api():
 
    sorteio = random.randint(1, 2)

    if sorteio == 1:
        raise ConnectionError("Falha na conexão")

    return "Conectado"


def conectar_com_tentativas():
    for tentativa in range(1, 4):
        try:
            conectar_api()
            print("Conectado com sucesso na tentativa", tentativa)
            return True
        except ConnectionError:
            print("Falha na tentativa", tentativa)

    print("Não foi possível conectar. Encerrando com segurança.")
    return False