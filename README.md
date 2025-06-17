
### 🏥 StoCam — Sistema de Estoque com Visão Computacional
Somos a StoCam, uma solução tecnológica para gestão inteligente de estoques hospitalares, baseada em visão computacional e inteligência artificial. Nossa proposta é automatizar a contagem de itens em gavetas hospitalares, reduzindo falhas humanas, desperdícios e ineficiências logísticas que impactam diretamente o atendimento na saúde.

Este repositório contém a API que realiza a leitura de imagens de estoque, processa as informações via modelo de IA (Roboflow) e retorna um dashboard com o inventário detectado, de forma automática, simples e eficiente.

## 🚀 Funcionalidades

    🔍 Predição automática de estoque a partir de uma imagem enviada.

    📄 Retorno de um dashboard estruturado em JSON com:

        Nome do item.

        Quantidade detectada.

        Identificação da gaveta (extraída automaticamente do nome da imagem).

    🌐 Interface via API (HTTP) para integração com outros sistemas (ex.: ERP hospitalar, sistemas de gestão).

    ♻️ Estrutura escalável, baseada em princípios de Clean Architecture, facilitando manutenção e evolução do sistema.

## 🔗 Fluxo de Funcionamento

    🖼️ O usuário faz uma requisição POST para /dashboard enviando uma imagem da gaveta.

    🔗 A API faz uma chamada para a API do Roboflow, enviando a imagem.

    🧠 O Roboflow retorna um JSON com os objetos detectados.

    🔧 O Adapter processa esse JSON, contabiliza os itens e extrai automaticamente o nome da gaveta a partir do nome do arquivo da imagem.

    📊 O sistema cria um Dashboard com as informações tratadas.

    🔥 O dashboard é retornado no formato JSON, pronto para ser consumido por qualquer sistema externo.

## 🎯 Exemplo de Requisição

🔸 Endpoint

  POST /dashboard

🔸 Body (form-data)

  Key: imagem
  Type: File

🔸 Resposta

  [
    {
      "nome": "ampola",
      "quantidade": 5,
      "gaveta": "gaveta_2"
    },
    {
      "nome": "seringa",
      "quantidade": 3,
      "gaveta": "gaveta_2"
    }
  ]

## 📸 Como o sistema entende a gaveta?

    O sistema extrai o nome da gaveta diretamente do nome do arquivo da imagem enviada.
    Exemplo: Se o arquivo se chama gaveta_2.jpg, o sistema entende que os itens pertencem à gaveta_2.

## ✅ Tecnologias Utilizadas

    Python 3
    Flask (API)
    Roboflow API (Visão Computacional)
    Clean Architecture (Organização do código)
    JSON (Formato de entrada e saída)

## 🏁 Como rodar o projeto localmente

  🔧 Instalar dependências

  - pip install -r requirements.txt

  Execute o app.py

  A API estará disponível em:

  http://127.0.0.1:5000

## 👥 Equipe

    Cilas Pinto Macedo — RM560745
    Ian Junji Maluvayshi Matsushita — RM560588
    Pedro Arão Baquini — RM559580
    Leandro Kamada Pesce Dimov — RM560381
    Leonardo de Souza Pierangelli — RM560501

## Video do funcionamento do projeto
    https://youtu.be/OJZuR2Y40t8
