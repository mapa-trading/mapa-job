class Acao:
    def __init__(self, nome, sigla, moeda, descricao, razaoSocial, website):
        self.nome = nome
        self.sigla = sigla
        self.moeda = moeda
        self.descricao = descricao
        self.razapSocail = razaoSocial
        self.website = website

    def toJson(self):
        return {
            "nome": self.nome,
            "sigla": self.sigla,
            "moeda": self.moeda,
            "descricao": self.descricao,
            "razaoSocial": self.razapSocail,
            "website": self.website
        }
