casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('Quanto você ganha? R$ '))
anos = int(input('Em quantos anos vai pagar? R$ '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('Seu empréstimo foi aprovado')
else:
    print('Empréstimo reprovado')


