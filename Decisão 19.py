#Lista de Estrutura de Decisão Nr 19
x = []
while len (x) == 0 :
 a = input ('digite um número entre 0 e 999:')
 if a.isnumeric () :ascii()
   if int(a) < 1000 :
     b = list (a)
     if len (a) == 1 :
       b.append ('unidades')
       print (b)
       x.append(1)
     else:
       if len (a) == 2 :
         b.insert (1, 'dezenas e')
         b.append ('unidades')
         print (b)
         x.append (1)
       else:
         b.insert (1, 'centenas')
         b.insert (3, 'dezenas e')
         b.append ('unidades')
         print (b)
         x.append (1)
   else:
     print ('valor inesperado! tente novamente!')
 else:
   print ('valor inesperado')
       