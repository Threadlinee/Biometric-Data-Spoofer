import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

ret, frame = cap.read()

if ret:
    cv2.imwrite('captured_face.jpg', frame)
    print("Face captured and saved as 'captured_face.jpg'")
else:
    print("Error: Could not capture image.")

cap.release()
cv2.destroyAllWindows()