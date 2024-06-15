num = int(input('Digite um número inteiro: '))
print('''Escolha as bases de conversão:
[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL''')
opção = int(input('Digite uma opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL É {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tebte novamente')



