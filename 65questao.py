def calcularCubo(numero):
    cubo = numero * numero * numero
    return cubo


def calcularDivisaoCubo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)
    else:
        return False