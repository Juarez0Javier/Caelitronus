import pygame
import sys
import subprocess
import json
import os

pygame.init()

def cargar_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    else:
        return {"musica": 0.5, "efectos": 0.5}

config = cargar_config()

WIDTH, HEIGHT = 920, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caeltronos")

try:
    background = pygame.image.load("font.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    pygame.mixer.music.load("violin.mp3")
    pygame.mixer.music.set_volume(config["musica"])
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Error cargando recursos: {e}")
    sys.exit()

opciones = ["COMENZAR PARTIDA", "AJUSTES", "CREDITOS", "SALIR"]
selected = -1

COLOR_NORMAL = (200, 190, 175)
COLOR_SELECCIONADO = (160, 150, 135)

class MatrixFont:
    def __init__(self, font_path, base_size, hover_size):
        self.font_path = font_path
        self.base_size = base_size
        self.hover_size = hover_size

    def render(self, text, selected):
        size = self.hover_size if selected else self.base_size
        font = pygame.font.Font(self.font_path, size)
        color = COLOR_SELECCIONADO if selected else COLOR_NORMAL
        return font.render(text, True, color)

font_renderer = MatrixFont("matrix mono.ttf", 36, 24)

def draw_menu():
    screen.blit(background, (0, 0))
    for i, opcion in enumerate(opciones):
        is_selected = (selected == i)
        text_surface = font_renderer.render(opcion, is_selected)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 60))
        screen.blit(text_surface, text_rect)

clock = pygame.time.Clock()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and selected != -1:
            if event.button == 1:
                if selected == 0:
                    pygame.quit()
                    subprocess.run(["python", "cinematica.py"])
                    sys.exit()
                elif selected == 1:
                    pygame.quit()
                    subprocess.run(["python", "ajuste.py"])
                    sys.exit()
                elif selected == 2:
                    print("Mostrando créditos...")
                elif selected == 3:
                    running = False

    selected = -1
    for i in range(len(opciones)):
        text_surface = font_renderer.render(opciones[i], False)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 60))
        if text_rect.collidepoint(mouse_pos):
            selected = i
            break

    draw_menu()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
