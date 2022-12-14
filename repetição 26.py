#26
y = input ('insira o numero total de eleitores: ')
if y.isnumeric() and int (y) > 0:
  x = []
  v1 = []
  v2 = []
  v3 = []
  while len (x) < int (y) :
    a = input ('escolha seu voto: 1 - João, 2 - José, 3 - Joaquim')
    if int (a) == 1 :
      v1.append (1)
      x.append (1)
    elif int (a) == 2:
      v2.append (2)
      x.append (2)
    elif int (a) == 3:
      v3.append (3)
      x.append(3)
    else:
      print ('insira um numero valido')
  print (f" total de votos: \v candidato 1 = {len (v1)} \v candidato 2 = {len (v2)} \v candidato 3 = {len (v3)}")
      
    
