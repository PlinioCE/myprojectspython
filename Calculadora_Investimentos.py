from time import sleep

titulo = ' INVESIMENTOS '
print(f'{titulo:=^40}\n')
while True:
    # taxa = 0.000381624132190338
    taxa = 0.011448723965709
    investimento = float(input('Informe o valor do investimento: R$ '))
    tempo_investimento = int(input('Informe o tempo(em meses) de investimento: '))
    print()
    contador_meses = 1
    valor_investimento = investimento
    while contador_meses < tempo_investimento + 1:
        calculo_investimento = valor_investimento + (valor_investimento * taxa)
        valor_investimento = calculo_investimento
        # print(f'{contador_meses}º mês: R$ {calculo_investimento:.2f}')
        # sleep(1)
        contador_meses += 1
    print(f'\nVocê obterá um lucro líquido de R$ {(calculo_investimento - investimento):.2f} em {tempo_investimento} meses.')
    saida = ' '
    while saida not in 'SN':
        saida = str(input('\nDeseja realizar um novo cálculo? [S/N] ')).strip().upper()[0]
    if saida == 'N':
        break
    print()
