palavra = input('palavra: ')
tpalavra = []
chances = 3
acerto = ''

while chances >= 1:
    acerto = 0
    guess = input('letra: ')
    for le in palavra:
        if guess in palavra:
            tpalavra += guess.upper()
            # acerto = 1
            break
        else:
            break
    print(tpalavra)

    # if acerto == 0:
    #     chances -= 1
    #     print('errou')
    # ttpal = ''.join(tpalavra)
    # print(ttpal)
    # if palavra == ttpal.lower():
    #     print(f'acerto miseravi')
    #     quit()
    # print(f'vc tem {chances} chances')

