import pprint
import requests


def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    dados_cep = response.json()
    print(dados_cep)
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get(
        'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    # retorna_dados_cep('22041001')
    # dados = retorna_dados_pokemon('pikachu')
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dados['sprites']['front_shiny'])
    response = retorna_response('https://globallabs.academy/')
    print(response)
