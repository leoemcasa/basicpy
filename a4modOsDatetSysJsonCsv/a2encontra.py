import os

path = input('caminho: ')
key = input('termo: ')

def format_size(filesize):
    base = 1024
    k = base
    m = base ** 2
    g = base ** 3
    t = base ** 4
    p = base ** 5

    if filesize < k:
        texto = 'B'
    elif filesize < m:
        filesize /= k
        texto = 'K'
    elif filesize < g:
        filesize /= m
        texto = 'M'
    elif filesize < t:
        filesize /= g
        texto = 'G'
    elif filesize < p:
        filesize /= t
        texto = 'T'
    else:
        filesize /= p
        texto = 'P'

    filesize = round(filesize, 2)
    return f'{filesize}{texto}'

conta = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if key in file:
            try:
                conta += 1
                filepath = os.path.join(root, file)
                filename, fileext = os.path.splitext(file)
                filesize = os.path.getsize(filepath)
                print()
                print(f'Arquivo encontrado: {file}')
                print(f'Caminho completo: {filepath}')
                print(f'Nome do arquivo: {filename}{fileext}')
                print(f'Tamanho do arquivo: {filesize}')
                print(f'Tamanho do arquivo: {format_size(filesize)}')
            except PermissionError as e:
                print('Sem permissão!')
            except FileNotFoundError as e:
                print('Arquivo não encontrado!')
            except Exception as e:
                print('Erro desconhecido!', e)

print()
print(f'{conta} arquivo(s) encontrado(s).')
