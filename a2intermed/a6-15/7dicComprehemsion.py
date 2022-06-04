lista = [
    ('chave', 2),
    ('chave2', 'valor2')
]

d1 = {x.capitalize(): y*2 for x, y in lista}
d2 = dict(lista)
print(d1, d2)

d3 = {f'chave_{x}': x**2 for x in range(4)}
print(d3)
