import random
import sys

print("Bem-vindo ao Tabuadex!\n")

print("""
\033[1mObjetivo do Jogo:\033[0m
Responda corretamente o maior número de problemas de tabuada para acumular pontos.

\033[1mComo Jogar:\033[0m
Você receberá uma sequência de perguntas de multiplicação. Responda rapidamente!
Cada resposta correta te dá pontos. Se errar, não perde tudo, mas não ganha pontos.

\033[1mVencedor:\033[0m
Quem tiver mais pontos ao final do jogo será o vencedor!

\033[1mDica:\033[0m
Se quiser sair do jogo a qualquer momento, digite 'SAIR' e pressione ENTER.

Boa sorte e divirta-se aprendendo a tabuada!
""")

iniciar = input("Pressione ENTER para continuar ou digite 'SAIR' para encerrar o jogo... ").strip().lower()
if iniciar == "sair":
    print("Jogo encerrado, até breve!")
    sys.exit()
elif iniciar == '':
    print("Vamos começar!\n")

pontos = 0
perguntas_feitas = 0

while True:
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)

    resposta = input(f"Qual é o resultado de {n1} x {n2}? ").strip().lower()

    if resposta == "sair":
        print(f"Jogo encerrado. Você respondeu {perguntas_feitas} perguntas corretamente e acumulou {pontos} pontos.")
        sys.exit()

    try:
        resposta_int = int(resposta)
        if resposta_int == n1 * n2:
            pontos += 10
            perguntas_feitas += 1
            print(f"Certa resposta! Você ganhou 10 pontos. Total de pontos: {pontos}. Perguntas feitas: {perguntas_feitas}")
        else:
            print("Resposta incorreta. Tente novamente!")
    except ValueError:
        print("Por favor, digite um número válido ou 'SAIR' para encerrar o jogo.")
