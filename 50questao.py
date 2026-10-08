alunos = {}

while len(alunos) < 5:
    nome = input("Digite o nome: ")

    if nome in alunos:
        print("Esse aluno já foi cadastrado. Digite outro nome.")
        continue

    nota = float(input("Digite a nota: "))
    alunos[nome] = nota

soma = 0

for nome in alunos:
    soma = soma + alunos[nome]

media = soma / len(alunos)

print("Media da turma:", media)

print("Alunos aprovados:")

for nome in alunos:
    if alunos[nome] >= 7:
        print(nome, alunos[nome])