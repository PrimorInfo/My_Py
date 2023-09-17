print('*'*20)
print('=== CHUTE&ACERTE ===')
print('*'*20)
num_secret = 72
chute = int(input('Digite um numero: '))
print('Você digitou: ', chute)

acertou = chute == num_secret
maior = chute > num_secret
menor = chute < num_secret

if(acertou):
    print('Você acertou! Parabéns!')
elif(maior):
    print('Você errou! O seu chute foi maior do que o Número Secreto. ')
elif(menor):
    print('Voce errou! O seu chute foi menor do que o Número Secreto. ')

