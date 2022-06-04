d1 = {
    'chave1':'valor1',
    'c2':'v2'
}
d1['c3'] = 'v3'

print('c2' in d1)
print('v3' in d1.values())
print(len(d1))

for k, v in d1.items():
    print(k,v)
