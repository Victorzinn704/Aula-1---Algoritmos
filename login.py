senha_correta = "senha123"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print("Senha errada, tente novamente")

if tentativas == 0:
    print("Acesso bloqueado")