from flask import Flask, request, jsonify
from Core.Dashboard_UseCase import criar_dashboard
from Adapters.Roboflow_Adapter import adapter_roboflow
from Adapters.Roboflow_Client import requisitar_predicao
import os

app = Flask(__name__)

@app.route('/dashboard', methods=['POST'])
def dashboard():
    print("request.files keys:", request.files.keys())
    #verificando se key imagem tá no body da requisição
    if 'imagem' not in request.files:
        return jsonify({"error": "Imagem não enviada"}), 400

    #pega a imagem da requisição
    imagem = request.files['imagem']
    #salvando a imagem
    imagem.save(f'{imagem.filename}')
    #request na api do roboflow. Devolve um json feio
    resultado_roboflow = requisitar_predicao(f'{imagem.filename}')
    #passa o json feio pro adapter tratar. Devolve numa lista de dicionarios
    lista_itens = adapter_roboflow(resultado_roboflow)
    #cria o dashboard
    dashboard_obj = criar_dashboard(lista_itens)
    #retorna o dashboard como json
    return jsonify(dashboard_obj.conteudo)

if __name__ == '__main__':
    app.run(debug=True)
