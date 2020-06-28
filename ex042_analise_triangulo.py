print('\033[1;31m-='*20)
print(' '*8, '\033[4;31m ANÁLISE DE TRIÂNGULO \033[m')
m1 = float(input('Primeira medida: '))
m2 = float(input('Segunda medida: '))
m3 = float(input('Terceira medida: '))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
   print('\033[4;31mForma um retângulo \033[m', end='')
   if m1 == m2 == m3:
       print('\033[4;31mEQUILÁTERO \033[m')
   elif m1 != m2 != m3 != m1:
       print('\033[4;31mESCALENO \033[m')
   else:
       print('\033[4;31mISÓSCELES \033[m')
else:
    print('\033[4;31mCom estás medidas não da para montar um retângulo\033[m')

