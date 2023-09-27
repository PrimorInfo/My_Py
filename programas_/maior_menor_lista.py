# maior menor em lista
listnum = []
maior = 0
menor = 0
for c in range(0, 5):
    listnum.append(int(input(f' Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listnum[c]
    else:
        if listnum[c] > maior:
            maior = listnum[c]
        if listnum[c] < menor:
            menor = listnum[c]
print('-=' * 30)
print(f'Você digitou os valores {listnum}')
print(f'Maior: {maior}, nas posições: ', end='')
for i, v in enumerate(listnum):
    if v == maior:
        print(f'{i}; ', end='')
print()
print(f'Menor: {menor}, nas posições: ', end='')
for i, v in enumerate(listnum):
    if v == menor:
        print(f'{i}; ', end='')

