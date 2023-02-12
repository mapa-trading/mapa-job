import os

import requests

MAPA_COTACOES_BASE_API = os.environ.get("MAPA_COTACOES_URL", "http://localhost:8080")


def inseri_dados_acoes(json):
    request = requests.post(f'{MAPA_COTACOES_BASE_API}/acoes', json=json)
    print(request.url, request.status_code)


def inseri_dados_crypto(json):
    request = requests.post(f'{MAPA_COTACOES_BASE_API}/cryptos', json=json)
    print(request.url, request.status_code)


def inseri_dados_moeda(json):
    request = requests.post(f'{MAPA_COTACOES_BASE_API}/moedas', json=json)
    print(request.url, request.status_code)


def inseri_dados_cotacoes(json):
    request = requests.post(f'{MAPA_COTACOES_BASE_API}/cotacoes', json=json)
    print(request.url, request.status_code)
