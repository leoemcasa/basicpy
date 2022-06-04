import os
import json

with open('a15abc2.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.seek(0)
    print(file.read())

os.remove('a15abc2.txt')

d1 = {
    'Pessoa1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa2': {
        'nome': 'Rose',
        'idade': 30,
    }
}
d1_json = json.dumps(d1, indent=True)

with open('a15abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)
