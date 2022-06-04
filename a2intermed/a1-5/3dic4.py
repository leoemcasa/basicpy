import copy, random

d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1  # em py é a única que associa, não cria uma nova
v[1] = 'x'
print(d1)

v = copy.deepcopy(d1)
v[1] = 'a'
print(d1)
print(v)
print(random.randrange(9))

