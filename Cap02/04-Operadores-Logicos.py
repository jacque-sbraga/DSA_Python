# and - todas as regras devem ser verdadeiras

print(7 % 2 != 0 and 7 <= 10)

# or - pelo menos uma condição deve ser verdadeira

print(7 % 2 != 0 or 7 >= 10)

# not - inverte o resultado lógico (true - false | false - true)
print(not(7 % 2 != 0 or 7 >= 10)) # o resultado da expressão é true e com not vira false


# Placeholder
# %s -> string
# %d -> inteiro
# %f -> float 


nome = "Jacque"
idade = 29

mensagem = "Meu nome é %s e eu tenho %d anos." %(nome, idade)
print(mensagem)

# Se for usar format com placeholder nomeado, passar o valor para os placeholders
print("Meu nome é {nome} e eu tenho {idade} anos.".format(nome='Jacque', idade=29))

# Se for usar format com indice, passar os valores ou variáveis
print("Meu nome é {0} e eu tenho {1} anos.".format(nome, idade))

# Mais moderno e mais legível é com fstring
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

