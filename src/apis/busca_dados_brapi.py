import json
from datetime import datetime

import requests

from src.model.Cotacao import Cotacao
from src.model.crypto import Crypto
from src.model.moeda import Moeda

BASE_API = "https://brapi.dev/api"


def get_crypto_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/v2/crypto?coin={sigla}")
    print(request.url)
    result = json.loads(request.content)["coins"][0]

    return Crypto(result["coinName"], result["coin"], result["currency"], result["coinImageUrl"])


def get_moeda_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/v2/currency?currency={sigla}-BRL")
    print(request.url, request.status_code)

    result = json.loads(request.content)["currency"][0]

    return Moeda(result["name"], result["fromCurrency"], result["toCurrency"], result["fromCurrency"])


def get_cotacao_acao_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/quote/{sigla}")
    print(request.url)
    result = json.loads(request.content)["results"][0]

    dataHora = result["regularMarketTime"][0:16]

    print(dataHora)

    return Cotacao(sigla, dataHora, result["regularMarketPrice"])

