from aeletronico import Eletronico
from alog import LogMixin


class Cellph(Eletronico, LogMixin):
    def __init__(self, nome):
        # super().__init__(nome)
        Eletronico.__init__(self, nome)
        self._online = False

    def connect(self):
        if not self._on:
            info = f'{self._nome} não conecta off'
            print(info)
            self.log_info(info)
            return
        if self._online:
            erro = f'{self._nome} já online'
            print(erro)
            self.log_error(erro)
            return
        info = f'{self._nome} online'
        self.log_info(info)
        self._online = True
        print(info)

    def disconnect(self):
        if not self._online:
            erro = f'{self._nome} já offline'
            print(erro)
            self.log_error(erro)
            return
        self._online = False
        info = f'{self._nome} offline'
        print(info)
        self.log_info(info)
