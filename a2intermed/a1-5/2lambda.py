def func(arg, arg2):
    return arg * arg2

var = func(2, 2)
print(var)

var2 = lambda x, y: x * y
print(var2(2,2))

lista = [
    ['p1', 13],
    ['p2', 3],
    ['p3', 18],
    ['p4', 23]
]

def f(item):
    return item[1]

lista.sort(key=f, reverse=True)
print(lista)

lista.sort(key=lambda item: item[1])
print(lista)
print(sorted(lista, key=lambda i: i[0], reverse=True))
