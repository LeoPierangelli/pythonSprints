from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ROBOFLOW_API_KEY")

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
