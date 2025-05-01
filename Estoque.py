import json

with open('resultado_predicao.json', 'r') as f:
    data = json.load(f)

contagem = {}

for item in data['predictions']:
    classe = item['class']
    if classe in contagem:
        contagem[classe] += 1
    else:
        contagem[classe] = 1

estoque = {
    'itens': [],
    'quantidade': []
}

for chave in contagem:
    estoque['itens'].append(chave)
    estoque['quantidade'].append(contagem[chave])

# print(estoque)

