class Cotacao:
    def __init__(self, sigla, dataHora, valor):
        self.sigla = sigla
        self.dataHora = dataHora
        self.valor = valor


    def toJson(self):
        return {
            "sigla": self.sigla,
            "dataHora": self.dataHora,
            "valor": self.valor
        }
