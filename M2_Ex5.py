import sys
from time import sleep

sleep(1)
print('\033[1;34mTHE PANDORA ISLAND LOST TREASURE\033[0m\n')
sleep(1)
start = input('Pressione ENTER para começar... ')
if start == '':
    sleep(1)
    print('\nNa Ilha de Pandora, um navio português, o São Vicente, naufragou no século XVII, carregado de riquezas.\n'
          'Antes de sucumbir, o capitão, perdido em desespero, escondeu o tesouro em um local secreto.\n'
          'Dizem que sua alma, amaldiçoada, vaga pela ilha, guiando aqueles que buscam o ouro, mas também os condenando à perdição.\n'
          'O mapa que ele deixou é uma ilusão, e a névoa eterna que cobre a ilha esconde mais do que o tesouro — ela guarda os segredos de almas perdidas há gerações.\n')
sleep(1)
print('Será que você é capaz de encontrar o misterioso tesouro?\n')
sleep(1)
start = str(input('Pressione ENTER para continuar... '))
if start == '':
    sleep(1)
    print('\nFase 1: Chegada à Ilha\n')
    sleep(1)
    print('Bem-vindo (ou não) à Ilha de Pandora, uma ilha misteriosa e envolta por uma densa névoa.\n'
          'O vento uiva e as árvores balançam como se sussurrassem segredos do passado.\n'
          'O mapa enigmático está em suas mãos, mas a sua jornada não será fácil.\n')
    sleep(5)
    print('Você irá agora iniciar a sua busca, escolha a opção A ou B:\n')
    sleep(1)
    print('Opção A: Explorar a praia, onde algumas relíquias de náufragos podem fornecer pistas.\n'
          'Opção B: Dirigir-se para a floresta, onde sombras estranhas se movem, indicando possíveis pistas ou armadilhas.\n')

    fase1 = str(input('Qual caminho quer seguir? (A ou B) -> '))
    if fase1 == 'A' or fase1 == 'a':
        sleep(2)
        print('\nVocê segue até a praia, o som das ondas quebrando contra as pedras ecoa no ar.\n'
              'Entre as rochas, encontra vestígios de uma embarcação antiga e, entre eles, um pequeno baú enferrujado.\n'
              'Dentro, há uma chave antiga, aparentemente feita de ouro. O mapa mostra um símbolo que combina com a chave.\n'
              'Agora, você tem um artefato que pode ser útil mais à frente!\n')
    elif fase1 == 'B' or fase1 == 'b':
        sleep(2)
        print('\nVocê se aventura na floresta densa, mas rapidamente percebe que algo está errado.\n'
              'O vento começa a soprar com força, e os sons da floresta se tornam cada vez mais assustadores.\n'
              'De repente, uma sombra estranha se aproxima e, antes que possa reagir, um monstro místico emerge das árvores, atacando-o.\n'
              'Não há escapatória. \033[1;31mGAME OVER!\033[0m Você se perdeu na floresta e foi derrotado pela criatura.\n')
        sys.exit()

    sleep(5)
    print('Fase 2: A Floresta Sombria\n')
    sleep(1)
    print('Você agora está na praia e, seguindo seu caminho, avista a densa floresta à sua frente.\n'
          'Você sente uma leve tensão no ar, como se algo estivesse observando você.\n')
    sleep(1)
    print('Opção A: Seguir para a floresta, onde há um antigo altar de pedra coberto de musgo. A atmosfera está carregada de mistério e há um enigma que precisa ser resolvido.\n'
          'Opção B: Explorar mais a praia, onde mais vestígios do naufrágio podem dar pistas sobre o tesouro.\n')
    sleep(1)
    fase2 = str(input('Qual caminho quer seguir? (A ou B) -> '))
    if fase2 == 'A' or fase2 == 'a':
        sleep(1)
        print('\nVocê decidiu seguir pela floresta e encontrou o antigo altar. Será capaz de decifrar o enigma?')
        sleep(2)
        resposta = str(input('\n\033[3;34m"Sou leve como uma pena, mas posso afundar um navio. Ninguém pode me ver, mas todos me sentem.\n'
                             'Quem sou eu?" \033[0m'))
        while resposta.lower() != 'vento':
            resposta = str(input('Resposta incorreta! Tente novamente ou digite DESISTIR para encerrar o jogo. -> '))
            if resposta.lower() == 'desistir':
                print('\nVocê foi bem até aqui, mas realmente isso não é para todos. \033[1;31mGAME OVER!\033[0m')
                sys.exit()
        if resposta.lower() == 'vento':
            sleep(1)
            print('\nVocê pensa um momento e, de repente, a resposta vem à sua mente: \033[1;3m"Vento!"\033[0m\n'
            'O altar de pedra começa a brilhar suavemente e uma passagem secreta se abre à sua frente.\n'
            'Dentro, você encontra uma espada antiga que brilha com um brilho etéreo.\n'
            'A espada será essencial para enfrentar os perigos da jornada mais à frente.\n')
            sleep(1)
            print('Você decifrou o enigma e conseguiu encontrar a espada mágica, um artefato importante para a próxima fase da sua jornada!\n')
    elif fase2 == 'B' or fase2 == 'b':
        sleep(2)
        print('\nVocê explora mais a praia, mas a névoa vai ficando mais densa e você começa a se sentir desorientado.\n'
              'Encontrando algumas pedras grandes, você tenta atravessar para um ponto mais seguro, mas logo percebe que se afastou da trilha principal.\n'
              'Em algum momento, você escorrega em uma rocha molhada e cai, se machucando gravemente!\n'
              '\033[1;31mGAME OVER!\033[0m'
              ' Você se perdeu na praia e não conseguiu continuar a jornada.')
        sys.exit()

    print('Fase 3: Jornada final, o caminho do tesouro.\n')
    sleep(1)
    print('Após ter superado as fases anteriores, você se encontra em uma encruzilhada dentro da floresta.\n'
          'O ar está carregado de tensão, e a sensação de que algo grande está prestes a acontecer é palpável.\n'
          'Dois caminhos se abrem à sua frente, e cada um leva a um destino misterioso.\n'
          'Esse será o seu último teste de coragem e sabedoria, antes de enfrentar o grande desafio final.\n')
    sleep(5)
    print('Opção A: Caverna Misteriosa: O caminho desce para as profundezas da terra, onde um enigma sombrio o aguarda, guardado pelas sombras.\n'
          'Opção B: Montanha Elevada: Uma escalada árdua até o topo da montanha, onde o vento cortante traz o enigma final, te desafiando a alcançar seu destino.\n'
          '')
    sleep(1)
    fase3 = str(input('Qual caminho quer seguir? (A ou B) -> '))
    if fase3 == 'A' or fase3 == 'a':
        sleep(1)
        print('\nVocê segue pelo caminho da Caverna Misteriosa, sentindo a atmosfera carregada de mistério e suspense.\n'
              'Cada passo ecoa nas paredes rochosas, e à medida que você se aprofunda, a escuridão parece envolver você.\n'
              'Mas, então, no fim de um longo corredor, você encontra uma grande sala, iluminada apenas por uma luz tênue que emana das paredes.\n'
              'No centro da sala, uma pedra gigante repousa sobre uma base de ouro gasto, e nela há um enigma esculpido.\n'
              'Você se aproxima e lê as palavras gravadas, enquanto uma voz misteriosa sussurra no fundo da caverna:\n'
              '\n'
              '\033[3m\033[34m"Eu sou a chave para riquezas escondidas e para tesouros perdidos.\n'
              'Minha essência não é de ouro, mas minha busca já foi o fim de muitos.\n'
              'Eu não sou visto, mas posso ser tocado.\n'
              'Sou o que os piratas sempre procuraram, mas jamais encontraram."\033[0m\n')
        sleep(1
              )
        resposta = str(input('O que é? -> '))
        while resposta.lower() != 'sorte':
            resposta = str(input('\nResposta incorreta! Tente novamente ou digite DESISTIR para encerrar o jogo. -> '))
            if resposta.lower() == 'desistir':
                sleep(1)
                print('\nVocê foi bem até aqui, mas realmente isso não é para todos. GAME OVER!')
                sys.exit()
        if resposta.lower() == 'sorte':
            sleep(1)
            print('\nA sala parece silenciar enquanto você reflete sobre o enigma.\n'
             'As palavras parecem evocar imagens de aventuras antigas e caças ao tesouro, mas a resposta clara aparece em sua mente.\n'
             '\nVocê diz, com confiança: \033[1;3m"Sorte!"\033[0m\n'
             '\nAssim que você fala a palavra, uma suave vibração percorre a caverna, e a pedra no centro da sala se move, revelando uma passagem secreta.\n'
             'A luz dourada que ilumina o caminho agora brilha mais intensamente, e você sente que o destino está ao seu alcance.\n'
             '\nVocê \033[1;32mVENCEU!\033[0m O tesouro que procurava não era ouro, mas a sabedoria para encontrar o caminho certo.\n'
             'A caverna se abre para você, e você avança para o futuro, sabendo que a sorte foi a chave que desvenda os maiores mistérios da vida.')
    if fase3 == 'B' or fase3 == 'b':
            print('\nVocê decidiu enfrentar o caminho da Montanha Elevada, acreditando que a escalada é o teste final.\n'
                  'A subida é difícil, com ventos fortes e nuvens pesadas obscurecendo sua visão.\n'
                  'Cada passo é uma luta contra os elementos, mas sua determinação o mantém firme.\n'
                  'Finalmente, quando chega ao topo, você se encontra diante de um cenário desolador.\n'
                  'Em vez de um enigma, uma força inesperada surge, e uma voz ecoa, carregada de desaprovação:\n'
                  '\n'
                  '\033[3;34m"Você procurou por força, mas esqueceu o que realmente importa na jornada.\n'
                  'O tesouro não é encontrado apenas pela força, mas pela sabedoria em ouvir os ventos da sorte."\033[0m\n'
                  '\n'
                  'O vento aumenta, e você sente sua energia ser drenada.\n'
                  'A montanha parece não querer que você fique, e, em um último sopro violento, é arrastado para o abismo.\n'
                  '\n\033[1;31mGAME OVER!\033[0m A montanha o testou com sua força, mas você não estava preparado para o verdadeiro desafio.\n'
                  'Sua busca terminou, mas você agora sabe que a sorte é o verdadeiro guia para o tesouro da vida.')









