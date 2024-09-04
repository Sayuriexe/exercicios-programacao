import json

with open('c:/Users/willy/Desktop/programacao_e_estudos/Repositorio/estagio-programacao/exercicios-estagio-programacao/exercicio3/dados.json') as file:
    faturamento = json.load(file)
menor_faturamento = float('inf')
maior_faturamento = float('-inf')
soma_faturamento = 0
dias_com_faturamento = 0
for dia in faturamento:
    valor = dia['valor']
    if valor > 0:
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor
        soma_faturamento += valor
        dias_com_faturamento += 1
media_faturamento = soma_faturamento / dias_com_faturamento

dias_acima_da_media = sum(1 for dia in faturamento if dia['valor'] > media_faturamento)
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_da_media} dias")

