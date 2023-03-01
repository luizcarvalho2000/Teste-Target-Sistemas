

import json

# Função para calcular o menor e o maior valor de um vetor de faturamentos
def min_max_faturamento(faturamento):
    menor_faturamento = faturamento[0]
    maior_faturamento = faturamento[0]
    for valor in faturamento:
        if valor < menor_faturamento:
            menor_faturamento = valor
        elif valor > maior_faturamento:
            maior_faturamento = valor
    return menor_faturamento, maior_faturamento

# Lê os dados de faturamento do arquivo JSON
with open('faturamento.json', 'r') as arquivo:
    faturamento = json.load(arquivo)

# Remove os dias sem faturamento do cálculo da média mensal
valores_faturamento = [valor for valor in faturamento if valor is not None]

# Calcula a média mensal de faturamento
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Calcula o menor e o maior valor de faturamento
menor_faturamento, maior_faturamento = min_max_faturamento(valores_faturamento)

# Calcula o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

# Imprime os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
