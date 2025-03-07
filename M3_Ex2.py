from random import randint

def line():
    print("-" * 30)

def header(texto):
    print(texto)

class Carro:

    lista = []

    def __init__(self, nome, velocidade):
        Carro.lista.append(self)
        self.nome = nome
        self.velocidade = velocidade

    def correr(self):
        print(f"O carro {self.nome} está correndo à uma média de {self.velocidade} km/h")

        circuito = 5.891 * 52
        tempo = (circuito / self.velocidade) * 60
        tempo = int(tempo)
        self.tempo = tempo

        print(f"Finalizou a corrida em {tempo} minutos\n")

    @staticmethod
    def vencedor(opcao):
        vencedor = Carro.lista[0]

        for carro in Carro.lista:
            if carro.tempo < vencedor.tempo:
                vencedor = carro

        if opcao == vencedor:
            print("Parabéns, você ganhou!!!")
        else:
            print(f"O vencedor é o {vencedor.nome}, você perdeu.")

carro1 = Carro("Nissan Skyline GT-R", randint(250, 300))
carro2 = Carro("Toyota Supra", randint(250, 300))
carro3 = Carro("Mitsubishi Lancer Evolution", randint(250, 300))

line()
header("RACE SIMULATOR".center(30))
line()
print("\nCarros na garagem: \n")
i = 1
for carro in Carro.lista:
    print(f"{i} - {carro.nome}")
    i += 1
print()

opcao = int(input("Escolha o seu carro: "))
print()
if opcao in [1, 2, 3]:
    carro_escolhido = Carro.lista[opcao - 1]
    print(f"Você escolheu o carro: {carro_escolhido.nome}\n")

    for carro in Carro.lista:
        carro.correr()

    Carro.vencedor(carro_escolhido)
else:
    print("Escolha inválida. Por favor, selecione 1, 2 ou 3.")

