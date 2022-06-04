lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]

for indice, nome in lista:
    print(indice, nome, lista[indice][1])

print('######################')

lista2 = ['luiz', "João", 'Maria']

for i, n in enumerate(lista2):
    print(i, n, lista2[i])
