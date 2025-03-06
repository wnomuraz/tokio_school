class Conta:
    def __init__(self, titular, numeroDeConta, quantidade):
        self.titular = titular
        self.numeroDeConta = numeroDeConta
        self.quantidade = quantidade

    def comparar(self, outra_conta):
        if self.quantidade > outra_conta.quantidade:
            return f"{self.titular} tem mais dinheiro."
        elif self.quantidade < outra_conta.quantidade:
            return f"{outra_conta.titular} tem mais dinheiro."

titular1 = Conta("Willian Nomura", 1234, 1000)
titular2 = Conta("Kylian Mbappé", 9876, 9999)

print(titular1.comparar(titular2))
