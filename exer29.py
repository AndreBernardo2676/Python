velocidade = float(input('Está a quntos Km por hora?'))
if velocidade > 80:
    print('MULTADO. Você excedeu o limite de segurança que é de 80 KM por hora.'.format(velocidade))
    multa = (velocidade-80) * 7
    print('O valor de sua multa é R$ {:.2f}'.format(multa))
print('Tenha um bom dia, viage com segurança')



