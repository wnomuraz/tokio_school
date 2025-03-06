# Lista que vai armazenar os livros
estoque = []

# Função para cadastrar um livro
def cadastrarLivro(titulo, autor, quantidade, preco):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'quantidade': quantidade,
        'preco': preco
    }
    estoque.append(livro)  # Adiciona o livro à lista de estoque
    print(f"Livro '{titulo}' cadastrado com sucesso!")

# Função para adicionar mais livros ao estoque
def adicionarEstoque(titulo, quantidade_adicional):
    for livro in estoque:
        if livro['titulo'].lower() == titulo.lower():  # Procura o livro pelo título
            livro['quantidade'] += quantidade_adicional  # Adiciona a quantidade
            print(f"Quantidade de '{livro['titulo']}' atualizada! Agora temos {livro['quantidade']} unidades no estoque.")
            return
    print(f"Livro '{titulo}' não encontrado no estoque.")  # Caso o livro não seja encontrado

# Função para remover livros do estoque
def removerEstoque(titulo, quantidade_remover):
    for livro in estoque:
        if livro['titulo'].lower() == titulo.lower():  # Procura o livro pelo título
            if livro['quantidade'] >= quantidade_remover:  # Verifica se há livros suficientes
                livro['quantidade'] -= quantidade_remover  # Remove a quantidade
                print(f"Quantidade de '{livro['titulo']}' atualizada! Agora temos {livro['quantidade']} unidades no estoque.")
            else:
                print(f"Não é possível remover {quantidade_remover} unidades de '{livro['titulo']}'. Só há {livro['quantidade']} unidades no estoque.")
            return
    print(f"Livro '{titulo}' não encontrado no estoque.")  # Caso o livro não seja encontrado

# Função para visualizar o estoque
def visualizarEstoque():
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("\nEstoque Atual:")
        for livro in estoque:
            print(f"Titulo: {livro['titulo']} | Autor: {livro['autor']} | Quantidade: {livro['quantidade']} | Preço: € {livro['preco']:.2f}")

# Função para o menu principal
def menu():
    while True:
        print('\n1: Cadastrar Livro\n'
              '2: Adicionar Estoque\n'
              '3: Remover Estoque\n'
              '4: Visualizar Estoque\n'
              '5: Sair')

        try:
            acao = int(input('Escolha a opção desejada: '))

            if acao == 1:
                titulo = input('Qual é o título do livro? ')
                autor = input('Qual é o autor do livro? ')
                quantidade = int(input('Qual é a quantidade? '))
                preco = float(input('Qual é o preço do livro? € '))
                cadastrarLivro(titulo, autor, quantidade, preco)

            elif acao == 2:
                titulo = input('Que livro quer adicionar ao estoque? ')
                quantidade_adicional = int(input('Quantas unidades deseja adicionar? '))
                adicionarEstoque(titulo, quantidade_adicional)

            elif acao == 3:
                titulo = input('Que livro quer remover do estoque? ')
                quantidade_remover = int(input('Quantas unidades deseja remover? '))
                removerEstoque(titulo, quantidade_remover)

            elif acao == 4:
                visualizarEstoque()

            elif acao == 5:
                print('Saindo do sistema...')
                break  # Encerra o loop e sai do programa

            else:
                print('Opção inválida! Tente novamente.')

        except ValueError:
            print('Entrada inválida! Por favor, insira um número válido.')

# Chama a função do menu principal
menu()
