def verificar_palindromo(s:str):
      """
      Recebe uma string e retorna 'YES' se for palíndromo, caso contrário 'NO'.
      """
      s = s.replace(' ', '')
      
      if s.lower()[::-1] == s.lower():
            
            return 'YES'
      
      return 'NO'

print(verificar_palindromo('a man a plan a canal panama'))