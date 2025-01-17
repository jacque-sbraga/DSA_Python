# Exercício 4: Soma dos Elementos da Diagonal
def soma_diagonal(matriz:list[list[int]]):
      """
      Recebe uma matriz quadrada e retorna a soma da diagonal principal.
      """
      linhas:int = len(matriz)

      soma_diagonal:int = 0

      for linha in range(0, linhas):
      
            soma_diagonal += matriz[linha][linha]
            
      return soma_diagonal

print('[\n[1,2,3,4],\n[5,6,7,8],\n[8,9,10,11],\n[12,13,14,15]\n]')
print(soma_diagonal([
      [2, 0, 0],
      [0, 3, 0],
      [0, 0, 4]
]))