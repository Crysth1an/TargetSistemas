faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}


def applicacao():
    total = core(faturamento)
    dados = calculo_percentual(total)
    output(dados)


def core(dados):
    total = 0
    for valor in dados.values():
        total += valor
    return total


def calculo_percentual(total):
    percentuais = {}
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        percentuais[estado] = percentual
    return percentuais


def output(dados):
    for estado, percentual in dados.items():
        print(f"{estado}: {percentual:.2f}%")


if __name__ == '__main__':
    applicacao()
