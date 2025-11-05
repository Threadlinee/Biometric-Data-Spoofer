import tkinter as tk
from tkinter import filedialog
import subprocess

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

root.mainloop()