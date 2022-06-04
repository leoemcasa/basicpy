import copy

v = ''
l1 = []
l2 = []
while v != 'q':
    v = input('Valor [(U)ndo, (R)edo, (Q)uit]: ').lower()
    if v == 'u':
        print(l2)
        continue
    if v == 'r':
        print(l1)
        continue
    else:
        l2 = copy.deepcopy(l1)
        l1.append(v)
        print(f'{l1}')
