times = ('FLAMENGO', 'ATLÉTICO PR', 'BAHIA', 'BOTAFOGO',
    'ATLÉTICO MG', 'BRAGANTINO', 'PALMEIRAS', 'SÃO PAULO', 
    'INTERNACIONAL', 'CRUZEIRO', 'GRÊMIO', 'FORTALEZA',
    'CRICIÚMA', 'JUVENTUDE', 'CORÍNTIAS', 'FLUMINENSE',
    'VASCO', 'VITÓRIA', 'ATLÉTIGO GO', 'CUIABÁ')
print('--<' * 44)
print(f'Lista de times do Brasileirão: {times}')
print('--<' * 44)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('--<' * 44)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('--<' * 44)
print(f'Times em ordem alfabética: {sorted(times)}')
print('--<' * 44)
print(f'Hoje o FLUMINENSE está na {times.index("FLUMINENSE")}ª posição. ')
print('--<' * 44)