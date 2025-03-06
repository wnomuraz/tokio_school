def linha():
    print("=" * 30)

def header(texto):
    print(texto.center(30))

class Aluno():
    def __init__(self, nome="undefined", idade=0, curso="undefined", matricula=000000):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matricula = matricula

    @staticmethod
    def menu():
        print("1 - Criar um novo aluno\n"
              "2 - Exibir informações de um aluno\n"
              "3 - Sair\n")

        option = int(input("Digite sua opção: "))
        return option

alunos = []

linha()
header("Sistema de gestão de alunos")
linha()

while True:
    option = Aluno.menu()

    if option == 1:
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")
        matricula = int(input("Digite o número de matrícula do aluno: "))

        aluno = Aluno(nome, idade, curso, matricula)
        alunos.append(aluno)
        print("\nAluno criado com sucesso!\n")

    elif option == 2:
        matricula = int(input("Digite o número da matrícula do aluno: "))

        aluno_encontrado = None
        for aluno in alunos:
            if matricula == aluno.matricula:
                aluno_encontrado = aluno
                break
        if aluno_encontrado:
            print("\nInformações do Aluno:\n")
            print(f"Nome: {aluno_encontrado.nome}")
            print(f"Idade: {aluno_encontrado.idade} anos")
            print(f"Curso: {aluno_encontrado.curso}")
            print(f"Número de Matrícula: {aluno_encontrado.matricula}\n")
        else:
            print("Aluno não encontrado!")

    elif option == 3:
        print("Saindo... Obrigado por usar o sistema de gestão de alunos!")
        break

    else:
        print("Opção inválida! Tente novamente.")


