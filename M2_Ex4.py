import random

print('Bem-vindo ao jogo da adivinhação!\n'
      'O computador vai pensar em um número de 1 à 100, consegue adivinhar qual é?\n')

numero_secreto = random.randint(1, 100)
tentativas = 7
contador = 0
palpite = 0

while tentativas > 0 and palpite != numero_secreto:
    palpite = int(input('Tente adivinhar o número secreto: '))
    if numero_secreto > palpite:
        print('O número correto é maior do que o informado.')
    elif numero_secreto < palpite:
        print('O número correto é menor do que o informado.')
    tentativas -= 1
    contador += 1
if palpite == numero_secreto:
    print(f'Parabéns, você acertou em {contador} tentativas!')
else:
    print(f'Não foi dessa vez, o número que o computador pensou foi o {numero_secreto}')

