from re import findall,IGNORECASE

def contar_vogais(s:str):
      """
      Recebe uma string e retorna o número de vogais.
      """
      return len(findall(r'[aeiou]',s,IGNORECASE))

print(contar_vogais('Jacqueline'))

