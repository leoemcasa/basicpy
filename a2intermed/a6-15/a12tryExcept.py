#a = 0 ## raise exception
try:
    print(a)
except:
    print('erro')


try:
    a = [] / 0
    print(a[1])
except NameError as erro:
    print('erro:', erro)
except (IndexError, KeyError) as erro:
    print('erro de indice ou chave')
except Exception as erro:
    print('erro inesperado')
else:
    print('sucesso')
finally:
    a = '"a" esta ok?'
    print(f'concluido {a}')  # exceuta independente so houve except
print('segue o jogo')