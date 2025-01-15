import json

def calcular_estatisticas(faturamento):

    #filtrar valores maiores que zero
    valores_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    #calcular menor, maior e media
    menor_valor = min(valores_validos)
    maior_valor = max(valores_validos)
    media_mensal = sum(valores_validos) / len(valores_validos)

    #contar dias acima da media
    dias_acima_da_media = sum(1 for dia in valores_validos if dia > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media

def main():

    with open('dados.json', 'r') as arquivo:
        faturamento_mensal = json.load(arquivo)

    menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas(faturamento_mensal)

    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

if __name__ == "__main__":
    main()