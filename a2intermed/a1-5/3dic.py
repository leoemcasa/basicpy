d1 = {'chave1':'valor1','c2':'v2'}
d1['c3'] = 'v3'

print(d1)
d1['c3'] = 'v.3'
print(d1)
d1.update({'c4':'v4'})
print(d1)
del d1['c4']
d1['chave1'] = ''
print(d1)
print(d1['c2'])
if d1.get('c3'):
    print(d1['c3'])

d2 = dict(c1='v1', c2='v2')
print(d2)
