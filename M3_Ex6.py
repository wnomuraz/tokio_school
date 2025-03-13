class ContaBancaria():
    def __init__(self, nome, numeroConta, saldo):
        self.__nome = nome
        self.__numeroConta = numeroConta
        self.__saldo = saldo

    def depositar(self, montante):
        if montante > 0:
            self.__saldo += montante

    def levantar(self, montante):
        if self.__saldo >= montante:
            self.__saldo -= montante

    def info(self):
        print(f"Nome do cliente: {self.__nome}")
        print(f"Número da conta: {self.__numeroConta}")
        print(f"Saldo disponível: EUR {self.__saldo}")

conta = ContaBancaria("Willian Nomura", 101010, 150000)
conta.info()
conta.depositar(25000)
conta.info()
conta.levantar(75000)
conta.info()