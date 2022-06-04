nome = input('Digite seu prenome: ')
nome_tam = nome.__len__()

if nome_tam <= 4:
    print(f'Nome curto')
elif nome_tam >= 5 and nome_tam <= 6:
    print(f'Nome normal')
else:
    print(f'Nome grande')
