estudante = {
      'nome': 'Marcelo',
      'idade': 21,
      'curso': 'Curso em vídeo'
}
estudante['endereco'] = 'Rua Da Luz'

print(estudante)

# del - exclui o dicionário da memória
# del estudante

print(estudante)

# retorna a quantidade de pares
print(len(estudante))
print(estudante.items())
print(list(map(lambda item: list(item),estudante.items())))