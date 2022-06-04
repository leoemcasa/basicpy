"""
variáveis: iniciam com minúsculas, separa-se com "_"
"""
nome = 'Leo'
idade = 49
altura = 1.7
peso = 97
e_maior = idade > 18
imc = peso/altura**2

print(nome, 'tem', idade, 'anos e seu IMC é', imc)
print('Normal: 18,5 a 25 ## Acima: 25 a 30 ## Obeso1 30 a 35')
print(f'{nome} tem {idade} anos e {imc:.2f} de IMC')
print('{} tem {} anos e {:.2f} de IMC'.format(nome, idade, imc))
print('{2} tem {0} anos e {1} de IMC'.format(idade, imc, nome))
print('{n} tem {id} anos e {i} de IMC'.format(n=nome, id=idade, i=imc))
