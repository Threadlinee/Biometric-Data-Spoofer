import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

image = cv2.imread('captured_face.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = detector(gray)

for face in faces:
    landmarks = predictor(gray, face)

    aligned_face = dlib.get_face_chip(image, landmarks)

    cv2.imwrite('aligned_face.jpg', aligned_face)
    print("Face aligned and saved as 'aligned_face.jpg'")

