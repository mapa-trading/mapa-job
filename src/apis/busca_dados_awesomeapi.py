import json
from datetime import datetime

import requests

from src.model.Cotacao import Cotacao

BASE_API = "https://economia.awesomeapi.com.br"


def get_cotacao_crypto_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/{sigla}")
    print(request.url)
    result = json.loads(request.content)[0]
    dataHora = str(datetime.fromtimestamp(int(result["timestamp"])).strftime("%Y-%m-%dT%H:%M"))

    return Cotacao(sigla, dataHora, result["bid"])


def get_cotacao_moeda_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/{sigla}")
    print(request.url)
    result = json.loads(request.content)[0]
    dataHora = str(datetime.fromtimestamp(int(result["timestamp"])).strftime("%Y-%m-%dT%H:%M"))

    return Cotacao(sigla, dataHora, result["bid"])

