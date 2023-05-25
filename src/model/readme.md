# Modelo de detecção de rachaduras

## Descrição

Este código usa a biblioteca Ultralytics e o modelo YOLO para realizar a detecção de objetos em tempo real a partir de uma webcam. Ele captura frames da webcam, realiza a detecção de objetos no frame atual e desenha retângulos em torno dos objetos detectados, exibindo o resultado em uma janela chamada "Webcam". O loop continua até que a tecla 'q' seja pressionada, momento em que a captura de vídeo é liberada e as janelas são fechadas.

## Treinamento do Modelo - /training/training.py

Na pasta /training deste projeto, você encontrará um arquivo chamado training.py. Este arquivo contém um script responsável por baixar um conjunto de imagens da internet e treinar um modelo YOLOv8 com base nessas imagens. O modelo treinado é o yolo.pt que está na mesma pasta que esse documento.

### Para executar o script de treinamento, siga as instruções abaixo:

Execute o arquivo training.py em um ambiente Python.
O script irá baixar o conjunto de imagens da internet e começará o processo de treinamento do modelo YOLOv8.
Após o treinamento, o modelo será salvo no formato .pt para uso posterior.

## Script principal - model.py

Execute o código em um ambiente Python.
O programa abrirá uma janela chamada "Webcam" exibindo o vídeo capturado pela webcam.
Os objetos detectados serão marcados com retângulos brancos e o nome do objeto será exibido próximo a cada retângulo.

## Link do Youtube

https://youtu.be/QXdE4vfUh5s
