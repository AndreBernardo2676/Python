distancia = float(input('Qual a distância do seu destino? '))
print('Você está prestes a iniciar uma viagem de {:.0f} KM'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Sua viagem vai custar R$ {:.2f}'.format(preço))

