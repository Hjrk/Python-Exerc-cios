#decisao 28
#file, alcatra e picanha
# <= 5, >5
# dinheiro, cartao 
m5 = {'file':4.90, 'alcatra':5.90, 'picanha':6.90}
M5 = {'file':5.80, 'alcatra':6.80, 'picanha':7.80}
pg = {'dinheiro':1, 'cartão':0.95}
t = input ('digite file, alcatra ou picanha: ')
q = input ('digite a quantidade em Kg: ')
p = input ('digite dinheiro ou cartão: ')
if t in m5 and q.isnumeric () and p in pg:
  if t == ('file') and int(q) <= 5 and p == 'dinheiro' :
    v = round (m5['file']*float(q),2)
    print (f" nota fiscal \v carne file \v quant {q} \v preço {v} \v pagamento dinheiro \v sem desconto \v a pagar {v}")
  elif t == ('file') and int(q) <= 5 and p == 'cartão' :
    v = round (m5['file']*float(q),2)
    v2 = v*0.95
    print (f" nota fiscal \v carne file \v quant {q} \v preço {v} \v pagamento cartão \v desconto 5 % \v a pagar {v2}")
  elif t == ('file') and int(q) > 5 and p == 'dinheiro' :
    v = round (M5['file']*float(q),2)
    print (f" nota fiscal \v carne file \v quant {q} \v preço {v} \v pagamento dinheiro \v sem desconto \v a pagar {v}")
  elif t == ('file') and int(q) > 5 and p == 'cartão' :
    v = round (M5['file']*float(q),2)
    v2 = v*0.95
    print (f" nota fiscal \v carne file \v quant {q} \v preço {v} \v pagamento cartão \v desconto 5 % \v a pagar {v2}")
  elif t == ('alcatra') and int(q) <= 5 and p == 'dinheiro' :
    v = round (m5['alcatra']*float(q),2)
    print (f" nota fiscal \v carne alcatra \v quant {q} \v preço {v} \v pagamento dinheiro \v sem desconto \v a pagar {v}")
  elif t == ('alcatra') and int(q) <= 5 and p == 'cartão' :
    v = round (m5['alcatra']*float(q),2)
    v2 = v*0.95
    print (f" nota fiscal \v carne alcatra \v quant {q} \v preço {v} \v pagamento cartão \v desconto 5 % \v a pagar {v2}")
  elif t == ('alcatra') and int(q) > 5 and p == 'dinheiro' :
    v = round (M5['alcatra']*float(q),2)
    print (f" nota fiscal \v carne alcatra \v quant {q} \v preço {v} \v pagamento dinheiro \v sem desconto \v a pagar {v}")
  elif t == ('alcatra') and int(q) > 5 and p == 'cartão' :
    v = round (M5['alcatra']*float(q),2)
    v2 = v*0.95
    print (f" nota fiscal \v carne alcatra \v quant {q} \v preço {v} \v pagamento cartão \v desconto 5 % \v a pagar {v2}")
  elif t == ('picanha') and int(q) <= 5 and p == 'dinheiro' :
    v = round (m5['picanha']*float(q),2)
    print (f" nota fiscal \v carne picanha \v quant {q} \v preço {v} \v pagamento dinheiro \v sem desconto \v a pagar {v}")
  elif t == ('picanha') and int(q) <= 5 and p == 'cartão' :
    v = round (m5['picanha']*float(q),2)
    v2 = v*0.95
    print (f" nota fiscal \v carne picanha \v quant {q} \v preço {v} \v pagamento cartão \v desconto 5 % \v a pagar {v2}")
  elif t == ('picanha') and int(q) > 5 and p == 'dinheiro' :
    v = round (M5['picanha']*float(q),2)
    print (f" nota fiscal \v carne picanha \v quant {q} \v preço {v} \v pagamento dinheiro \v sem desconto \v a pagar {v}")
  elif t == ('picanha') and int(q) > 5 and p == 'cartão' :
    v = round (M5['picanha']*float(q),2)
    v2 = v*0.95
    print (f" nota fiscal \v carne picanha \v quant {q} \v preço {v} \v pagamento cartão \v desconto 5 % \v a pagar {v2}")
else :
  print ('inválido')
#final