# Tuplas - pode ser usadas como saídas
# É uma estrutura imutável, não tem como modificar após a criação
tupla1 = ('Geografia', 10, 'Matemática', 5, 'Inglês', 10)

# Não suporta deletar elementos, para isso é necessário deletar toda a tupla
# del tupla1['Geografia']

# Não tem como adicionar novos valores após a criação
# tupla1[7] = 'Português'

print(tupla1)
print(len(tupla1))

# Suporta slicing
print(tupla1[:2])

lista_tupla = list(tupla1)

print(lista_tupla)