from datetime import date
atual = date.today().year
nasc = int(input('Ano do nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Alistesse imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print('Você não tem 18 anos faltam {} para se alistar.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))



