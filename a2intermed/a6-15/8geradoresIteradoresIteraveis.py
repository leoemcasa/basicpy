import sys, time
lista = [0,1,2,3,4,5]
lst2 = 12345
print(hasattr(lista, '__iter__'), hasattr(lst2, '__iter__'))

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))
print(type(l1), type(l2))
print(sys.getsizeof(l1), sys.getsizeof(l2))
