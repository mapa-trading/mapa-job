import json

import requests

from src.model.acao import Acao

BASE_API = "https://fintz.herokuapp.com/api"
API_KEY = "b0375eb6"


def get_acao_by_sigla(sigla):
    request = requests.get(f"{BASE_API}/b3/acoes/{sigla}/indicadores")
    print(request.url)
    result = json.loads(request.content)

    return Acao(result["empresa"], result["ticker"], "BRL", result["setor"],
                result["empresa"] + " LTDA", "http://www." + result["ticker"] + ".com.br")
