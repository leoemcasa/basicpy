import json

with open('a15abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(f'  {k1}, {v1}')
        