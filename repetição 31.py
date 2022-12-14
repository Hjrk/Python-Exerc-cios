#Nr 31
print ('Lojas Tabajara')
x = [1]
y = []
while len(y) < 1:
 i = input (f"Produto {len(x)}: R$ ")
 if i.isnumeric:
   if float (i) != 0:
     x.append(float(i))
   else :
     y.append (1)
     t = sum (x) - 1
     print (f"Total da compra: {t}")
     ii=input ('Valor que o cliente forneceu: R$ ')
     print (f"Troco: {float (ii) - t}")
 else:
   print ('entrada inválida')
#final