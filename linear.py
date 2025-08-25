nomes = ["Ana", "Joao", "Batman", "Zelda", "Vasco"]

busca = input("Digite o nome que deseja buscar: ")

posicao = -1
for i in range(len(nomes)):
    if nomes[i] == busca:
        posicao = i = 1
        break

if posicao == -1:
    print("Nome não encontrado")
else:
    print("Nome encontrado na posição", posicao)