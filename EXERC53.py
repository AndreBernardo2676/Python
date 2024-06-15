frase = str(input('Escreva uma frase: ')).strip().upper() # espaços automático e maiúscula
palavra = frase.strip()
junto = "".join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase não é um palimdromo')
    

