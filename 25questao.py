produtos = []

quantidade = int(input("Digite a quantidade de produtos a serem cadastrados: "))

for i in range(quantidade):
    nome = input(f"Digite o nome do produto {i + 1}: ")
    produtos.append(nome)

total_produtos = len(produtos)

print(f"\nProdutos cadastrados: {produtos}")
print(f"Quantidade total de produtos cadastrados: {total_produtos}")