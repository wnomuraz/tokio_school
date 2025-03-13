from abc import ABC, abstractmethod
from idlelib.configdialog import help_pages
from xml.dom.expatbuilder import CDATA_SECTION_NODE


class Lutador(ABC):

    @abstractmethod
    def atacar(self, enemy):
        pass

    @abstractmethod
    def defender(self, damage):
        pass

    @abstractmethod
    def obterVida(self):
        pass

class Deadpool(Lutador):
    def __init__(self):
        self.hp = 100

    def atacar(self, enemy):
        damage = 25
        print("Deadpool ataca!")
        enemy.defender(damage)

    def defender(self, damage):
        self.hp -= damage
        print(f"Deadpool recebe {damage} de dano. HP restante: {self.hp}")

    def obterVida(self):
        return self.hp

class Wolverine(Lutador):
    def __init__(self):
        self.hp = 100

    def atacar(self, enemy):
        damage = 30
        print("Wolverine ataca!")
        enemy.defender(damage)

    def defender(self, damage):
        self.hp -= damage
        print(f"Wolverine recebe {damage} de dano. HP restante: {self.hp}")

    def obterVida(self):
        return self.hp

def exibirMenu():
    print("Escolha os personagens: \n"
          "1 - Deadpool\n"
          "2 - Wolverine\n")

def escolherPersonagem():
    while True:
        exibirMenu()
        escolha = int(input("Qual o personagem escolhido? "))

        if escolha == 1:
            return Deadpool()
        elif escolha == 2:
            return Wolverine()
        else:
            print("\nEscolha inválida.\n")

def batalha(p1, p2):
    while True:
        print(f"")

escolherPersonagem()
