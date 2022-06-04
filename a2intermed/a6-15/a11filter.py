from a11mapDados import produtos, pessoas, lista

print(lista)
newList = filter(lambda x: x > 5, lista)
print(list(newList))

newLista = [x for x in lista if x > 5]
print(list(newLista))
""""""
list10plus = filter(lambda p: p['preco'] > 10, produtos)
for produto in list10plus:
    print(produto)
print('#' * 4)
def filtra(produto):
    if produto['preco'] > 50:
        return True

listplus = filter(filtra, produtos)
for produto in listplus:
    print(produto)
