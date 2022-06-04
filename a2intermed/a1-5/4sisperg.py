perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qto é 2+2?',
        'respostas': {'a':'1','b':'4','c':'5',},
        'resp_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Qto é 3*2?',
        'respostas': {'a': '4', 'b': '9', 'c': '6' },
        'resp_certa': 'c'
    }
}

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resp = input('Resp: ')
    if resp == pv['resp_certa']:
        print('certô misaravi')
    else:
        print('errô infeliz')
