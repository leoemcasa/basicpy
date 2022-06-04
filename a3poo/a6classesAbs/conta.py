from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, ag, conta, saldo):
        self._ag = ag
        self._conta = conta
        self._saldo = saldo

    @property
    def ag(self):
        return self._ag

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor deve ser número")
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor deve ser número")
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Ag: {self.ag}', end =' ')
        print(f'Conta: {self.conta}', end =' ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
