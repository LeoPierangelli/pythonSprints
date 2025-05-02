from roboflow import Roboflow
import json

rf = Roboflow(api_key="mB8Ak44KAuneBt65f5Im")
project = rf.workspace().project("my-first-project-kl4s4")
model = project.version(4).model

# Visualizar sua predição
model.predict("imagem 3.webp", confidence=40, overlap=30).save("predicao1.jpg")

# Dicionário retornado:
resultado = model.predict("imagem 3.webp", confidence=40, overlap=30).json()

# Convertendo para string JSON formatada
resultado_json = json.dumps(resultado, indent=2)

# Salvando em um arquivo
with open("resultado_predicao.json", "w") as f:
    f.write(resultado_json)