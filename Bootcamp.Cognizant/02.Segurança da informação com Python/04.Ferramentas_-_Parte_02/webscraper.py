import requests
from bs4 import BeautifulSoup

# objeto site recebendo o conteudo da requisicao http do site...
site = requests.get('https://www.climatempo.com.br/').content

# objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

# transforma html em string e o print vai exibir o html
# print(soup.prettify())

result = soup.find("p", class_="-gray _flex _align-center")
temperatura = []

for item in result:
    temperatura.append(item.text)

temperatura = ' '.join(temperatura).split()
temp_minima = min(temperatura)
temp_maxima = max(temperatura)
print(f'{soup.title.string}')
print(f'{soup.p.string}')
print(f'Temperatura mínima: {temp_minima}')
print(f'Temperatura máxima: {temp_maxima}')
