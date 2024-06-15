print('-=-' * 20)
print('Analizador de segmento')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segunfo segmento: '))
r3 = float(input('Tercriro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento acima podem formar um triângulo!')
else:
    print('O segmento não pode formar um triângulo!')
    

    
    
    
        