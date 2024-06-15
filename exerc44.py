print('{:=^40}'.format('LOJAS ANDRÉ'))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
{1} À VISTA DINHEIRO/CARTÃO:
[2} À VISTA CARTÃO:
{3} 2 X NO CARTÃO:
{4} 3 X NO CARTÃO OU MAIS:''')
opção = float(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)

elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2 x de  R$ {:.2f} sem juros'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totpar = int(input('Quantas parcelas? '))
    parcela = total / totpar
    print('Sua compra será parcelada em {} x fica em R$ {:.2f} com juros'.format(totpar, parcela))
else:
    total = 0
    print('Opção inválida de pagamento, Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar no final R$ {:.2f}'.format(preço, total))





