def somar_tres_numeros(a, b, c):
    soma = a + b + c

    if soma <= 21:
        return soma

    if a == 11 or b == 11 or c == 11:
        soma = soma - 10

    if soma <= 21:
        return soma
    else:
        return -1