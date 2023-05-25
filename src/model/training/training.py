# Importando as bibliotecas necessárias
from roboflow import Roboflow
import os
from dotenv import load_dotenv
from ultralytics import YOLO

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()
api_key = os.environ.get('API_KEY')

# Inicializando a instância do Roboflow e configurando o projeto e dataset
rf = Roboflow(api_key=api_key)
project = rf.workspace("university-bswxt").project("crack-bphdr")
dataset = project.version(2).download("yolov8")

# Carregando o modelo YOLOv8
model = YOLO('../crack-2/yolov8n.pt')

# Treinando o modelo com o dataset
model.train(dataset, epochs=10, batch_size=8)

# Alternativamente, podemos executar o seguinte comando no terminal
# !yolo train data=/content/crack-2/data.yaml model=yolov8n.pt epochs=10 lr0=0.01
