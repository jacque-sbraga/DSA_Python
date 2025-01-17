def soma_pares(lista:list):
      """
      Recebe uma lista de inteiros e retorna a soma de todos os números pares.
      """
      return sum([item for item in lista if item % 2 == 0])
print(soma_pares([1,2,3,5,7]))