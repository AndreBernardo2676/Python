from random import randint
from time import sleep
computador = randint(0, 5)# Faz o computador sortear
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))#Jogador tenta adivinhar.
print('PROCESSANDO....')
sleep(2)
if jogador == computador:
    print('ACERTOU')
else:
    print('ERROU. Pensei em {} e não em {}.'.format(computador, jogador))







