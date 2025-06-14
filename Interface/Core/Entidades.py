class Dashboard:
    def __init__(self, itens: list):
        self.conteudo = itens

    '''
    o argumento itens precisa ser assim:

    [
     {
     'nome': 'ampola', 
     'quantidade': 5, 
     'gaveta': 'gaveta_2'
     },

     {'nome': 'seringa', 
     'quantidade': 3, 
     'gaveta': 'gaveta_2'
     },
    ]
    '''

    def filtrar_por_gaveta(self, nome_da_gaveta):
        lista_filtrada = []

        for item in self.conteudo:
            if item['gaveta'] == nome_da_gaveta:
                lista_filtrada.append(item)

        return lista_filtrada


    def __repr__(self):
        return f'Dashboard com {len(self.conteudo)} itens.'

