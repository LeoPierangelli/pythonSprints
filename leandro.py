from ultralytics import YOLO
import cv2
import json
from collections import Counter

# Carrega o modelo
model = YOLO("yolo11n.pt")  # substitua pelo seu modelo correto

# Caminho da imagem
img_path = "C:/Users/Leandro/Pictures/meds.webp"

# Roda a predição
results = model(img_path)

# Extrai as classes detectadas
names = model.names  # dicionário com id: nome da classe
classes_detectadas = results[0].boxes.cls.tolist()  # lista de índices das classes
nomes_detectados = [names[int(i)] for i in classes_detectadas]

# Conta quantos de cada classe foram detectados
contagem = dict(Counter(nomes_detectados))

# Converte para JSON formatado
json_saida = json.dumps(contagem, indent=2, ensure_ascii=False)
print(json_saida)

results[0].show()



