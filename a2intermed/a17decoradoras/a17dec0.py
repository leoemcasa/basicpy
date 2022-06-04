def fOi():
    print('Oi')
fOi()

var = fOi
var()

def master():
    def slave():
        print('Oi')
    slave()
master()

def master():
    def slave():
        print('Oi')
    return slave
var = master()
var()
print(type(var))


