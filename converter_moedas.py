reais = float(input('Quanto dinheiro você tem na carteira?  R$ '))
dolar = reais / 4.86
print('Com R${:.2f} você pode comprar U$${:.2f}'.format(reais, dolar))