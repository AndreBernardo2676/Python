n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu nome começa com {}'.format(nome[0]))
print('Seu nome termina com {}'.format(nome[len(nome) -1]))

