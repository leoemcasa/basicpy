"""cpf = 168.995.350-09 16899535009
1*10=10, 6*9=54, 8*8=64, 9*7=63, 9*6=54, 5*5=25, 3*4=12, 5*3=15, 0*2=0
soma=297 // 11 - (297 % 11) = 11 // se 11 > 9, 1o dig=0
----
1*11=11, 6*10=60, 8*9=72, 9*8=72, 9*7=63, 5*6=30, 3*5=15, 5*4=20, 0*3=0, 0*2=0
soma=343 // 11 - (343 % 11) = 9 // se 9 > 9, 2o dig=9"""

cpfStr = input('cpf: ')

if not cpfStr.isnumeric() or cpfStr.__len__() != 11:
    print("cpf invalido")
    quit()

cpflist = ''  # MAIS FÁCIL "cpflist = cpf[:9]" ou cpf[:-2]
for i in range(9):
    cpflist += "".join(cpfStr[i])

count = 11
acum = 0
for i in range(9):
    count -= 1
    acum += count * int(cpflist[i])

if 11 - acum % 11 > 9:
    d1 = 0
else:
    d1 = 11 - acum % 11

cpflist1 = cpflist + str(d1)

count = 12
acum = 0
for i in range(10):
    count -= 1
    acum += count * int(cpflist1[i])

d2 = 11 - acum % 11 if 11 - acum % 11 <= 9 else 0

cpflist2 = cpflist1 + str(d2)

print('########')

if cpfStr == cpflist2:
    print('ok')
else:
    print(f'{cpfStr} seria {cpflist}-{d1}{d2}')
