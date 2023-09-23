#é número primo?
num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes,'.format(num, tot), end='')
if tot == 2:
    print('por isso, é um número Primo.')
else:
    print('por isso, Não é um número Primo.')
