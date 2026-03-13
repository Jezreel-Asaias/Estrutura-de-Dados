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