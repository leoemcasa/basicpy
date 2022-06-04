from conta import Conta

class Cc(Conta):
    def __init__(self, ag, conta, saldo, limite = 100):
        #super().__init__(ag, conta, saldo)
        Conta.__init__(self, ag, conta, saldo)
        self._limite = limite


    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
