def frequencia_numeros(lista:list):
      """
      Recebe uma lista de inteiros e retorna um dicionário com os números e suas frequências.
      """
      frequencia : dict = {}

      for numero in lista:
            if numero in frequencia:
                  frequencia[numero] += 1
            else:
                  frequencia[numero] = 1

      return frequencia

print(frequencia_numeros([1,1,1,1,2,1,2,3,4,1,3]))