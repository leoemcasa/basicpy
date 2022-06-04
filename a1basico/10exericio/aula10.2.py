horas = ''
while not horas.isnumeric():
    horas = input('Digite uma hora entre 0 e 23: ')
horas = int(horas)
if horas >= 0 and horas <=11:
    print(f'Bom dia!')
elif horas >= 12 and horas <= 17:
    print(f'Boa tarde!')
elif horas >= 18 and horas <= 23:
    print(f'Boa noite!')
else:
    print(f'Que horas vc pensa que é?')
