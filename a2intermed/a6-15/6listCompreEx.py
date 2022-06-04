str1 = '01234567890123456789012345678901234567890123456789'
# lista = ['0123456789', '0123456789', '0123456789']
# retorno = '0123456789.0123456789.0123456789'


def f10(param):
    n = 10
    chunks = [str1[i:i + n] for i in range(0, len(str1), n)]
    return chunks
    # for i in param:


v = f10(str1)
print(v)
strf = '.'.join(v)
print(strf)
# solução
str2 = '01234567890123456789012345678901234567890123456789'
n2 = 10
lista = [str2[1:1+n2] for i in range(0, len(str2),n2)]
retorno = '.'.join(lista)
print(lista)
print(retorno)
