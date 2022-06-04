"""
Condições If, Elif e Else
"""
num1 = input('num1: ')
num2 = input('num2: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    print(f'a soma é: {num1 + num2}')
except:
    print("tá louco?")
