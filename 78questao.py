def calcular_media(n1, n2, n3):
    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
        raise ValueError("Nota inválida. As notas devem estar entre 0 e 10.")

    media = (n1 + n2 + n3) / 3
    return media


# Programa principal
try:
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
except ValueError:
    print("Erro: digite apenas números.")
else:
    try:
        resultado = calcular_media(nota1, nota2, nota3)
        print("Média:", round(resultado, 2))

        if resultado >= 7:
            print("Situação: Aprovado")
        elif resultado >= 5:
            print("Situação: Recuperação")
        else:
            print("Situação: Reprovado")
    except ValueError as erro:
        print("Erro:", erro)