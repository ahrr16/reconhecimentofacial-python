import cv2
import mediapipe as mp
import os
webcam = cv2.VideoCapture(1)
rcd = mp.solutions.face_detection
rr = rcd.FaceDetection()
desenho = mp.solutions.drawing_utils
 
while True:
    verificador, frame = webcam.read()

    if not verificador:
      break

    lista_rostos = rr.process(frame)

    if lista_rostos.detections:
       for rosto in lista_rostos.detections:
          desenho.draw_detection(frame, rosto)
    cv2.imshow("Rostos na webcam", frame)
    if cv2.waitKey(5) == 27:
       break
    




webcam.release()
cv2.destroyAllWindows()