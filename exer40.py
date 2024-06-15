n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média fica {:.1f}'.format(n1, n2, média))
if média < 5:
    print('Aluno reprovado')
elif 7 > média >= 5:
    print('Aluno em recuperaçaõ')
else:
    var = média >= 5
    print('Aluno aprovado')




