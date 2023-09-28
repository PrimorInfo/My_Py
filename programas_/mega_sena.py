# palpites para a Mega sena: qtos jogos? sorteio entre 1 e 60; facça uma lista composta
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 25)
print('     Jogo da Mega Sena     ')
print('-' * 25)
quant = int(input('Quantos números você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
#print(f'Os números sorteados foram: {jogos}')
print('-=' * 5, f'  Sorteando {quant} Jogos  ', '-=' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 6, ' < BOA SORTE! >', '-=' * 7)



