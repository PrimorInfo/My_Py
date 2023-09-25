# simulador de caixa eletrônico (qtas cédulas: de 50, 20, 10, 5, 1)
print('=' * 30)
print('{:^30}'.format('Banco NEO')) # print('     Banco NEO   ')
print('=' * 30)
valor = int(input('Qual o valor do saque? R$ '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'  Total de {totCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao "Banco NEO". Tenha um Bom dia!')
