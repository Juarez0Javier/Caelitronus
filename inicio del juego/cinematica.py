from moviepy.editor import VideoFileClip
import subprocess
import sys

try:
    clip = VideoFileClip("prologo.mp4")
    clip.preview()
    clip.close()
except Exception as e:
    print("Error al reproducir el video:", e)
    sys.exit()

subprocess.run(["python", "juego.py"])
