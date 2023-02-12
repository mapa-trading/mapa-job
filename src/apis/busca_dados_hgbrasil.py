import json

import requests

from src.model.acao import Acao

BASE_API = "https://api.hgbrasil.com/finance/stock_price"
API_KEY = "b0375eb6"


def get_acao_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/?key={API_KEY}&symbol={sigla}")
    print(request.url)
    result = json.loads(request.content)["results"][0]

    return Acao(result["longName"], result["symbol"], result["currency"], "", "", "")
