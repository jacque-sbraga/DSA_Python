lista_1 = ['arroz', 'feijão', 'leite', 'pão']

# len - retorna o tamanho da lista

numeros = [10000,1254949,1,2]
# retorna o valor máximo da lista (números)
print('max:', max(numeros))

# append - adiciona um novo item no final da  - não verifica se já existe o item na lista
numeros.append(-4)
numeros.append(-4)

# count - conta quantas vezes aparece o número na lista
print('count:',numeros.count(-4))
print(numeros)

# Filtrar itens únicos na lista
nao_duplicados = list(set(numeros))
print(nao_duplicados)

# Lista só com itens únicos
lista_2 = [item for item in set(numeros)]

print(lista_2)

# index - retorna o indice de um elemento na lista e retorna erro caso não exista
print(lista_2.index(-4))

# retorna erro caso o item não esteja presente na lista
# print(lista_2.index(-5))

# insert - insere um novo item na lista com base em um indice informado(obrigatório)
lista_2.insert(0,-5)

print(lista_2)

lista_2.remove(-5)

# remove - remove um elemento da lista e retorna erro caso o item não exista
print(lista_2)

# Erro - o item não está presente na lista
# print(lista_2.remove(-5))