frase = input('frase: ')
tfrase = ''
tam = frase.__len__()
count = 0
maiusc = input('tornar maiusc: ')

while count < tam:
    print(f'{count}{frase[count]},', end="")
    if frase[count] == maiusc:
        tfrase = tfrase + frase[count].upper()
    else:
        tfrase = tfrase + frase[count]
    count += 1
    print(f'{tfrase}')
print(f'')
print(f'---------')
print(f'{tfrase}')

