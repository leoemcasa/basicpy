"""
entrada de dados
"""
nome = input("Seu nome: ")
idade = input('Idade: ')
ano_nasc = 2022 - int(idade)

print('------------')
print(f'{nome} tem {idade} anos'
      f' e nasceu em {ano_nasc -1} ou {ano_nasc}')