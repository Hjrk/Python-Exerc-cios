# Nr 5
import math
x=[]
while len(x) == 0:
 h1 = input ('população 1: ')
 x1 = input ('digite a taxa de crescimento de população 1 em \% : ')
 h2 = input ('população 2: ')
 x2 = input ('digite a taxa de crescimento da população 2 em \% : ')
 if h1.isnumeric () and int (h1) > 0 and x1.isnumeric () and h2.isnumeric () and int (h2) > 0 and x2.isnumeric ():
   tempo = math.log (int(h1)/int(h2),int(x2)/int(x1))
   print (tempo, 'anos')
   x.append(1)
 else: 
  print ('digite apenas números')
#final