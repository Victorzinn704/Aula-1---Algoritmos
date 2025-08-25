n = int(input("Digite um número: "))

soma = 0
cont = 0
for i in range(1, n+1):
    soma = soma + i
    cont = cont + 1

print("Soma com laço:", soma)
print("Quantidade de somas feitas:", cont)

soma_formula = n * (n + 1) // 2
print("Soma pela fórmula:", soma_formula)
# soma dos n primeiros números naturais