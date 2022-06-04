carrinho = []
carrinho.append(('prod1', 30))
carrinho.append(('prod2', 20))
carrinho.append(('prod3', 50))

total = 0
for prod in carrinho:
    total += prod[1]
print(total)

total = []
for prod in carrinho:
    total.append(prod[1])
print(total, sum(total))

total = sum([x[1] for x in carrinho])
print(total)
