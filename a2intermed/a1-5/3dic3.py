clientes = {
    'clinte1': {
        'nome': 'jo',
        'sobrenome': 'santos'
    },
    'clinte2': {
        'nome': 'ze',
        'sobrenome': 'silva'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
