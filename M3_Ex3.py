class Animal:
    def __init__(self, nome):
        self._nome = nome

    def emitirSom(self):
        print("O animal emite um som")

class Gato(Animal):
    def __init__(self, nome):
        self.nome = nome

    def miar(self):
        return "meooooooooooooow"

class Cao(Animal):
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return "ruff, ruff, ruff"



animal1 = Gato("Leônidas")
animal2 = Cao("Rex")

print(f"{animal1.nome} é um gato que faz {animal1.miar()}")
print(f"{animal2.nome} é um cão que faz {animal2.latir()}")