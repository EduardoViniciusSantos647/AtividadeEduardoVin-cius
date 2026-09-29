def parse_cpf(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        print("CPF válido!")
    else:
        print("CPF inválido. Digite 11 números.")


def main():
    cpf = input("Digite o CPF (só números): ")
    parse_cpf(cpf)


main()