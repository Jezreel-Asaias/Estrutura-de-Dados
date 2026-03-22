# Questoes extras.
# Atividade 01: Contar Números em uma Lista

# def contar_numeros(lista, numero):
#     contador = 0
#     for item in lista:
#         if item == numero:
#             contador += 1
#     return contador

# numeros = [10, 20, 10, 30, 10, 20, 10]
# print(contar_numeros(numeros, 10))
# print(contar_numeros(numeros, 20))
# print(contar_numeros(numeros, 30))
# print(contar_numeros(numeros, 40))

# Atividade 02: Considere uma função que recebe uma lista como parâmetro.

# 1. Lista com n elementos
# A função deve percorrer a lista, identificar os elementos
# repetidos e retornar uma lista com os elementos que se
# repetem.
# a) Implemente a função
# b) Calcule o tempo de execução, conforme o modelo RAM

# def identificar_repetidos(lista):
#     repetidos = []
#     n = len(lista)
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             if lista[i] == lista[j] and lista[i] not in repetidos:
#                 repetidos.append(lista[i])
#                 break
                
#     return repetidos

# numeros = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
# print(identificar_repetidos(numeros))

# Questões da lista da Semana 03

# Questão 01. Assinale a alternativa que completa a afirmação: A análise da complexidade algoritmos
# computacionais é a técnica utilizada para ___________ .
# a) simular se o algoritmo está correto e funcional.
# b) escalar o código.
# c) estimar o desempenho performático do algoritmo quando a quantidade de entrada aumenta.
# d) garantir que o programa possui portabilidade entre vários sistemas operacionais
# Resposta: c) estimar o desempenho performático do algoritmo quando a quantidade de entrada aumenta.

# Questão 02. Correlacione as colunas:
# (A) Eficácia
# (B) Eficiência
# (C) Corretude
# (D) Complexidade
# ( ) Ocorre quanto o algoritmo tem Corretude.
# ( ) A _____________ exprime quando o algoritmo sempre produz a saída
# correta.
# ( ) Expressa o desempenho de um algoritmo.
# ( ) Um algoritmo tem ______ quando apresenta baixa complexidade.
# Resposta:
# (A)
# (C)
# (D)
# (B)

# Questão 03. O Modelo RAM (Random Access Machine) é uma abstração fundamental para a análise de
# algoritmos iterativos. Sobre as premissas deste modelo, assinale a alternativa incorreta:
# a) Cada operação elementar (como soma, subtração ou atribuição) possui um custo de tempo constante.
# b) O tempo necessário para acessar qualquer posição da memória é o mesmo, independentemente do
# índice ou endereço.
# c) O modelo assume que o processador executa múltiplas instruções simultaneamente.
# d) Operações complexas, como execução de funções, não possuem custo unitário, devendo ser analisadas
# pela soma de suas instruções internas.
# Resposta: c) O modelo assume que o processador executa múltiplas instruções simultaneamente.

# Questão 04. Diferencie análise empíca vs análise matemática para análise da complexidade?
# Resposta:
# Análise Empírica.
# Esta análise baseia-se na execução real do código em um computador físico. Você roda o programa, cronometra o tempo e observa o consumo de recursos.

# Análise Matemática.
# Também chamada de análise teórica, ela foca na lógica do algoritmo antes de qualquer linha de código ser compilada, baseando-se no Modelo RAM.

# Questão 05. Como ocorre a execução de programas conforme a arquitetura de von Neumann?
# Resposta:
# A execução ocorre através de um ciclo repetitivo chamado Ciclo de Busca-Decodificação-Execução

# Questão 06. Conforme o modelo RAM, estime o tempo T das instruções abaixo:
# a) i = 0
# b) i <= 3
# c) i > 3 and j < 5
# d) soma = (soma + i) * 5
# e) for i in range(0,5)

# Resposta:
# a) i = 0T = 1: Ocorre 1 operação de atribuição.
# b) i <= 3T = 1: Ocorre 1 operação de comparação (relacional).
# c) i > 3 and j < 5T = 3: Ocorrem 2 operações de comparação (>  e <) e 1 operação lógica (and).
# d) soma = (soma + i) * 5T = 3: Ocorre 1 adição, 1 multiplicação e 1 atribuição do resultado à variável soma.
# e) for i in range(0, 5)T = 12: No modelo RAM, a estrutura de repetição é decomposta:Inicialização (i=0): 1 operação.Testes de Condição (i < 5): 6 operações (5 verdadeiras e 1 falsa para sair do laço).Incrementos (i = i + 1): 5 operações.Cálculo: 1 + 6 + 5 = 12.

# Questão 07. Classifique por ordem de grandeza as expressões de tempo T(n):
# a) T(n) = 3n+1
# b) T(n) = 4n³ + 5n² + n
# c) T(n) = n
# d) T(n) = 5
# e) T(n) = 4n² +1

# Resposta:
# a) T(n) = 3n+1O(n): A expressão
# b) T(n) = 4n³ + 5n² + nO(n³): O termo dominante é 4n³.
# c) T(n) = nO(n): A expressão é linear.
# d) T(n) = 5O(1): A expressão é constante
# e) T(n) = 4n² +1O(n²): O termo dominante é 4n².

# Cálculo de T(n)

# Questão 08. Para os códigos a seguir, calcule a expressão T(n):
# def somar(a, b):
#     soma = a + b
#     return soma
# T(n) = 2: Ocorrem 1 operação de adição e 1 operação de retorno.

# def multiplicar(a, b):
#     produto = a * b
#     return produto
# T(n) = 2: Ocorrem 1 operação de multiplicação e 1 operação de retorno.

# def potencializar(b, e):
#    potencia = 1
#    for i in range(e):
#      potencia *= b
#    return potencia
# T(n) = 2e + 2: Ocorrem 1 operação de atribuição (potencia = 1), e para cada iteração do laço (e vezes) ocorrem 1 multiplicação e 1 comparação, totalizando 2 operações por iteração. Além disso, há 1 operação de retorno no final. Portanto, o total é 2e (para as operações dentro do laço) + 2 (para a inicialização e o retorno).

# Questão 09. Para os códigos a seguir, calcule a expressão T(n) e explique a diferença entre as
# complexidades das mesmas funções da questão 08:

# def somar(a, b):
#     soma = a + b
#     return soma
# T(n) = 2: Ocorrem 1 operação de adição e 1 operação de retorno. A complexidade é O(1) (constante), pois o número de operações não depende do tamanho da entrada.

# def multiplicar(a, b):
#    produto = 0
#    for i in range(b):
#      produto = somar(produto, a)
#     return produto

# Codificação

# Questão 10. Escreva uma função Python num_consoantes(texto) que conte o número de consoantes de
# uma string. Expresse a função T(n) para essa função.

# def num_consoantes(texto):
#     consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     contador = 0
#     for char in texto:
#         if char in consoantes:
#             contador += 1
#     return contador

# Questão 12. Escreva uma função Python interseção(lista01, lista02) que recebe duas listas e retorna uma
# terceira lista com os elementos que estão na duas ao mesmo tempo. Caso não haja elementos que estejam
# nas duas retorna uma lista vazia. Faça uma versão com laço e outra versão com conjuntos. Expresse a
# função T(n) para essas funções.

# Versão com laço
# def intersecao(lista01, lista02):
#     resultado = []
#     for item in lista01:
#         if item in lista02 and item not in resultado:
#             resultado.append(item)
#     return resultado

# Versão com conjuntos
# def intersecao_conjuntos(lista01, lista02):
#     conjunto01 = set(lista01)
#     conjunto02 = set(lista02)
#     resultado = conjunto01.intersection(conjunto02)
#     return list(resultado)

# Questão 13. Escreva uma função Python união(lista01, lista02) que recebe duas listas e retorna uma
# terceira lista que contenha todos os elementos que estavam nas duas anteriores. A lista resultante não deve
# repertir elementos. Faça uma versão com laço e outra versão com conjuntos. Expresse a função T(n) para
# essa função.

# Versão com laço
# def uniao(lista01, lista02):
#     resultado = []
#     for item in lista01:
#         if item not in resultado:
#             resultado.append(item)
#     for item in lista02:
#         if item not in resultado:
#             resultado.append(item)
#     return resultado

# Versão com conjuntos
# def uniao_conjuntos(lista01, lista02):
#     conjunto01 = set(lista01)
#     conjunto02 = set(lista02)
#     resultado = conjunto01.union(conjunto02)
#     return list(resultado)

# Questão 14. Escreva uma função Python ordenar(lista) que recebe uma lista e orderna em ordem
# crestente seus elementos, simulando a funcionalidade de função sort(). Expresse a função T(n) para essa
# função.

# def ordenar(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lista[j] > lista[j+1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]
#     return lista



