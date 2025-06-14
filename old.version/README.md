# Sistema de Estoque com Visão Computacional + Entrada Manual

Somos a StoCam, uma solução tecnológica voltada à gestão automatizada de estoques hospitalares, baseada na integração entre visão computacional, inteligência artificial e infraestrutura de monitoramento contínuo. Nosso objetivo é otimizar o controle de insumos hospitalares, reduzindo falhas humanas, desperdícios e ineficiências logísticas que impactam diretamente a qualidade do atendimento à saúde. No código apresentado, desenvolvemos o início da nossa leitura de imagens através de inteligência artificial, unido com conhecimentos em tratamento de dicionários para possibilidade de manutenção manual do estoque do hospital parceiro.


- O estoque é criado no sistema através de uma requisição de leitura de imagem na API do ROBOFLOW
- Recebemos um dicionário com todos os itens identificados na imagem
- Transformamos esse arquivo em um banco de dados contínuo que irá atualizar o sistema de ERP de estoque do Hospital
- Disponibilizamos a opção de modificação do estoque. Caso o funcionário deseje alterar algum conteúdo, pode escolher adicionar ou remover itens presentes no banco de dados.
- Visualiza os itens presentes no estoque.

---

## Integrantes

- Cilas Pinto Macedo - RM560745
- Ian Junji Maluvayshi Matsushita RM560588
- Pedro Arão Baquini - RM559580
- Leandro Kamada Pesce Dimov - RM560381
- Leonardo de Souza Pierangelli - RM560501

---

## Funcionalidades do código

- Leitura de um arquivo `resultado_predicao.json` com as previsões de classes de objetos identificados por um modelo de visão computacional.
- Contabilização automática da quantidade de cada classe detectada.
- Interface em linha de comando para:
  - Adicionar itens manualmente.
  - Atualizar nome ou quantidade de um item.
  - Remover itens.
  - Visualizar o estoque atual em formato tabular.

---

## Como funciona

1. **Leitura do JSON**
   - O sistema lê um arquivo chamado `resultado_predicao.json` contendo a chave `"predictions"`, que deve ser uma lista de objetos com a chave `"class"` representando o tipo do item detectado.

2. **Contabilização Automática**
   - Cada ocorrência de uma classe é contabilizada e armazenada em uma estrutura de dicionário.

3. **Manipulação Manual via Terminal**
   - O usuário pode interagir com o sistema por meio de menus e inputs para gerenciar o estoque.

---

## Exemplo de entrada (`resultado_predicao.json`)
```json
{"predictions": [
    {
      "x": 498,
      "y": 608,
      "width": 84,
      "height": 16,
      "confidence": 0.9970365166664124,
      "class": "ampola",
      "class_id": 0,
      "detection_id": "05a281f9-2e7a-4d76-b449-3ffa1d8b825c",
      "image_path": "gaveta 2.jpg",
      "prediction_type": "ObjectDetectionModel"
    }
  ],
  "image": {
  "width": "1280",
  "height": "720"
  }
}
```
<img src="Diagrama.png">

## Vídeo do projeto funcionando
https://youtu.be/_I0peYpfJTs
