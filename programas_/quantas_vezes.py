frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes. '.format(frase.count('A')))
print('A primeira posição que A ocupa pela primeira vez: {}'.format(frase.find('A')+1))
print('A última posição que A ocupa pela última vez: {}'.format(frase.rfind('A')+1))
