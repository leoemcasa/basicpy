"""
Condições If, Elif e Else
"""
num1 = input('num1: ')
num2 = input('num2: ')

if num1.isnumeric() and num2.isnumeric():
    print(num1[0])
    num1 = int(num1)
    num2 = int(num2)
    print(f'a soma é: {num1 + num2}')
elif num1.isnumeric() or num2.isnumeric():
    pass  # ou "..." sem aspas como placehold
else:
    print("tá louco?")