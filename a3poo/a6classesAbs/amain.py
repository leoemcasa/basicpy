from cp import Cp
from cc import Cc

cp = Cp(1, 1, 0)
cp.depositar(10)

print('###############')

cc = Cc(1, 2, saldo=0, limite=200)
cc.depositar(100)
cc.sacar(200)
