def receber_numeros():
    numeros = []

    for i in range(5):
        numero = float(input("Digite um número: "))
        numeros.append(numero)

    return numeros


def maior_numero(numeros):
    maior = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero

    return maior


def menor_numero(numeros):
    menor = numeros[0]

    for numero in numeros:
        if numero < menor:
            menor = numero

    return menor



lista = receber_numeros()

print("O maior número é:", maior_numero(lista))
print("O menor número é:", menor_numero(lista))