def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValueError("Valor inválido. Digite um valor maior que zero.")

    if valor_saque > saldo:
        raise ValueError("Saldo insuficiente.")

    novo_saldo = saldo - valor_saque
    return novo_saldo

saldo_atual = 500.0

try:
    valor = float(input("Digite o valor do saque: "))
    saldo_atual = realizar_saque(saldo_atual, valor)
    print("Saque realizado! Novo saldo:", saldo_atual)
except ValueError as erro:
    print("Erro:", erro)