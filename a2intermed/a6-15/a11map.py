from a11mapDados import produtos, pessoas, lista

print(lista)
newLista = map(lambda x: x * 2, lista)
print(list(newLista))
newList = [x * 2 for x in lista]
print(list(newList))

for produto in produtos:
    print(produto)

precos = map(lambda p: p['preco'], produtos)
for preco in precos:
    print(preco)

def sobePreco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

newProd = map(sobePreco, produtos)
for produto in newProd:
    print(produto)

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)
