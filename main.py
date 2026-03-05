while True:
    nome = input("Digite seu nome: ")
    if nome == "":
        print("O nome não pode ser vazio. Por favor, tente novamente.") 
    elif not nome.isalpha():
        print("O nome deve conter apenas letras. Por favor, tente novamente.")
    else:
        break

while True:
    idade = input("Digite sua idade: ")
    if not idade.isdigit():
        print("A idade deve conter apenas números. Por favor, tente novamente.")
    else:
        break

while True:
    email = input("Digite seu email: ")
    if "@" not in email or "." not in email:
        print("O email deve conter '@' e '.'. Por favor, tente novamente.")
    else:
        break
while True:
    senha = input("Digite sua senha: ")
    if len(senha) < 6:
        print("A senha deve conter pelo menos 6 caracteres. Por favor, tente novamente.")
    else:
        break

print("Cadastro realizado com sucesso!")
print("ola " + nome + " você tem " + idade + " anos, seu email é " + email + " e sua senha é " + senha)
print("Obrigado por se cadastrar, " + nome + "!")
