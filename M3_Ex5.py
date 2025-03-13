from time import sleep


class FormaPagamento():
    def __init__(self, opcao):
        self.opcao = opcao

    def processarPagamento(self):
        print("\nO seu pagamento está sendo processado...")
        sleep(3)

class CartaoCredito(FormaPagamento):
    def __init__(self):
        super().__init__(1)

    def processarPagamento(self):
        super().processarPagamento()
        print("Você escolheu pagar com cartão de crédito.")
        sleep(1)
        print("Pagamento efetuado com sucesso!")

class PayPal(FormaPagamento):
    def __init__(self):
        super().__init__(2)

    def processarPagamento(self):
        super().processarPagamento()
        print("Você escolheu pagar com PayPal.")
        sleep(1)
        print("Pagamento efetuado com sucesso!")

print("-" * 30)
print("FORMAS DE PAGAMENTO".center(30))
print("-" * 30)
print("1 - Cartão de Crédito\n"
      "2 - Paypal\n")

while True:
    entrada = int(input("Qual a forma de pagamento? "))

    if entrada == 1:
        pagamento = CartaoCredito()
        break
    elif entrada == 2:
        pagamento = PayPal()
        break
    else:
        print("Opção inválida.")

pagamento.processarPagamento()