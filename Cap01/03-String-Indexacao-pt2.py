# Manipulação de texto - slicing (faz o fatiamento da string sem alterar o valor original)

s = 'Data Science Academy'

# Marca o indice inicial
print(s[1:])

# Marca a posição final, o valor é exclusivo (o valor não entra no resultado final)
print(s[:3])

print(s[:4])

# Último caractere, porém de traz para frente
print(s[-1])

# Retorna toda a string, com exceção da última letra
print(s[:-1])

# Usar a notação de indice para fatiar a string em pedaços especificos

# Usar dois pontos duas vezes em seguida o número que especifica o número de saltos dos elementos
print(s[::2])

# Usando essa notação inverte a string
print(s[::-1])

# String é um objeto imutável e não tem como mudar os seus elementos individualmente.
# s[0] = 'X'

# Operador de * repete a string pela quantidade especificada
letra = 'x' * 3
print(letra)