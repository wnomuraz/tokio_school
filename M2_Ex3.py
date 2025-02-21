print('Bem-vindo à escolha de caminho!\n')
print('Você têm 3 opções de caminho:\nCaminho A\nCaminho B\nCaminho C\n')
escolha = str(input('Escolha o caminho que quer seguir, digitando A, B ou C: '))
if escolha == 'A' or escolha == 'a':
    print('Você escolheu o caminho A: É um caminho seguro.')
elif escolha == 'B' or escolha == 'b':
    print('Você escolheu o caminho B: É um caminho difícil, mas que leva a direção correta.')
elif escolha == 'C' or escolha == 'c':
    print('Você escolheu o caminho C: É uma má escolha de caminho.')
else:
    print('Escolha inválida.')