# Importando bibliotecas necessárias
from ultralytics import YOLO
import cv2

# Carregando o modelo YOLO
model = YOLO("./yolo.pt")

# Inicializando a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

# Loop principal
while True:
    # Lendo o próximo frame da webcam
    ret, frame = cap.read()

    # Realizando a detecção de objetos no frame usando o modelo YOLO
    results = model(frame)

    # Anotando o frame com as detecções
    annotated_frame = results[0].plot()

    # Realizando a predição contínua do modelo no frame
    results = model.predict(frame, stream=True)

    # Iterando sobre os resultados da predição
    for result in results:
        # Obtendo as coordenadas dos retângulos das caixas delimitadoras
        boxes = result.boxes.cpu().numpy()

        # Iterando sobre as caixas delimitadoras
        for box in boxes:
            # Obtendo as coordenadas do retângulo
            r = box.xyxy[0].astype(int)
            print(r)

            # Desenhando o retângulo no frame
            cv2.rectangle(frame, r[:2], r[2:], (255, 255, 255), 2)

            # Definindo a fonte e escrevendo o nome do objeto detectado
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(
                frame,
                result.names[int(box.cls[0])],
                (r[0] + 6, r[1] - 20),
                font,
                1.0,
                (255, 255, 255),
                1,
            )

    # Exibindo o frame com as detecções na janela "Webcam"
    cv2.imshow("Webcam", frame)

    # Verificando se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberando a captura de vídeo e fechando as janelas
cap.release()
cv2.destroyAllWindows()
