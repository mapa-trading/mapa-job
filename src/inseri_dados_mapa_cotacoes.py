import requests


# http://localhost:8080/acoes


def inseri_dados_acoes(json):
    request = requests.post('http://localhost:8080/acoes', json=json)
    print(request.url, request.status_code)


def inseri_dados_crypto(json):
    request = requests.post('http://localhost:8080/cryptos', json=json)
    print(request.url, request.status_code)


def inseri_dados_moeda(json):
    request = requests.post('http://localhost:8080/moedas', json=json)
    print(request.url, request.status_code)
