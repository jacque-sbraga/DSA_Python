# from platform import python_version

# print(python_version())

# Funções built-in -> são funções internas do python

# Operações aritméticos

# Soma +
print(4+4)

# Subtração -
print(4-1)

# Multiplicação *
print(4*2)

# Divisão /
print(4/2)

# Potência **
print(4**2)

# Módulo %
print(4%3)

# Como saber o tipo do dado/estrutura? type()
print(type(4)) # int
print(type(4.1)) # float
print(type("Texto...")) # str


# Cuidados com números float

print(3.1 + 3.4) # float + float = float

print( 4 + 4.0) # float + int = float

print(4 + 4) # int + int = int

print(4 / 2) # na divisão de inteiros o resultado será float

print( 4 // 2) # com duas barras o resultado será inteiro
print(4.1 // 3.5) # mesmo com duas barras o resultado será float


# Conversão float e int
print(float(3.0))
print(int(9.5))

# Conversão hexadecimal e binário
print(hex(394))
print(bin(286))

# Funções abs, round e pow
print(abs(-8)) # valor absoluto

print(round(9.5448784878, 1)) # retorna o número arredondado de acordo com o número de casas decimais informado

print(pow(2, 2))
