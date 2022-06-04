from itertools import zip_longest, count
cidades = ['cgh', 'gru', 'gyn', 'bel', 'fln']
estados = ['sp', 'sp', 'go', 'pa', 'sc', 'df']
cidestad = zip(estados, cidades)
print(list(cidestad))
cidest = zip_longest(estados, cidades)
print(list(cidest))
cidest = zip_longest(estados, cidades, fillvalue='??')
print(list(cidest))

indices = count()
cidades = ['cgh', 'gru', 'gyn', 'bel', 'fln']
estados = ['sp', 'sp', 'go', 'pa', 'sc', 'df']
cid_est = zip(
    indices,
    estados,
    cidades
)
for indices, estados, cidades in cid_est:
    print(indices, estados, cidades)
