# Conceituais

# Questão 01. Considere as funções T(n) listadas abaixo e indique o termo dominante e a notação Big-O.
# a) 2n + 4n^2 + 5n
# Termo Dominante: 2^n
# Notação Big-O: O(2^n)

# b) 3n^2 + 6
# Termo Dominante: 3n^2 (ou simplesmente n^2)
# Notação Big-O: O(n^2)

# c) n^3 + n^2- n
# Termo Dominante: n^3
# Notação Big-O: O(n^3)

# Questão 02. Considere as funções abaixo que representam o tempo de execução de quatro algoritmos
# distintos:
# f1. T(n) = 100n log n
# f2. T(n) = n² + 10n
# f3. T(n) = 2^n
# f4. T(n) = 5n³

# Assinale a alternativa que apresenta as funções na ordem de crescimento assintótico da menor para a
# maior:
# a) f3 < f2 < f1 < f4
# b) f4 < f3 < f2 < f1
# c) f2 < f1 < f4 < f3
# d) f1 < f2 < f4 < f3

# alternativa correta é a d) f1 < f2 < f4 < f3.

# Questão 03. Considere as funções T(n) listadas abaixo e prove que:
# a) 3n2 + 2n + 1 ∈ O(n2)
# b) 3n + 6 ∈ O(n)
# c) n3 + n2 - n ∈ O(n2)

# Respostas:

# a) 3n² + 2n + 1 ∈ O(n²)

# Para n >= 1:
#   2n <= 2n²   (pois n <= n²)
#   1  <= n²    (pois 1 <= n²)

# Logo:
#   3n² + 2n + 1 <= 3n² + 2n² + n² = 6n²

# Conclusão: tomando c = 6 e n0 = 1,
#   3n² + 2n + 1 <= 6n²  para todo n >= 1. ■

# b) 3n + 6 ∈ O(n)

# Para n >= 1:
#   6 <= 6n   (pois 1 <= n)

# Logo:
#   3n + 6 <= 3n + 6n = 9n

# Conclusão: tomando c = 9 e n0 = 1,
#   3n + 6 <= 9n  para todo n >= 1. ■

# c) n³ + n² - n ∈ O(n²)  --> AFIRMAÇÃO FALSA

# Prova por contradição:
#   Suponha que existam c > 0 e n0 tais que:
#     n³ + n² - n <= c * n²  para todo n >= n0

#   Dividindo por n² (n > 0):
#     n + 1 - (1/n) <= c

#   O lado esquerdo cresce sem limite quando n -> infinito,
#   logo nenhuma constante c pode satisfazer a desigualdade
#   para todo n suficientemente grande. Contradição. ■

#   O correto seria: n³ + n² - n ∈ O(n³)

#   Prova correta:
#   Para n >= 1:
#     n²  <= n³
#     -n  <  0 <= n³

#   Logo:
#     n³ + n² - n <= n³ + n³ = 2n³

#   Conclusão: tomando c = 2 e n0 = 1,
#     n³ + n² - n <= 2n³  para todo n >= 1.

# Cálculo de Complexidade

# Questão 04. Para os códigos a seguir, expresse a Complexidade do pior caso:
# def funcA(n):
#     # O(n) - um loop de 1 até n
#     if n == 0:
#         print("Vazio")
#     else:
#         for i in range(1, n+1):
#             print(i)


# def funcB(n):
#     # O(log n) - i dobra a cada iteração (i = i * 2)
#     i = 1
#     while i <= n:
#         i = i * 2
#         print(i)


# def funcC(n):
#     # O(log n) - i é dividido por 2 a cada iteração (i = i // 2)
#     i = n
#     while i >= 0:
#         i = i // 2
#         print(i)


# def funcD(n):
#     # O(2^n) - o loop vai de 1 até 2^n, dominando toda a função
#     k = 1
#     for i in range(1, 2**n + 1):
#         if (2**k % i == 0):
#             print("k= ", i)
#         k = k + 1

# Questão 05. Para os códigos a seguir, expresse a Complexidade do pior caso:
# def somar(a, b):
#     # O(1) - apenas uma operação aritmética, independente da entrada
#     soma = a + b
#     return soma


# def multiplicar(a, b):
#     # O(1) - apenas uma operação aritmética, independente da entrada
#     produto = a * b
#     return produto


# def potencializar(b, e):
#     # O(e) - o loop executa 'e' vezes, onde e é o expoente
#     potencia = 1
#     for i in range(e):
#         potencia *= b
#     return potencia

# Questão 06. Para os códigos a seguir, expresse a complexidade do pior caso:
# def somar(a, b):
#     # O(1) - apenas uma operação aritmética, independente da entrada
#     soma = a + b
#     return soma


# def multiplicar(a, b):
#     # O(b) - o loop executa 'b' vezes, chamando somar() que é O(1)
#     # O(b) * O(1) = O(b)
#     produto = 0
#     for i in range(b):
#         produto = somar(produto, a)
#     return produto


# def potencializar(b, e):
#     # O(e * b) - o loop executa 'e' vezes, chamando multiplicar() que é O(b)
#     # O(e) * O(b) = O(e * b)
#     potencia = 1
#     for i in range(e):
#         potencia = multiplicar(potencia, b)
#     return potencia

# Questão 07. A conversão de números decimais para binários efetua sucessivas divisões por 2 a fim de calcular o número na base binária. Ex: 13 em binário é 1101?
# # 13 // 2 = 6 , resto 1
# # 6 // 2 = 3, resto 0
# # 3 // 2 = 1, resto 1
# # 1// 2 = 0, resto 1
# def decimalBinario_01(n):
#     # O(log n) - o loop divide n por 2 a cada iteração (n = n // 2)
#     # assim como na funcC da questão 4, o número de iterações
#     # é igual à quantidade de bits necessários para representar n,
#     # que é log2(n)
#     if n == 0:
#         return "0"
    
#     binario = ""
#     while n > 0:
#         resto = n % 2
#         binario = str(resto) + binario
#         n = n // 2
#     return binario

# Questão 08. Considerando os códigos iterativos da busca sequencial e da busca binária, presuma que a
# lista possui chaves repetidas múltiplas vezes na lista. Neste caso, você deve retornar uma lista com todas
# as posições onde a chave foi encontrada. Se a chave não for encontrada na lista, retornar uma lista vazia.
# Implemente as funções python que realizam essa funcionalidade e calcule a complexidade no pior caso ?

# def busca_sequencial(lista, chave):
#     # O(n) - no pior caso percorre toda a lista
#     posicoes = []
#     for i in range(len(lista)):
#         if lista[i] == chave:
#             posicoes.append(i)
#     return posicoes


# def busca_binaria(lista, chave):
#     # O(n) - no pior caso a chave se repete muitas vezes,
#     # sendo necessário varrer toda a lista para coletar todas as posições.
#     # A busca binária pura é O(log n), porém como precisamos retornar
#     # TODAS as ocorrências, precisamos expandir para esquerda e direita
#     # a partir do índice encontrado, tornando o pior caso O(n)
#     posicoes = []
    
#     inicio = 0
#     fim = len(lista) - 1
#     indice_encontrado = -1

#     # Primeira etapa: busca binária para achar uma ocorrência — O(log n)
#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         if lista[meio] == chave:
#             indice_encontrado = meio
#             break
#         elif lista[meio] < chave:
#             inicio = meio + 1
#         else:
#             fim = meio - 1

#     # Se não encontrou nenhuma ocorrência, retorna lista vazia
#     if indice_encontrado == -1:
#         return posicoes

#     # Segunda etapa: expande para esquerda e direita — O(n) no pior caso
#     i = indice_encontrado
#     while i >= 0 and lista[i] == chave:
#         posicoes.insert(0, i)
#         i -= 1

#     i = indice_encontrado + 1
#     while i < len(lista) and lista[i] == chave:
#         posicoes.append(i)
#         i += 1

#     return posicoes


# # Exemplo de uso
# lista = [1, 2, 3, 3, 3, 3, 5, 6]
# chave = 3

# print("Busca Sequencial:", busca_sequencial(lista, chave))
# print("Busca Binária:   ", busca_binaria(lista, chave))