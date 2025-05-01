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

data_base = {
    'itens': [],
    'quantidade': []
}

for chave in contagem:
    data_base['itens'].append(chave)
    data_base['quantidade'].append(contagem[chave])

print(data_base)

