c = ''
while c != 's':
    num1 = ''
    num2 = ''
    op = ''
    while not num1.isnumeric():
        num1 = input('num1: ')
    while not (op == '+' or op == '-'):
        op = input('+ ou -: ')
    while not num2.isnumeric():
        num2 = input('num2: ')
    if op == '+':
        print(f'------------------')
        print(f'{num1} + {num2} = {int(num1) + int(num2)}')
    else:
        print(f'------------------')
        print(f'{num1} - {num2} = {int(num1) - int(num2)}')
    print(f'------------------')
    c = input('tecle "s" para sair: ')
