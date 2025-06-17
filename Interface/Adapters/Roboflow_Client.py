from inference_sdk import InferenceHTTPClient
from Adapters.pyt import api_key

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=api_key
)

def requisitar_predicao(imagem_url: str):
    resultado = CLIENT.infer(
        imagem_url,
        model_id="my-first-project-kl4s4/4"
    )
    return resultado
