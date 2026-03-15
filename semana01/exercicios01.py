# Questão 01. Escreva uma função Python e_multiplo(n,m) que recebe dois valores inteiros e retorna True
# caso n seja um múltiplo de m e False caso contrário.

# def e_multiplo(n, m):
#     if n % m == 0:
#         return True
#     else:
#         return False

# print(e_multiplo(10, 2))
# print(e_multiplo(10, 3))
# print(e_multiplo(15, 5))
# print(e_multiplo(15, 4))

# Questão 02. Escreva uma função Python cubo(a) que recebe um valor float que representa a aresta de um
# cubo e imprima a área, o perímetro e o volume do cubo.

# def cubo(a):
#     area = 6 * (a ** 2)
#     perimetro = 12 * a
#     volume = a ** 3
#     print(f"Área: {area}")
#     print(f"Perímetro: {perimetro}")
#     print(f"Volume: {volume}")

# cubo(2.0)

# Questão 03. O salário semanal de um funcionário é igual ao valor por hora trabalhada multiplicado pelo
# total de horas normais, mais o pagamento de horas extras. O pagamento de horas extras é igual ao total de
# horas extras multiplicado por 1,5 vezes o valor por hora normal. Escreva uma função Python
# calcula_salario(valor_hora, horas_normais, horas_extras) que receba como entrada o salário por hora,
# o total de horas normais e o total de horas extras e exiba o salário semanal do funcionário.

# def calcula_salario(valor_hora, horas_normais, horas_extras):
#     salario_normal = valor_hora * horas_normais
#     salario_extra = valor_hora * 1.5 * horas_extras
#     salario_total = salario_normal + salario_extra
#     print(f"Salário semanal: R$ {salario_total:.2f}")

# input_valor_hora = float(input("Digite o valor por hora: "))
# input_horas_normais = int(input("Digite o total de horas normais: "))
# input_horas_extras = int(input("Digite o total de horas extras: "))
# calcula_salario(input_valor_hora, input_horas_normais, input_horas_extras)

# Questão 04. Escreva uma função Python min_max(l) que recebe uma lista de inteiros e retorna uma
# tupla com o menor valor da lista e o maior valor da lista.

# def min_max(l):
#     if not l:
#         return None
#     menor = min(l)
#     maior = max(l)
#     return (menor, maior)

# lista = [3, 1, 4, 1, 5, 9]
# resultado = min_max(lista)
# print(f"Menor valor: {resultado[0]}, Maior valor: {resultado[1]}")

# Questão 05. Escreva uma função Python format_data(data) que inverta o formato no formato
# "dia/mes/ano", onde dia e mes tem dois dígitos e ano tem quatro dígitos, para o formato "ano/mes/dia".

# def format_data(data):
#     partes = data.split('/')
#     if len(partes) != 3:
#         return "Formato de data inválido"
#     dia, mes, ano = partes
#     return f"{ano}/{mes}/{dia}"

# input_data = input("Digite a data no formato dia/mes/ano: ")
# resultado = format_data(input_data)
# print(f"Data formatada: {resultado}")

# Questão 06. Escreva uma função Python num_vogais(s) que conte o número de vogais de uma string.

# def num_vogais(s):
#     vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛ'
#     contador = 0
#     for char in s:
#         if char in vogais:
#             contador += 1
#     return contador

# input_string = input("Digite uma string: ")
# resultado = num_vogais(input_string)
# print(f"Número de vogais na string: {resultado}")

# Questão 07. Escreva uma função Python del_pontuacoes(s) uma string s, representando uma frase, e
# retorne uma cópia dessa frase sem a pontuação. Por exemplo, se a string recebida for "Olá, seja
# bem-vindo.", esta função retornaria "Olá seja bem vindo".

# def del_pontuacoes(s):
#     pontuacoes = '.,;:!?()[]{}"\'-'
#     resultado = ''
#     for char in s:
#         if char not in pontuacoes:
#             resultado += char
#     return resultado

# input_string = input("Digite uma frase: ")
# resultado = del_pontuacoes(input_string)
# print(f"Frase sem pontuação: {resultado}")

# Questão 08. Escreva uma função Python produto_impar() que receba uma lista com uma sequência de
# valores inteiros e retorne se existe um par distinto de números na sequência cujo produto seja ímpar.

# def produto_impar(lista):
#     for i in range(len(lista)):
#         for j in range(i + 1, len(lista)):
#             if (lista[i] * lista[j]) % 2 != 0:
#                 return True
#     return False

# input_lista = [1, 2, 3, 4, 5]
# resultado = produto_impar(input_lista)
# print(f"Existe um par de números cujo produto é ímpar? {resultado}")

# Questão 09. Escreva uma função Python imposto_devido(renda) considerando que no país Utopia cada
# cidadão tem que pagar imposto sobre a sua renda. Cidadãos que recebem até 1000 dinheiros utópicos
# pagam 5% de imposto. Cidadãos que recebem entre 1000 e 2500 pagam 5% de imposto sobre 1000
# dinheiros e 10% sobre o que passar de 1000. Cidadãos que recebem mais do 5000 dinheiros pagam 5%
# de imposto sobre 1000 dinheiros, 10% de imposto sobre 2500 dinheiros e 20% sobre o que passar de
# 5000.

# def imposto_devido(renda):
#     if renda <= 1000:
#         imposto = renda * 0.05
#     elif renda <= 2500:
#         imposto = (1000 * 0.05) + (renda - 1000) * 0.10
#     elif renda <= 5000:
#         imposto = (1000 * 0.05) + (renda - 1000) * 0.10
#     else:
#         imposto = (1000 * 0.05) + (2500 * 0.10) + (renda - 5000) * 0.20
#     return imposto
# input_renda = float(input("Digite a renda do cidadão: "))
# resultado = imposto_devido(input_renda)
# print(f"Imposto devido: R$ {resultado:.2f}")

# Questão 10. Escreva um programa que permita ao usuário navegar pelas linhas de texto em um arquivo.
# O programa solicita ao usuário o nome do arquivo e insere as linhas de texto em uma lista. Em seguida, o
# programa entra em um loop no qual imprime o número de linhas no arquivo e solicita ao usuário o
# número da linha. Os números de linha variam de 1 até o número de linhas no arquivo. Se a entrada for 0,
# o programa é encerrado. Caso contrário, o programa imprime a linha associada a esse número.

# def navegar_arquivo():
#     nome_arquivo = input("Digite o nome do arquivo: ")
#     try:
#         with open(nome_arquivo, 'r') as arquivo:
#             linhas = arquivo.readlines()
#             num_linhas = len(linhas)
#             print(f"O arquivo tem {num_linhas} linhas.")
#             while True:
#                 numero_linha = int(input("Digite o número da linha (0 para sair): "))
#                 if numero_linha == 0:
#                     print("Encerrando o programa.")
#                     break
#                 elif 1 <= numero_linha <= num_linhas:
#                     print(f"Linha {numero_linha}: {linhas[numero_linha - 1].strip()}")
#                 else:
#                     print("Número de linha inválido. Tente novamente.")
#     except FileNotFoundError:
#         print("Arquivo não encontrado. Verifique o nome e tente novamente.")
# navegar_arquivo()