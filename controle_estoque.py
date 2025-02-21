print('Controle de estoque\n')

estoque = []

def cadastrarProduto(nome, quantidade, preco):
    produto = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
    estoque.append(produto)

while True:
    print('1: Cadastrar Produto\n'
          '2: Adicionar Produto\n'
          '3: Remover Produto\n'
          '4: Visualizar Estoque\n'
          '5: Sair\n')

    try:
        acao = int(input('Escolha a opção desejada: '))

        if acao == 1:
            nome = input('Qual é o nome do produto? ')
            quantidade = int(input('Qual é a quantidade? '))
            preco = float(input('Qual é o preço de venda? € '))
            cadastrarProduto(nome, quantidade, preco)
            print(f'\nO produto {nome} foi cadastrado com sucesso!\n')

        elif acao == 2:
            nomeProduto = input('\nQue produto quer adicionar ao estoque? ')
            produtoEncontrado = False
            for produto in estoque:
                if produto['nome'].lower() == nomeProduto.lower():
                    quantidadeAdicional = int(input('Quantas unidades deseja adicionar? '))
                    produto['quantidade'] += quantidadeAdicional
                    print(f"Quantidade de {produto['nome']} atualizada! Agora temos {produto['quantidade']} unidadades no estoque.\n")

        elif acao == 3:
            nomeProduto = input('\nQue produto quer remover do estoque? ')
            produtoEncontrado = False
            for produto in estoque:
                if produto['nome'].lower() == nomeProduto.lower():
                    quantidadeRemover = int(input('Quantas unidades deseja remover? '))
                    if quantidadeRemover > produto['quantidade']:
                        print(f"Não é possível remover {quantidadeRemover} unidades, pois só há {produto['quantidade']} unidades em estoque.\n")
                    else:
                        produto['quantidade'] -= quantidadeRemover
                        print(f"Quantidade de {produto['nome']} atualizada! Agora temos {produto['quantidade']} unidadades no estoque.\n")
                    produtoEncontrado = True
                    break
                if not produtoEncontrado:
                    print(f"O produto {nomeProduto} não foi encontrado no estoque.\n")

        elif acao == 4:
            if not estoque:
                print('\nO estoque está vazio.\n')
            else:
                print('\nEstoque atual: ')
                for produto in estoque:
                    print(f"\nNome: {produto['nome']} | Quantidade: {produto['quantidade']} | Preço: € {produto['preco']:.2f}\n")

        elif acao == 5:
            print('O programa será encerrado.')
            break

        else:
            print('\nOpção inválida, tente novamente.\n')
    except ValueError:
        print('Entrada inválida! Por favor informe um número válido.\n')