import json

import requests

from src.model.acao import Acao
from src.model.crypto import Crypto
from src.model.moeda import Moeda

BASE_API = "https://brapi.dev/api"


def get_acao_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/quote/{sigla}")
    print(request.url)
    result = json.loads(request.content)["results"][0]

    return Acao(result["longName"], result["symbol"], result["currency"], "", "", "")


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
