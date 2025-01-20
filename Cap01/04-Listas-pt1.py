lista_1 = ['arroz', 'feijão', 'leite', 'pão']

print(lista_1)

print(type(lista_1))

lista_3 = [1,2,'três', 'quatro']

print(lista_3)

# Indexação e slicing

item_1 = lista_1[0]

print(item_1)

# Remove um item da lista
del lista_1[1]
print(lista_1)

# Listas aninhadas
lista_aninhada = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# print(lista_aninhada)
print(lista_aninhada[0][2])

# sorted - ordena a lista retornando uma nova sem modificar a variável original
lista_aninhada = list(map(lambda item: sorted(item, reverse=True), lista_aninhada))
print(lista_aninhada)

# Concatenando listas

lista_2 = lista_1 + lista_3
lista_1.extend(lista_3)
print(lista_2)
print(lista_1)


lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Usar sort com map - o sort ordena a lista modificando a original e não retorna uma nova lista.
list(map(lambda item: item.sort(reverse=True), lista_aninhada))

print(lista_aninhada)