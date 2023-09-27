# dividindo uma lista em outras listas
# vários números, gerando 2 listas extras: os pares e os ímpares
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}' )
print(f'A lista pares é {pares}' )
print(f'A lista ímpares é {impares}' )

