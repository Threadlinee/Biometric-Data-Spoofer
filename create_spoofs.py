from deepface import DeepFace

img = 'aligned_face.jpg'

DeepFace.generate_video(img, 'deepfake_video.mp4')
print("Deepfake video generated as 'deepfake_video.mp4'")

