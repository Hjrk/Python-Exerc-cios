#Lista de Exercicios Estrutura de Decisao Nr. 26
litros_vendidos = input('Litros Vendidos:')
x = []
while len(x) == 0 :
 if litros_vendidos.isnumeric :
   tipo_combustivel = input('Tipo de Combustível: A/G')
   a = ['a', 'A']
   b = ['g', 'G']
   if tipo_combustivel in a :
     A = 1.90
     L = float (litros_vendidos)
     valor = L * A
     if L < 20 :
       valor2 = valor * 0.97
       print ('valor a ser pago', valor2)
       x = 1
     elif L >= 20 :
       valor2 = valor * 0.95
       print ('valor a ser pago', valor2)
       x = 1
   elif tipo_combustivel in b :
     G = 2.50
     L = float (litros_vendidos)
     valor = L * G
     if L < 20 :
       valor2 = valor * 0.96
       print ('valor a ser pago', valor2)
       x = 1
     elif L >= 20 :
       valor2 = valor * 0.94
       print ('valor a ser pago', valor2)
       x = 1
   else:
     print ('valor inesperado, tente novamente!')
 else :
   print ('valor inesperado, tente novamente!')
 break