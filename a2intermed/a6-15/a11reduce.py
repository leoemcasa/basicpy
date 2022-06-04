from a11mapDados import produtos, pessoas, lista
from functools import reduce

acumula = 0  # review
for i in lista:
    acumula += i
print(acumula)

sumList = reduce(lambda ac, i: i + ac, lista, 0)
print(sumList)
