#requisições para sites
import requests

#traduzir a resposta
from bs4 import BeautifulSoup

#URL para acesso
url = 'https://g1.globo.com/'

#fazendo busca da requisição HTTP
resposta = requests.get(url)

#verificar se a requisição deu certo
if resposta.status_code == 200: #200 -> ok

    soup = BeautifulSoup(resposta.text, 'html.parser') #traduzir a resposta

    #print(soup) #escreve html do site

    #encontrar todas as notícias
    noticias = soup.find_all('a', class_='feed-post-link')
    print('Últimas notícias do G1:')
    for i, noticias in enumerate(noticias): #percorre todas as notícias
        print(f'{i+1}. {noticias.text}') #escreve cada notícia