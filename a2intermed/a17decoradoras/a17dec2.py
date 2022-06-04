def master(funcao):
    def slave(*arfs, **kwargs):
        print('Decorada')
        funcao(*arfs, **kwargs)
    return slave

@master
def oi(msg):
    print(msg)

#oi = master(oi)
oi('oi')
