import os
from src.busca_dados_brapi import get_crypto_by_sigla, get_acao_by_sigla, get_moeda_by_sigla
from src.inseri_dados_mapa_cotacoes import inseri_dados_crypto, inseri_dados_moeda, inseri_dados_acoes

INSERIR_DADOS_INICIAIS = os.environ.get("INSERIR_DADOS_INICIAIS", "true")

CRYPTOS = ["BTC", "ETH", "LTC", "BNB", "DOGE", "AVAX", "BCH", "USDC", "BUSD"]
ACOES = ["EMBR3", "PETR4", "MGLU3"]
MOEDAS = ["USD", "EUR", "ARS", "BOB", "CNY", "PYG", "VEF"]


def buscar_e_inserir_dados_iniciais():
    for crypto in CRYPTOS:
        ativo = get_crypto_by_sigla(crypto)
        inseri_dados_crypto(ativo.toJson())

    for acao in ACOES:
        ativo = get_acao_by_sigla(acao)
        inseri_dados_acoes(ativo.toJson())

    for moeda in MOEDAS:
        ativo = get_moeda_by_sigla(moeda)
        inseri_dados_moeda(ativo.toJson())


def buscar_e_inserir_cotacoes():
    print("Buscando e armazenando as cotações")
    for crypto in CRYPTOS:
        # TODO()
        pass

    for acao in ACOES:
        # TODO()
        pass


def main():
    if INSERIR_DADOS_INICIAIS == "true":
        buscar_e_inserir_dados_iniciais()

    buscar_e_inserir_cotacoes()


if __name__ == "__main__":
    main()
