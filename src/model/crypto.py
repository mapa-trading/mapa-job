class Crypto:
    def __init__(self, nome, sigla, moeda, imagem_url):
        self.nome = nome
        self.sigla = sigla
        self.moeda = moeda
        self.imagem_url = imagem_url

    def toJson(self):
        return {
            "nome": self.nome,
            "sigla": self.sigla,
            "moeda": self.moeda,
            "imagemUrl": self.imagem_url
        }
