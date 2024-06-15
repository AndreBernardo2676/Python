salario = float(input('Quanto você recebe? R$'))
aumento = salario + (salario * 15 / 100)
print('Seu salario de R$ {:.3f} com o aumento de 15% passará a receber R$ {:.3f}'.format(salario, aumento))
