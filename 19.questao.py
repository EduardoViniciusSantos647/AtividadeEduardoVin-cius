numero = int(input("Digite um número inteiro positivo: "))

while numero < 0:
    print("Número inválido! O fatorial só existe para números não negativos.")
    numero = int(input("Digite um número inteiro positivo: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")