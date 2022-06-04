def ola():
    return 'oi'

def main(func):
    return func()

v1 = main(ola)
print(v1)

def f1(fun, *args, **kwargs):
    return fun(*args, **kwargs)

def oi(nome):
    return f'Hi {nome}'

def sauda(nome, saudac):
    return f'{saudac} {nome}'

exec = f1(oi, 'vc')
print(exec)

ex = f1(sauda, saudac='hiih', nome='todos')
print(ex)
