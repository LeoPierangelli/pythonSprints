from roboflow import Roboflow
from Adapters.pyt import api_key

def requisitar_predicao(imagem_path: str):
    rf = Roboflow(api_key=api_key)
    project = rf.workspace().project("my-first-project-kl4s4")
    model = project.version(4).model
    
    resultado = model.predict(imagem_path, confidence=40, overlap=30).json()
    return resultado

