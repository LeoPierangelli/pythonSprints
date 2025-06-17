from flask import Flask, request, jsonify
from Core.Dashboard_UseCase import criar_dashboard
from Adapters.Roboflow_Adapter import adapter_roboflow
from Adapters.Roboflow_Client import requisitar_predicao
import os

app = Flask(__name__)

@app.route('/dashboard', methods=['POST'])
def dashboard():
    # Verifica se o content-type é application/json
    if not request.is_json:
        return jsonify({"error": "Content-Type deve ser application/json"}), 415 
    
    #pega a imagem da requisição
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "JSON inválido ou 'url' não enviado"}), 400

    image_url = data['image_url']
    #request na api do roboflow. Devolve um json feio
    resultado_roboflow = requisitar_predicao(image_url)
    #passa o json feio pro adapter tratar. Devolve numa lista de dicionarios
    lista_itens = adapter_roboflow(resultado_roboflow)
    #cria o dashboard
    dashboard_obj = criar_dashboard(lista_itens)
    #retorna o dashboard como json
    return jsonify(dashboard_obj.conteudo)

if __name__ == '__main__':
    app.run(debug=True)
