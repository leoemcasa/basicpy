def master(funcao):
    def slave():
        print('Decorada')
        funcao()
    return slave

@master
def oi():
    print('oi')

#oi = master(oi)
oi()
