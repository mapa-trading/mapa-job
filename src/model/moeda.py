class Moeda:
    def __init__(self, nome, sigla, moeda, origem):
        self.nome = nome
        self.sigla = sigla
        self.moeda = moeda
        self.origem = origem

    def toJson(self):
        return {
            "nome": self.nome,
            "sigla": self.sigla,
            "moeda": self.moeda,
            "origem": self.origem
        }
