somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {}ª pessoa ------'. format(p))
    nome = str(input('Nome: ')).strip()  # o strip tira os espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        mairidadehomem = idade
        momevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        mairidadehomem = idade
        momevelho = nome
    if sexo in 'Ff' and idade < 20:
            totmulher20 += 1
mediaidade = somaidade / 4
print(' A média das idades é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com mais de 20 anos'.format(totmulher20))




