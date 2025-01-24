lista1 = [1,2,3,4,5]
lista2 = [2,4,6]

for item1 in lista1:
      for item2 in lista2:
            print(item1 * item2)
            
      print('-----------')

# Concatenação de listas

print(lista1 + lista2) # concatenação das listas

# Loop em dicionários

dictionary = {'k1': 'python', 'k2': 'R', 'k3': 'Scala'}

for item in dictionary:
      print(item) # itera sobre as chaves

# items() retorna os pares chave:valor
for chave, value in dictionary.items():
      print(f'{chave}: {value}')