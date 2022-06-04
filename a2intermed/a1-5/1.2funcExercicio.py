def saudNom(s='Alo', n='vc'):
    print(s, n)

saudNom('oi', 'tu')

def n3Soma(n1=1, n2=1, n3=1):
    print(n1 + n2 + n3)

n3Soma(1, 2, 3)

def percent(n1=100, n2=0):
    return n1 + n1 * n2 / 100

print(percent(30, 10))
'''
def fb(num):
    if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
    elif num % 3 == 0:
            return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num
MELHOR
'''
def fb(num):
    if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
    if num % 3 == 0:
            return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num

print(fb(15))
