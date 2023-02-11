from flask import Flask
import os
from atualiza_banco_dados import buscar_e_inserir_dados_iniciais, buscar_e_inserir_cotacoes

INSERIR_DADOS_INICIAIS = os.environ.get("INSERIR_DADOS_INICIAIS", "true")

app = Flask(__name__)


@app.route("/")
def update():
    if INSERIR_DADOS_INICIAIS == "true":
        buscar_e_inserir_dados_iniciais()

    buscar_e_inserir_cotacoes()
    return "Cotacoes atualizadas"


if __name__ == '__main__':
    app.run()
