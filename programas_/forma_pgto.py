# compra a vista e condições de pagto com e sem juros
print('{:=^40}'.format(' Lojas GUANABARA '))
preço = float(input('Prreço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/Pix
[2] à vista cartão
[3] 2X no cartão
[4] 3X ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço -(preço*10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total/2
    print('Sua compra será de 2X de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço *20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será de {}X de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('Opção Inválida! Tente novamente. ')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))