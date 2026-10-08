class SaldoInsuficienteError(Exception):
    """Erro para saque maior que o saldo disponível"""


def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")

    return saldo - valor