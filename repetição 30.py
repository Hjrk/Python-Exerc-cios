#Nr 30
import csv
with open ('panificadora.csv', 'w') as t:
 p = csv.writer (t)
 print ("Preco do Pão: R$0,18 \vPanificadora Pão de Ontem - Tabela de Preços")
 for n in range (50):
  s = lambda n:0.18*n
  y = round (s(n), 2)
  p.writerow ((n, '-', y))
with open ('panificadora.csv', 'r') as tb:
 r = csv.reader (tb)
 for x in r:
   print (x)
 