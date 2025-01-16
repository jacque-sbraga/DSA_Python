# Python  tem a tipagem dinâmica - a variável é tipada pelo interpetrador dinamicamente
var_teste = 1

# Definindo o tipo da variável - type hints
var_teste: str = 1

# Só pode usar a variável se definir antes
print(var_teste)

# Declaração múltipla

# Assim é usado uma tupla e é feito o desacoplamento, onde cada elemento será atribuido a uma variável
pessoa_1, pessoa_2, pessoa_3 = ('Bob', 'Maria', 'Ana')

# Os valores são separados por vírgula e será atribuido a cada variável
pessoa_1, pessoa_2, pessoa_3 = 'Bob', 'Maria', 'Ana'
print(pessoa_1, pessoa_2, pessoa_3)

# Cada variável receberá o mesmo valor
fruta_1 = fruta_2 = fruta_3 = "Melancia"

print(fruta_1)

# Sinal de + -> usar com variáveis numéricas ele soma, usar com variáveis string ele concatena



