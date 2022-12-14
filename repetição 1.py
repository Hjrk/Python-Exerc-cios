# Nr 1
x = []
while len (x) == 0:
  n = round (float (input ('insira uma nota entre 0 e 10: ')),3)
  if n >= 0 and n <= 10:
    x.append (1)
    print (f" nota: {n}")
    break
  else: 
    print ('entrada invalida')
#final
