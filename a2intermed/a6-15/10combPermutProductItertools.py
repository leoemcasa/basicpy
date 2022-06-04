from itertools import combinations, permutations, product

pessoas = ['leo', 'ze', 'luiz', 'jo', 'bob']
#arranj = (input('(C)omb, (P)erm ou P(r)oduct:' )).lower()
# ap = []
# for grupo in permutations(pessoas, 2):
#     ap.append(grupo)
#     print(grupo)
# print(len(ap))

for grupo in product(pessoas, repeat=2):
    print(grupo)
    