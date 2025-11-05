import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def capture_fingerprint():
    subprocess.run(["python", "capture_fingerprint.py"])

def capture_face():
    subprocess.run(["python", "capture_face.py"])

def capture_iris():
    subprocess.run(["python", "capture_iris.py"])

def process_fingerprint():
    subprocess.run(["python", "process_fingerprint.py"])

def process_face():
    subprocess.run(["python", "process_face.py"])

def process_iris():
    subprocess.run(["python", "process_iris.py"])

def create_spoofs():
    subprocess.run(["python", "create_spoofs.py"])

def deliver_spoofs():
    subprocess.run(["python", "deliver_spoofs.py"])

def generate_deepfake():
    # Open a file dialog to select the source image
    source_image_path = filedialog.askopenfilename(title="Select Source Image", filetypes=[("Image files", "*.jpg *.png")])
    if not source_image_path:
        return

    # Open a file dialog to select the target video
    target_video_path = filedialog.askopenfilename(title="Select Target Video", filetypes=[("Video files", "*.mp4 *.avi")])
    if not target_video_path:
        return

    # Generate the deepfake video using Deep Live Cam
    output_video_path = 'deepfake_output.mp4'
    os.system(f'python run.py -s {source_image_path} -t {target_video_path} -o {output_video_path}')

    print(f"Deepfake video generated and saved as '{output_video_path}'")

root = tk.Tk()
root.title("Biometric Data Spoofer")

tk.Button(root, text="Capture Fingerprint", command=capture_fingerprint).pack()
tk.Button(root, text="Capture Face", command=capture_face).pack()
tk.Button(root, text="Capture Iris", command=capture_iris).pack()
tk.Button(root, text="Process Fingerprint", command=process_fingerprint).pack()
tk.Button(root, text="Process Face", command=process_face).pack()
tk.Button(root, text="Process Iris", command=process_iris).pack()
tk.Button(root, text="Create Spoofs", command=create_spoofs).pack()
tk.Button(root, text="Deliver Spoofs", command=deliver_spoofs).pack()
tk.Button(root, text="Generate Deepfake", command=generate_deepfake).pack()

root.mainloop()