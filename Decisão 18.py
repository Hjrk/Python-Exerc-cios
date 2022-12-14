#Exercicio Nr. 18
from datetime import date
x = []
while len(x) == 0:
 a = input('digite a data de seu nascimento: dd/mm/aaaa')
 b = a.split('/', 2)
 if len (b) == 3:
   if bool (date(year=int(b[2]), month=int(b[1]), day=int(b[0]))) :
     print ('data válida')
     x.append(1)
   else:
     print ('valor inesperado! tente novamente')
 else:
   print ('valor inesperado! tente novamente!')

