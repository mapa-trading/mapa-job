from src.apis.busca_dados_brapi import get_crypto_by_sigla, get_moeda_by_sigla
from src.apis.busca_dados_awesomeapi import get_cotacao_crypto_by_sigla, get_cotacao_moeda_by_sigla
from src.apis.busca_dados_hgbrasil import get_acao_by_sigla
from src.apis.inseri_dados_mapa_cotacoes import inseri_dados_crypto, inseri_dados_moeda, inseri_dados_acoes, \
    inseri_dados_cotacoes

CRYPTOS = ["BTC", "ETH", "LTC", "DOGE"]
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
        cotacao = get_cotacao_crypto_by_sigla(crypto)
        inseri_dados_cotacoes(cotacao.toJson())

    for moeda in MOEDAS:
        cotacao = get_cotacao_moeda_by_sigla(moeda)
        inseri_dados_cotacoes(cotacao.toJson())

    for acao in ACOES:
        # TODO()
        pass