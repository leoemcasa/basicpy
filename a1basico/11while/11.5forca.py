palavra = input('palavra: ')
tpalavra = []
for i in palavra:
    tpalavra.append("_")
ttpal = ''.join(tpalavra)
chances = 3
acerto = ''
for i in range (10):
    print(ttpal)

while chances >= 1:
    acerto = 0
    guess = input('letra: ')
    for i, le in enumerate(palavra):
        if le == guess:
            tpalavra[i] = guess.upper()
            acerto = 1
    if acerto == 0:
        chances -= 1
        print('errou')
    ttpal = ''.join(tpalavra)
    print(ttpal)
    if palavra == ttpal.lower():
        print(f'acerto miseravi')
        quit()
    print(f'vc tem {chances} chances')

