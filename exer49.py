n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:.2f} = {:.2f}'. format(n, c, n * c))

