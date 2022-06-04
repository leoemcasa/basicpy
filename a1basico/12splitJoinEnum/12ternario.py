logUsr = False
msg = 'logado' if logUsr else 'não logado'
print(msg)
print(logUsr or 'Não Logado')
logUsr = True
msg = 'logado' if logUsr else 'não logado'
print(msg)
print(logUsr or 'Não Logado')
