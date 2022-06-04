class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('rErrado!')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')
