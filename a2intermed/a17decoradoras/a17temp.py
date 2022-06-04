from time import time
from random import random
from time import sleep

def velocidade(func):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = func(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função {func.__name__}'
              f'levou {tempo:.2f}ms executando')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(6):
        r = random()
        print(f'{i}, {r:.2f}', end=' - ')
        sleep(r)

for i in range(3):
    demora()
    if i < 2:
        print('----------------------------')
