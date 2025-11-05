import cv2

cap = cv2.VideoCapture('deepfake_video.mp4')

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Deepfake Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

