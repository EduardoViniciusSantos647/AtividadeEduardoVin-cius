class SaldoInsuficienteError(Exception):
   def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")

    return saldo - valor