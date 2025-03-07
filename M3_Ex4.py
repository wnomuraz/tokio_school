class Veiculo():
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def apresentar(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def apresentar(self):
        super().apresentar()
        print(f"O veículo tem {self.portas} portas")
        print()

class Moto(Veiculo):
    def __init__(self, marca, ano, quadriciclo):
        super().__init__(marca, ano)
        self.quadriciclo = quadriciclo

    def apresentar(self):
        super().apresentar()
        if self.quadriciclo:
            print("O veículo é um quadriciclo.")
        else:
            print("O veículo não é um quadriciclo.")
        print()

veiculo1 = Carro("Volkswagen", 2024, 5)
veiculo2 = Moto("Yamaha", 2024, True)

veiculo1.apresentar()
veiculo2.apresentar()
