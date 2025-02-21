import sys
from time import sleep

print('Bem-vindo à calculadora de triângulos!')
while True:
    ladoA = float(input('\nDigite o comprimento do lado A: '))
    ladoB = float(input('Digite o comprimento do lado B: '))
    ladoC = float(input('Digite o comprimento do lado C: '))

    while ladoA + ladoB <= ladoC or ladoA + ladoC <= ladoB or ladoB + ladoC <= ladoA:
        print('\nTriângulo inválido. Digite novos valores para continuar: \n')
        ladoA = float(input('Digite o comprimento do lado A: '))
        ladoB = float(input('Digite o comprimento do lado B: '))
        ladoC = float(input('Digite o comprimento do lado C: '))

    sleep(0.5)
    continuar = input('\nPressione ENTER para calcular a área do triângulo... ')

    if continuar == '':
        s = (ladoA + ladoB + ladoC) / 2
        area = (s * (s - ladoA) * (s - ladoB) * (s - ladoC)) ** 0.5
        sleep(0.5)
        print(f'\nA área do triângulo é {area:.2f}')

    sleep(0.5)
    if ladoA == ladoB and ladoA == ladoC and ladoB == ladoC:
        print('Todos os lados são iguais, o triângulo é equilátero!')
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('Dois lados são iguais, o triângulo é isósceles!')
    else:s
        print('Todos os lados são diferentes, o triângulo é escaleno!')

    continuar = input('\nPressione ENTER para fazer outra operação ou digite EXIT para encerrar o programa: ')

    if continuar.lower().strip() == 'exit':
        print("Programa encerrado.")
        sys.exit()
