import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')


# for pergunta in html.select('.question-summary'):
#     titulo = pergunta.select_one('.question-hyperlink')
#     data = pergunta.select_one('.relativetime')
#     votos = pergunta.select_one('.vote-count-post')
#     print(data.text, titulo.text, votos.text, sep='\t')

for pergunta in html.select('.s-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    print(f'{data.text}, {votos.text} votos')#, {resp.text}')
    print(titulo.text)
    print()
"""
for pergunta in html.select('.s-post-summary--stats-item.has-answers'):
    for r in html.select('.s-post-summary--stats-item-number'):
    #resp = pergunta.select('title')
        print(r.text)
    # for show in pergunta.select_one('.s-post-summary--stats-item'):
    #     print(show)
    #     print( '######')
"""