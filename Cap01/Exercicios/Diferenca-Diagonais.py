# Exercício 5: Diferença Absoluta
def diferenca_diagonais(matriz:list[list[int]]):
      """
      Recebe uma matriz quadrada e retorna a diferença absoluta entre as somas das diagonais.
      """
      linhas:int = len(matriz)

      soma_diagonal_principal = 0
      soma_diagonal_secundaria = 0
      for linha in range(0, linhas):
            colunas = len(matriz[linha]) - 1
      
            soma_diagonal_principal += matriz[linha][linha]
            
            soma_diagonal_secundaria += matriz[linha][colunas-linha]
            
      return soma_diagonal_principal - soma_diagonal_secundaria
            

# print([
#       [2, 0, 0],
#       [0, 3, 0],
#       [0, 0, 4]
# ])

print(diferenca_diagonais([
      [2, 0, 0],
      [0, 3, 0],
      [0, 0, 4]
]))