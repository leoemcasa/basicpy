# https://docs.python.org/3/library/functions.html#open

file = open('a15abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  # pra ler o arquivo sendo editado sem precisar fechar e abrir novamente
print(file.read())
print('#########')

file.seek(0, 0)
print(file.readline(), end = '')
print(file.readline(), end = '')
print(file.readline(), end = '')
print('#########')

file.seek(0, 0)
for linha in file.readlines():
    print(linha)

file.close()

try:
    file = open('a15abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()
