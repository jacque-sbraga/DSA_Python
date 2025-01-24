# while - enquanto a condição for verdadeira, executa as operações

valor = 0

# Para entrar no loop, a condição precisa ser verdadeira pelo menos uma vez
while valor < 10:
      print(valor)

      # a condição deixará de ser verdadeira em um momento. Sem isso dá loop infinito
      valor += 1

# usando else para encerrar o loop while

x = 0
while x < 10:
      print(x)
      x += 1
else:
      print('loop concluído')

# pass, break e continue

valor = 0
while valor < 10:

      if valor == 4:

            # para o loop
            break
      else:
            # passa - usado quando uma declaração de código é obrigatória, mas não quer executar uma ação no momento
            pass 
      print(valor)

      valor += 1

# continue - passa para a próxima iteraçao

