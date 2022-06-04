# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print(cars)

frase = 'q w e q w q w w'  # input('frase: ')
tfrase = frase.split(" ")
# print(f'{tfrase}')
maior = 0
letra = ''

for valor in tfrase:
    qtd = tfrase.count(valor)
    if qtd > maior:
        maior = qtd
        letra = valor
print(maior, letra)

print(valor, tfrase, qtd)
# print(f'{tfrase.sort()}')
