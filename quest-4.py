# Questão 4
faturamentoPorEstado = [
    {
        "estado" : 'sp',
        "valor": 67836.43
     },
    {
        "estado" : 'rj',
        "valor" : 36678.66},
    {
        "estado": 'mg',
        "valor" : 29229.88
    },
    {
        "estado" : 'es',
        "valor" : 27165.48
    },
    {
        "estado" : 'outros',
        "valor" : 19849.53}
]

faturamentoTotal = sum(faturamento['valor'] for faturamento in faturamentoPorEstado)
print(faturamentoTotal)

for faturamento in faturamentoPorEstado:
    print(f'O percentual faturado pelo estado do {faturamento['estado']} equivale a {(faturamento['valor'] / faturamentoTotal) * 100:.2f}%.')
