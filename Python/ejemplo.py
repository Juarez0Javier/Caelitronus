import cv2
import pygame
import sys

# Inicializar Pygame
pygame.init()
screen_width = 1030
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reproducción de Video con OpenCV y Pygame")

# Ruta del video (usa la ruta absoluta para evitar errores)
video_path = r"D:\juegos\Caelitronus\Assets\Movie\prologo.mp4"

# Cargar el video con OpenCV
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: no se pudo abrir el video.")
    sys.exit()

# Obtener FPS del video
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:  # fallback si no se puede obtener FPS
    fps = 30
frame_delay = int(1000 / fps)  # delay en milisegundos

# Ajustar tamaño del video a la ventana
resize_width, resize_height = screen_width, screen_height

running = True
while running:
    ret, frame = cap.read()
    if not ret:
        break  # Termina si el video se acabó

    # Convertir BGR (OpenCV) a RGB (Pygame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Redimensionar frame al tamaño de la ventana
    frame = cv2.resize(frame, (resize_width, resize_height))

    # Convertir el frame a superficie de Pygame
    frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

    # Mostrar el frame en pantalla
    screen.blit(frame_surface, (0, 0))
    pygame.display.flip()

    # Delay según FPS
    pygame.time.delay(frame_delay)

    # Manejar eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

# Liberar recursos
cap.release()
pygame.quit()
