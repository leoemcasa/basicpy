lista = ['eu', 'tu', 'eles', 'nos', 'vos', 'eles', 1 ,3, 7, 97]

v1, v2, *sublista, vfim = lista
print(lista)
print(v1, v2, sublista, vfim)
print(sublista[-1])
# trocando valores de var
v1, v2, sublista[-1], vfim = v2, v1, vfim, sublista[-1]
print(v1, v2, sublista, vfim)
