def pedir_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))

            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                return idade

        except ValueError:
            print("Isso não é um número inteiro. Tente novamente.")


idade_usuario = pedir_idade()
print("Cadastro realizado! Idade registrada:", idade_usuario)