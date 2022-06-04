num1 = ''
num2 = ''
while not num1.isnumeric():
    num1 = input('num1: ')
while not num2.isnumeric():
    num2 = input('num2: ')
num2 = int(num2)
num1 = int(num1)
print(f'A soma é: {num1 + num2}')

