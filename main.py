from flask import Flask

from atualiza_banco_dados import buscar_e_inserir_dados_iniciais, buscar_e_inserir_cotacoes

app = Flask(__name__)


@app.route("/atualizar-cotacoes", methods=['POST'])
def update():
    buscar_e_inserir_cotacoes()
    return "Cotacoes atualizadas"


@app.route("/", methods=['GET'])
def hello():
    return "Tudo certo por aqui"


@app.route('/dados-iniciais', methods=['POST'])
def init_dados():
    buscar_e_inserir_dados_iniciais()
    return "Beleza adicionou os dados"


if __name__ == '__main__':
    app.run()
