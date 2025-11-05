import cv2

# Load the deepfake video
cap = cv2.VideoCapture('deepfake_video.mp4')

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Play the video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Deepfake Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()