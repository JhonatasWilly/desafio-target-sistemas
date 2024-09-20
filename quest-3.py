# Questão 3
import json 

with open('dados.json', 'r') as file:
    dados = json.load(file)

# Extração de dias que tiveram o faturamento igual a zero
dados_tratados = list(filter(lambda dado: dado['valor'] != 0.0, dados))

dia_com_menor_faturamento = min(dados_tratados, key=lambda dado: dado['valor'])
dia_com_maior_faturamento = max(dados_tratados, key=lambda dado: dado['valor'])

# Função para calcular a media das vendas. 
def media_das_vendas():
    totalVendas = 0
    for dado in dados_tratados:
        totalVendas +=  dado['valor']
    return(totalVendas / len(dados_tratados))
mediaMensal = media_das_vendas()

cont = 0 
for dado in dados_tratados:
    if dado['valor'] > mediaMensal:
        cont += 1

print(f'Menor faturamento: {dia_com_menor_faturamento}')
print(f'Maior faturamento: {dia_com_maior_faturamento}')
print(f'Quantidade de dias que tiveram o faturamento superior a media do faturamento mensal: {cont}')