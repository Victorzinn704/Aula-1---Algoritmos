cpf = input("Digite o CPF (11 dígitos): ")

if cpf.isdigit() and len(cpf) == 11:
    print("CPF válido")
else:
    print("CPF inválido")