# Importa as bibliotecas para: captura e manipulação de vídeo, detecção de rostos
import cv2
import mediapipe as mp
import os
# Inicializa a captura de vídeo pela webcam usando o parâmetro "1" indicando qua câmera usar (0 geralmente é a câmera padrão)
webcam = cv2.VideoCapture(1)
# Objeto de detecção de rostos do MediaPipe
rcd = mp.solutions.face_detection
rr = rcd.FaceDetection()

# Desnha os resultados na tela
desenho = mp.solutions.drawing_utils

# Loop infinito para capturar os framas em tempo real
while True:
    # Lê um frame da webcam
    verificador, frame = webcam.read()
    # Se não conseguir, interrompe o loop 
    if not verificador:
      break
    # Processa o frame para detectar rostos
    lista_rostos = rr.process(frame)
    # Se detectar rostos, faz um desenho em volta deles
    if lista_rostos.detections:
       for rosto in lista_rostos.detections:
          desenho.draw_detection(frame, rosto)
    # Exibe o frame com os rostos detectados em uma janela
    cv2.imshow("Rostos na webcam", frame)
    # Espera 5ms por uma tecla. Se for 'ESC' (código 27), encerra o loop   
    if cv2.waitKey(5) == 27:
       break
    




webcam.release()
cv2.destroyAllWindows()
