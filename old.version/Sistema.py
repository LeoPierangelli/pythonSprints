import json

##Estoque Visao_Computacional
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
    'nome': [],
    'quantidade': []
}

for chave in contagem:
    estoque['nome'].append(chave)
    estoque['quantidade'].append(contagem[chave])
 

##Estoque-Manual 
def forca_opcao(msg, lista):
    opcoes = '\n'.join(lista)
    escolha = input(f'{msg} \n{opcoes} \n-> ')
    while escolha not in lista:
        print('Opção invalida, por favor tente novamente.')
        escolha = input(f'{msg} \n{opcoes} \n-> ')
    return escolha


def forca_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        print('Número invalido, tente novamente.')
        num = input(msg)
    num = int(num)
    return num


def adicionar():
    visualizar()
    item_novo = input('Novo item: ')
    estoque['nome'].append(item_novo)
    quantidade = forca_numero('Quantidade: ')
    estoque['quantidade'].append(quantidade)
    visualizar()
    return


def atualizar():
    visualizar()
    escolha = forca_opcao('Qual item deseja atualizar?', estoque['nome'])
    indices = atualiza_indices()
    indice = indices[escolha]
    atributo = forca_opcao(f'Qual atributo do(a) {escolha} deseja mudar?', estoque.keys())
    if atributo == 'nome':
        novo_nome = input('Novo nome: ')
        estoque[atributo][indice] = novo_nome
        print(f'nome atualizado para: {novo_nome}')
    if atributo == 'quantidade':
        estoque[atributo][indice] = forca_numero(f'Nova quantidade: ')
    visualizar()
    return


def atualiza_indices():
    indices = {estoque['nome'][i]: i for i in range(len(estoque['nome']))}
    return indices

def remover():
    visualizar()
    nome_remover = forca_opcao("Qual item você deseja remover?", estoque['nome'])
    indices = atualiza_indices()
    indice_remover = indices[nome_remover]
    for key in estoque.keys():
        estoque[key].pop(indice_remover)
    print('O estoque está sendo atualizado...')
    visualizar()

def visualizar():
    print("\n=== Estoque Atual ===")
    print(f"{'nome':<15} {'Quantidade':<10}")
    print("-" * 37)
    for i in range(len(estoque['nome'])):
        nome = estoque['nome'][i]
        quantidade = estoque['quantidade'][i]
        print(f"{nome:<15} {quantidade:<10}")
    print("-" * 37)

menu = {
    'adicionar':adicionar,
    'remover':remover,
    'atualizar':atualizar,
    'visualizar':visualizar,
    'sair': 'sair'
}

print('Bem vindo à Stocam!')

while True:
    escolha = forca_opcao('Qual operação deseja realizar?', menu.keys())
    if escolha == 'sair':
        print('Saindo do sistema...')
        break
    else:
        menu[escolha]()