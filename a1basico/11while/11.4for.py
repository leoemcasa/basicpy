frase = input('frase: ')
tfrase = ''
maiusc = input('tornar maiusc: ')

## for i in frase:
##    print(f'{i}')

for i in range(0, frase.__len__(), 1):
    if frase[i] == maiusc:
        tfrase = tfrase + frase[i].upper()
    else:
        tfrase += frase[i]
    print(f'{tfrase}')

"""while count < tam:
    print(f'{count}{frase[count]},', end="")
    if frase[count] == maiusc:
        tfrase = tfrase + frase[count].upper()
    else:
        tfrase = tfrase + frase[count]
    count += 1
    print(f'{tfrase}')
print(f'')
print(f'---------')
print(f'{tfrase}')"""

