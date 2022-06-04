class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._on = False

    def on(self):
        if self._on:
            return
        self._on = True
        print(f'{self._nome} on')

    def off(self):
        if not self._on:
            return
        self._on = False
        print(f'{self._nome} off')
