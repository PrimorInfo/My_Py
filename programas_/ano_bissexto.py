# ano bissexto ou não
from datetime import date
ano = int(input('Quer saber que ano é ´Bissexto?, (para ano atual 0). Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400 ==0:
    print('Ano digitado: {}, é BISSEXTO'.format(ano))
else:
    print('Ano digitado: {}, NÃO é BISSEXTO'.format(ano))

