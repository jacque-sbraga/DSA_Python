def ordenacao_personalizada(lista:list):
      """
      Recebe uma lista de inteiros e retorna a lista com ímpares antes dos pares, mantendo a ordem relativa.
      """
      impares = list(filter(lambda item: item % 2 != 0, lista))
      pares = list(filter(lambda item: item % 2 == 0, lista))
      
      impares = sorted(impares)
      pares = sorted(pares)
      
      return impares + pares

print(ordenacao_personalizada([5,2,1,10,4,9]))