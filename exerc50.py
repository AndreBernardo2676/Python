soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    if num % 2 == 0:     # % 2 para apresentar só os números pares.
        soma += num
        cont += 1

print('Você informou {} números e a soma é {}'. format(cont, soma))





