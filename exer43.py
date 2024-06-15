peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (M)'))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}:'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')



