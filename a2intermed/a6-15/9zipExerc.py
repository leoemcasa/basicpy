from itertools import count
cont = count(start=10, step=5)

la = [1, 2, 3, 4, 5, 6, 7]
lb = [1, 2, 3, 5]
lc = [(x+y) for x, y in list(zip(la, lb))]

print(la)
print(lb)
print(lc)

listSoma = []
for i in range(len(lb)):
    listSoma.append(la[i] + lb[i])
print(listSoma)

listSoma = []
for en, i in enumerate(lb):
    listSoma.append(la[en] + lb[en])
print(listSoma)
