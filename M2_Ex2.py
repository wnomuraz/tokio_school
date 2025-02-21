print('Bem-vindo à calculadora de média!')

class Calculadora:
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcularMedia(self):
        print(f'A sua média final é: {(self.nota1 + self.nota2 + self.nota3) / 3:.2f}')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = Calculadora(nota1, nota2, nota3)
media.calcularMedia()