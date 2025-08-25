notas = []
qtd = int(input("Quantos alunos? "))

for i in range(qtd):
    nota = float(input(f"Nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / qtd
maior = max(notas)
menor = min(notas)

acima = 0
for n in notas:
    if n > media:
        acima += 1

percentual = (acima / qtd) * 100

print("Média da turma:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Percentual acima da média:", percentual, "%")