def contar_caractere(texto, caractere):
    contador = 0

    for letra in texto:
        if letra == caractere:
            contador = contador + 1

    print("O caractere", caractere, "aparece", contador, "vezes.")


