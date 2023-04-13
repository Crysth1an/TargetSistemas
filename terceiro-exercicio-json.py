# TODO: • O menor valor de faturamento ocorrido em um dia do mês;
# TODO: • O maior valor de faturamento ocorrido em um dia do mês;
# TODO: • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

maior, menor, media_dias = 0, 9999, 0

faturamento_mensal = []


def applicacao():
    dados_carregado = leitura_arq_json_segunda_dia_um()
    media = calculo_media(dados_carregado)
    core(dados_carregado, media, maior, menor, media_dias)


def leitura_arq_json_segunda_dia_um():
    # Carrega os dados de faturamento mensal a partir de um arquivo JSON
    with open('dados.json', 'r') as arquivo:
        # dados é uma lista
        dados = json.load(arquivo)
        return dados


def calculo_media(dados):
    valor_somado, quantidade_dias = 0, 0
    for linha in dados:
        if linha['valor'] != 0:
            quantidade_dias += 1
            valor_somado += linha['valor']
    media_valores = valor_somado / quantidade_dias
    return media_valores


def core(dados, media, maior_valor, menor_valor, quantidade_media_dias):
    for linha in dados:
        if linha['valor'] > maior_valor:
            maior_valor = linha['valor']
        elif linha['valor'] < menor_valor and linha['valor'] != 0:
            menor_valor = linha['valor']

        if linha['valor'] > media:
            quantidade_media_dias += 1

    output(maior_valor, menor_valor, quantidade_media_dias, media)


def output(maior_valor, menor_valor, quantidade_media_dias, media_faturameto):
    print(f'Menor faturamento diário: R${maior_valor:.2f}')
    print(f'Maior faturamento diário: R${menor_valor:.2f}')
    print(f'Media de faturamento Mensal: R${media_faturameto:.2f}')
    print(f'Dias com faturamento acima da média: {quantidade_media_dias}')


if __name__ == '__main__':
    applicacao()
