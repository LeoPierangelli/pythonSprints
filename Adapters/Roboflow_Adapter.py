def adapter_roboflow(json_roboflow):
    predictions = json_roboflow.get('predictions')

    contagem = {}

    for item in predictions:
        nome = item['class']

        chave = (nome) #Conta +1 se o nome já tiver aparecido no json da predição

        #Parte necessária para conseguirmos a quantidade
        if chave in contagem:
            contagem[chave] += 1
        else:
            contagem[chave] = 1

    #Saída para o Core
    lista_itens = [
        {
         'nome': nome, 
         'quantidade': quantidade, 
         'gaveta': "gaveta 1"
         }
         
        for (nome), quantidade in contagem.items()
    ]

    return lista_itens
