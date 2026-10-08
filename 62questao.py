def e_perfeito(numero):
    if numero <= 0:
        return False

    soma = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma = soma + divisor

    if soma == numero:
        return True
    else:
        return False


n = int(input("Digite um número: "))

if e_perfeito(n):
    print(n, "é um número perfeito!")
else:
    print(n, "não é um número perfeito.")