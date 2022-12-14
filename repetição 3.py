
#Nr 3
#nome +3c, idade <130, salário > 0, sexo f/m, estado civil s,c,v,d
x = []
while len(x) < 1:
 n = input ('insira seu nome: ')
 if len (list (n)) > 3:
   x.append (1)
 else:
   print ('nome inválido, precisa ter mais de 3 caracteres')
y = []
while len(y) < 1:
 i = input ('insira sua idade: ')
 if int (i) < 130:
   y.append (2)
 else:
   print ('idade inválida, limite de 130 anos')
z = []
while len(z) < 1:
 sl = input ('insira o salário: ')
 if int (sl) > 0:
   z.append (3)
 else:
   print ('salário inválido, precisa ser maior que zero')
w =[]
while len(w) < 1:
 sx = input ('digite o sexo f/m: ')
 sxx = ['f', 'F', 'm', 'M']
 if sx in sxx:
   w.append (4)
 else:
   print ('sexo inválido, digite (f ou m)')
u=[]
while len(u) < 1:
 ec = input ('digite o estado civil \v s-solteiro(a), c-casado(a), v-viuvo(a), d-divorciado(a): ')
 ecc = ['s', 'S', 'c', 'C', 'v', 'V', 'd', 'D']
 if ec in ecc:
   u.append (5)
 else:
   print ('nome inválido, precisa ter mais de 3 caracteres')
 print ('dados armazenados!')
#final