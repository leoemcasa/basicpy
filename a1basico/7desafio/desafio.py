"""
criar var nome (str), idade (int), altura e peso (float), ano atual (int);
obter anoNascimento, IMC (2 casas decimais) e exibir com F-String
"""
nome = 'Leo'
idade = 49
alt = 1.7
peso = 97.0
ano_atual = 2022
ano_nasc = ano_atual - idade
ano_nasc2 = ano_atual - idade - 1
imc = peso / alt ** 2

print(f'{nome} tem {idade} anos e mede {alt}. Pesa {peso} e tem IMC de {imc:.2f}')
print(f'Considerando que estamos em {ano_atual}, deve ter nascido em {ano_nasc2} ou {ano_nasc}')
