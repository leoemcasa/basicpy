"""
Tipos de dados (primitivos)
"""
print(type('leo'))  # , end=',## ')  # str- string ## textos 'assim' ou "assim"
print(type(123), end='## ')  # int - inteiro ## 123 ou 0 ou -10
print(type(0.0), end='## ')  # float - real/ ponto flutuante ## 12.3 0.0 -10.0
print(type(True), end='## ')  # bool - boleano/ lógico ## true or false
print(type(10==10), end='## ')  # bool
print(bool(10==10), end='## ')  # bool
print(bool(''), end='## ')  # bool tipo vazios retornam falso
print('10', type('10'), type(int('10')))
print('10', type('10'), float('10'))
print(49, bool(49>18))

