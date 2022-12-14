#Lista de Exercícios Estrutura de Decisao Nr. 21
saque = input ('informe o valor do saque:')
saque2 = int(saque)
if saque.isnumeric():
  if saque2 >= 10 and saque2 <=600:
    notas_100 = int (saque2 / 100)
    notas_50 = int (saque2 % 100 / 50)
    notas_10 = int (saque2 % 50 / 10)
    notas_5 = int (saque2 % 10 / 5)
    notas_1 = int (saque2 % 5)
    print ('serão fornecidas', notas_100, 'notas de 100,', notas_50 ,'notas de 50,' ,notas_10 ,'notas de 10,', notas_5 ,'notas de 5 e', notas_1, 'notas de 1.')
else: 
 print ('valor inesperado')