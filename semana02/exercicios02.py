# Questão 01. Qual a principal diferença entre uma Lista e uma Tupla ?
# Resposta: A principal diferença entre uma Lista e uma Tupla é que as Listas são mutáveis, ou seja, seus elementos podem ser alterados após a criação, enquanto as Tuplas são imutáveis, o que significa que seus elementos não podem ser modificados depois de serem definidos.

# Questão 02. Se você converter a lista [10, 20, 20, 30, 40, 40] em um Set, qual será o resultado final?
# Resposta: O resultado final será {40, 10, 20, 30}. Isso ocorre porque os Sets não permitem elementos duplicados, então todos os elementos repetidos são removidos.

# lista_original = [10, 20, 20, 30, 40, 40]
# meu_set = set(lista_original)
# print(meu_set)

# Questão 03. Dada a lista numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], utilize a acesso em sublistas para obter:
# a) Os três primeiros elementos.
# b) Os elementos do índice 5 ao 8

# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# tres_primeiros = numeros[0:3] 
# print(f"a) Três primeiros: {tres_primeiros}")
# indice_5_ao_8 = numeros[5:9]
# print(f"b) Índices 5 ao 8: {indice_5_ao_8}")

# Questão 04. Dada a string texto = "banana", como você usaria um dicionário para contar quantas vezes
# cada letra aparece? (Ex: {'b': 1, 'a': 3, 'n': 2}).

# texto = "banana"
# contagem = {}

# for letra in texto:

#     if letra in contagem:
#         contagem[letra] += 1

#     else:
#         contagem[letra] = 1

# print(contagem)

# Questão 05. Crie uma estrutura que represente uma lista de alunos, onde cada aluno é um dicionário
# contendo "nome" e uma lista de "notas". Como você acessaria a segunda nota do primeiro aluno?

# alunos = [
#     {"nome": "Alice", "notas": [85, 90, 78]},
#     {"nome": "Bob", "notas": [92, 88, 95]},
#     {"nome": "Charlie", "notas": [80, 85, 82]}
# ]

# segunda_nota_primeiro_aluno = alunos[0]["notas"][1]
# print(f"A segunda nota do primeiro aluno é: {segunda_nota_primeiro_aluno}")

# Questão 06. A partir de uma lista de nomes ['ana', 'bia', 'caio'], crie um dicionário onde a chave é o nome
# e o valor é o número de letras desse nome.

# nomes = ['ana', 'bia', 'caio']
# dicionario_nomes = {}
# for nome in nomes:
#     dicionario_nomes[nome] = len(nome)
# print(dicionario_nomes)

# Questão 07. Dada a lista de dicionários jogadores = [{'nome': 'A', 'pontos': 10}, {'nome': 'B', 'pontos': 50},
# {'nome': 'C', 'pontos': 30}], como você ordenaria essa lista pela pontuação (do maior para o menor)?

# jogadores = [
#     {'Carlos': 'A', 'pontos': 10}, 
#     {'Bob': 'B', 'pontos': 50}, 
#     {'Charlie': 'C', 'pontos': 30}
# ]
# jogadores.sort(key=lambda j: j['pontos'], reverse=True)
# print(jogadores)

# Questão 08. Imagine um sistema de e-commerce que precisa gerenciar os itens que um usuário adiciona
# ao carrinho. Crie uma lista vazia. Adicione três produtos ("Celular", "Fone", "Capa"). O usuário desistiu
# da "Capa"; remova-a. Ao final, exiba quantos itens restaram.

# carrinho = []
# carrinho.append("Celular")
# carrinho.append("Fone")
# carrinho.append("Capa")
# print(f"Carrinho após adição: {carrinho}")
# carrinho.remove("Capa")
# print(f"Carrinho após remoção: {carrinho}")
# print(f"Quantidade de itens restantes: {len(carrinho)}")

# Questão 09. Um mercadinho quer saber quantos quilos de cada fruta tem em estoque. Crie um
# dicionário com {"maçã": 10, "banana": 15}. Atualize o estoque de "banana" para 20 e adicione "uva"
# com 5. No final, imprima apenas as chaves (nomes das frutas) disponíveis.

# estoque = {"maçã": 10, "banana": 15}
# estoque["banana"] = 20
# estoque["uva"] = 5
# print(f"Frutas disponíveis: {list(estoque.keys())}")

# Questão 10. Escreva uma função Python imprimeLista(lista) que recebe uma lista de elementos e
# imprime todos os elementos.

# def imprimeLista(lista):
#     for elemento in lista:
#         print(elemento)
        
# minha_lista = [1, 2, 3, 4, 5,6,7,8,9,10]
# imprimeLista(minha_lista)

# Questão 10. Escreva uma função Python imprimeLista(lista) que recebe uma lista de elementos e
# imprime todos os elementos.

# def imprimeLista(lista):
#     for elemento in lista:
#         print(elemento)
# minha_lista = [1, 2, 3, 4, 5,6,7,8,9,10]
# imprimeLista(minha_lista)

# Questão 11. Escreva uma função Python somaTotal(numeros) que recebe uma lista de inteiros e imprime
# a soma total dos inteiros.

# def somaTotal(numeros):
#     soma = 0
#     for n in numeros:
#         soma += n
#     print(soma)

# minha_lista = [10, 20, 30, 40]
# somaTotal(minha_lista)

# Questão 12. O interpretador Python do computador do professor Arthur está corrompido e excluiu a
# função index(caractere) da String. Para corrigir essea falha, escreva uma função Python indice(texto,
# caractere) que recebe uma string e um caractere e retorne a posição do caractere dentro da string. de
# inteiros e imprime a soma total dos inteiros.

# def indice(texto, caractere):
#     for i in range(len(texto)):
#         if texto[i] == caractere:
#             return i
#     return -1

# texto = "banana"
# caractere = "n"
# posicao = indice(texto, caractere)
# if posicao != -1:
#     print(f"O caractere '{caractere}' está na posição {posicao} da string '{texto}'.")
# else:
#     print(f"O caractere '{caractere}' não foi encontrado na string '{texto}'.")

# Questão 13. Escreva uma função Python estaOrdenado(lista) que recebe uma lista de inteiros verifica se
# está ordenada.

# def estaOrdenado(lista):
#     for i in range(len(lista) - 1):
#         if lista[i] > lista[i + 1]:
#             return False
#     return True

# minha_lista = [1, 2, 3, 4, 5]
# if estaOrdenado(minha_lista):
#     print("A lista está ordenada.")
# else:    
#     print("A lista não está ordenada.")

# Questão 14. Escreva uma função Python divideNumeros(lista) que recebe uma lista de inteiros e retorna
# um dicionário no formato: {“pares”: [], “impares”: []} com a lista de números pares e outra lista de
# números impares.

# def divideNumeros(lista):
#     resultado = {"pares": [], "impares": []}
#     for numero in lista:
#         if numero % 2 == 0:
#             resultado["pares"].append(numero)
#         else:
#             resultado["impares"].append(numero)
#     return resultado

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resultado = divideNumeros(numeros)
# print(f"Números pares: {resultado['pares']}")
# print(f"Números ímpares: {resultado['impares']}")

# Questão 15. Escreva uma função Python removerInicio(dicionario) que recebe um dicionário no
# formato: {“1o”: “um”, “2o”: “dois”, “3o”: “três”, …}, remove o primeiro elemento, desloca os outros
# para posições anteriores e imprime o resultado. Por exemplo, ao executarmos uma vez teremos o
# resultado: {“1o”: “dois”, “2o”: “três”, “3o”: “quatro”, …}

# def removerInicio(dicionario):
#     valores = list(dicionario.values())
#     if valores:
#         valores.pop(0)
#     novo_dicionario = {}
#     for i, valor in enumerate(valores):
#         nova_chave = f"{i+1}o"
#         novo_dicionario[nova_chave] = valor
#     return novo_dicionario
# dicionario = {"1o": "um", "2o": "dois", "3o": "três", "4o": "quatro"}
# resultado = removerInicio(dicionario)
# print(resultado) 

# Questão 16. Escreva uma função Python juntarOrdenado(lista1, lista2) que recebe duas listas de
# inteiros ordenados e retorne uma nova lista que junta as duas listas anteriores na ordem correta.

# def juntarOrdenado(lista1, lista2):
#     resultado = []
#     i, j = 0, 0
#     while i < len(lista1) and j < len(lista2):
#         if lista1[i] < lista2[j]:
#             resultado.append(lista1[i])
#             i += 1
#         else:
#             resultado.append(lista2[j])
#             j += 1
#     resultado.extend(lista1[i:])
#     resultado.extend(lista2[j:])
#     return resultado

# lista1 = [1, 3, 5, 7]
# lista2 = [2, 4, 6, 8]
# resultado = juntarOrdenado(lista1, lista2)
# print(resultado)

# Questão 17. Escreva uma função Python ordenar(lista) que recebe uma lista de inteiros não ordenados e
# retorne a lista ordenada.

# def ordenar(lista):
#     for i in range(len(lista)):
#         for j in range(0, len(lista) - i - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#     return lista

# numeros = [64, 34, 25, 12, 22, 11, 90]
# resultado = ordenar(numeros)
# print("Lista ordenada:", resultado)

# Questão 18. Escreva uma função Python ordenarAlunos(listaAlunos) que recebe uma lista de
# dicionários que representam alunos no formato: [{“nome”: “arthur”, “média”: “7.0”}, {“nome”:
# “josefina”, …} não ordenada e imprima os alunos ordenados por aluno.

# def ordenarAlunos(listaAlunos):
#     return sorted(listaAlunos, key=lambda aluno: aluno['nome'])
# alunos = [
#     {"nome": "Arthur", "média": 7.0},
#     {"nome": "Josefina", "média": 8.5},
#     {"nome": "Carlos", "média": 6.5}
# ]
# alunos_ordenados = ordenarAlunos(alunos)
# for aluno in alunos_ordenados:
#     print(f"Nome: {aluno['nome']}, Média: {aluno['média']}")