#conversão base numérica binário/octal/hexadecimal
num = int(input('Digite um número: '))
print('''Escolaha uma das bases para conersão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) # 2: para retirart referências 0x da resposta
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida! Tente novamente.')