# importando libs
import numpy as np
import mediapipe as mp
import cv2 as cv

#  Index dos Olhos e das Íris 
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]
# Configurando Malha e webcam
mp_face_mesh = mp.solutions.face_mesh
cap = cv.VideoCapture(0)
face_recognize_solution = mp.solutions.face_detection
face_recognize = face_recognize_solution.FaceDetection()
# Inicializando drawing utils
draw = mp.solutions.drawing_utils


def FaceDetection():
    with mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
    ) as face_mesh:
        while True:
            # Verificando se está lendo a Webcam e capturando os frames
            verify, frame = cap.read()

            # Verificando se consegue ler a câmera
            if not verify:
                break

            # Pegando todas as faces que a câmera encontra
            face_list = face_recognize.process(frame)

            # Desenhando em volta de todas as faces que a câmera encontra
            if face_list.detections:
                for face in face_list.detections:
                    draw.draw_detection(frame, face)

            # Inicializando malha customizavel
            frame = cv.flip(frame, 1)
            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img_height, img_width = frame.shape[:2]
            results = face_mesh.process(rgb_frame)
            if results.multi_face_landmarks:
                mesh_points = np.array([np.multiply([p.x, p.y], [img_width, img_height]).astype(int) for p in
                                        results.multi_face_landmarks[0].landmark])
                # Desenhando elipse pros olhos
                cv.polylines(frame, [mesh_points[LEFT_EYE]], True, (0, 255, 0), 1, cv.LINE_AA)
                cv.polylines(frame, [mesh_points[RIGHT_EYE]], True, (0, 255, 0), 1, cv.LINE_AA)
                # Pegando eixo e raio das iris
                (left_cx, left_cy), left_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
                (right_cx, right_cy), right_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
                # Marcando posição central da iris
                center_left = np.array([left_cx, left_cy], dtype=np.int32)
                center_right = np.array([right_cx, right_cy], dtype=np.int32)
                # Desenhando circunferência em volta da Iris
                cv.circle(frame, center_left, int(left_radius), (255, 0, 255), 1, cv.LINE_AA)
                cv.circle(frame, center_right, int(right_radius), (255, 0, 255), 1, cv.LINE_AA)
            # Abrindo janela da câmera
            cv.imshow('WebCam', frame)

            # Para Aplicação
            if cv.waitKey(5) == 27:
                break

    cap.release()
    cv.destroyAllWindows()
