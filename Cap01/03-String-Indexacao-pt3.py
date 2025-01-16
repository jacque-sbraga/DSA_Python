# Funções built-in de Strings

# Tudo em python é um objeto

s = 'Data Science Academy'

# transforma a string em maiusculo
print(s.upper())

# transforma a string em minúsculo
print(s.lower())

# Transforma a string em uma lista com base em um separador
print(s.split('a'))

# Verifica se a string termina com um caractere/string
print(s.endswith('my'))

# Verifica se a string é espaço
print(s.isspace())

# Operador in verifica se o valor está presente na string
print('Data' in s)

# == Comparando string
print('Data Science Academy' == s)