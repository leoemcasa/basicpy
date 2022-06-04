num = ''
while not num.isnumeric():
    num = input('num: ')
num = int(num)
if num % 2 == 0:
    print(f'num par')
else:
    print(f'num impar')
